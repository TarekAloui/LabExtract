import os
from fastapi import FastAPI, File, UploadFile
from src.services import extract_info
from src.models import LabReportInfo

app = FastAPI()


@app.post("/extract-info/", response_model=LabReportInfo)
async def extract_info_endpoint(file: UploadFile = File(...)):
    # Save the uploaded file temporarily
    if not os.path.exists("tmp"):
        os.makedirs("tmp")
    temp_file_path = f"/tmp/temp_{file.filename}"
    with open(temp_file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Extract the information from the file
    extracted_data = extract_info(temp_file_path)
    extracted_data = (
        extracted_data["lab_report"]
        if "lab_report" in extracted_data
        else extracted_data
    )

    # Remove the temporary file
    os.remove(temp_file_path)

    return extracted_data
