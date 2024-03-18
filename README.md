# Project Information:
- The project uses unstructured for extracting the text from the document (including using OCR if the input is an image)
- The project uses langchain and kor extraction_chain in order to extract the relevant fields
- The llm model used is `gpt-4-1106-preview`

# How to run the endpoint locally

## Step 1: add env variables
- You need to include a folder at the top level called `env` and inside, you should add a `.env.dev` file
  where you specify your OPENAI_API_KEY environment variable

## Step 2: build and run the dev docker image locally using docker compose
- docker compose -f docker-compose.dev.yaml up --build


## Step3: navigate to the API docs to test the endpoint directly
- Navigate to `http://localhost:8000/docs#/default/extract_info_endpoint_extract_info__post` where you will find the Swagger UI that
  displays information about the endpoint, and gives you the option to `try it out` directly by uploading a file and then pressing `execute`


Please note: 
- The endpoint was tested on jpeg and pdf, but should be able to accept other formats (txt, json, etc)

