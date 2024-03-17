from pydantic import BaseModel
from typing import Optional


class PhysicianInfo(BaseModel):
    name: Optional[str]


class PatientInfo(BaseModel):
    name: Optional[str]
    dob: Optional[str]
    address: Optional[str]
    gender: Optional[str]


class LabReportInfo(BaseModel):
    physician: Optional[PhysicianInfo]
    patient: Optional[PatientInfo]
