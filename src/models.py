from pydantic import BaseModel


class PhysicianInfo(BaseModel):
    name: str


class PatientInfo(BaseModel):
    name: str
    dob: str
    address: str
    gender: str


class LabReportInfo(BaseModel):
    physician: PhysicianInfo
    patient: PatientInfo
