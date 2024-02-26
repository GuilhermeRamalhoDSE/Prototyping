from datetime import date
from pydantic import BaseModel

class LicenseSchema(BaseModel):
    customer_id: int
    name: str
    email: str
    address: str
    tel: str
    license_code: str
    active: bool
    start_date: date
    end_date: date

    class Config:
        from_attributes = True  

class LicenseCreateSchema(BaseModel):
    customer_id: int
    name: str
    email: str
    address: str
    tel: str
    license_code: str
    active: bool
    start_date: date
    end_date: date

class LicenseUpdateSchema(BaseModel):
    name: str = None
    email: str = None
    address: str = None
    tel: str = None
    license_code: str = None
    active: bool = None
    start_date: date = None
    end_date: date = None
