from langchain.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from kor.extraction import create_extraction_chain
from langchain_openai import ChatOpenAI
from kor.nodes import Object, Text


def file_to_vector_db(file_path="lab_report.jpeg"):
    # Load the image file and extract text
    loader = UnstructuredFileLoader(file_path)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)

    # Create embeddings and store them in a vector database
    embeddings = OpenAIEmbeddings()
    vector_db = FAISS.from_documents(texts, embeddings)

    return vector_db


def extract_info_from_db(vector_db):
    # Define the schema for extracting patient and physician information using Kor
    patient_schema = Object(
        id="patient",
        description="Patient information from the lab report",
        attributes=[
            Text(id="name", description="Patient's full name"),
            Text(id="dob", description="Patient's date of birth"),
            Text(id="address", description="Patient's address"),
            Text(
                id="gender",
                description="Patient's gender. Options: M (Male), F (Female), O (Other)",
            ),
        ],
    )

    physician_schema = Object(
        id="physician",
        description="Ordering physician information",
        attributes=[
            Text(id="name", description="Ordering Physician's full name"),
        ],
    )

    lab_report_schema = Object(
        id="lab_report",
        description="Lab report information",
        attributes=[
            physician_schema,
            patient_schema,
        ],
        many=False,
    )

    # Create the extraction chain using Kor
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    extraction_chain = create_extraction_chain(
        llm, lab_report_schema, encoder_or_encoder_class="json"
    )

    # Query the vector database and extract information
    qa = RetrievalQA.from_chain_type(
        llm=llm, chain_type="stuff", retriever=vector_db.as_retriever()
    )

    def extract_info(query):
        relevant_docs = qa.retriever.get_relevant_documents(query)
        relevant_text = " ".join([doc.page_content for doc in relevant_docs])
        return extraction_chain.run(relevant_text)

    patient_info = extract_info(
        "Extract patient and physician information from the lab report including patient full name, date of birth, address, gender and physician full name."
    )["data"]

    return patient_info


def extract_info(file_path="lab_report.jpeg"):
    # Get the vector db
    vector_db = file_to_vector_db(file_path)

    # Extract the patient and physician information
    patient_info = extract_info_from_db(vector_db)

    return patient_info