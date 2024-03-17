import os
from fastapi import FastAPI, File, UploadFile
from .services import extract_info
from .models import LabReportInfo

app = FastAPI()


@app.post("/extract-info/", response_model=LabReportInfo)
async def extract_info_endpoint(file: UploadFile = File(...)):
    # Save the uploaded file temporarily
    temp_file_path = f"temp_{file.filename}"
    with open(temp_file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Extract the information from the file
    extracted_data = extract_info(temp_file_path)

    # Remove the temporary file
    os.remove(temp_file_path)

    return extracted_data
