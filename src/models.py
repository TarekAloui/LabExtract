from pydantic import BaseModel
from typing import Optional


class PhysicianInfo(BaseModel):
    physician_name: Optional[str]


class PatientInfo(BaseModel):
    patient_name: Optional[str]
    patient_dob: Optional[str]
    patient_address: Optional[str]
    patient_gender: Optional[str]


class LabReportInfo(BaseModel):
    patient: Optional[PatientInfo]
    physician: Optional[PhysicianInfo]
