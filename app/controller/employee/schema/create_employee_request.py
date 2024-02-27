from pydantic import BaseModel, Field
from typing import Optional

class Create_employee_request(BaseModel):
        name: str = Field(...,description="Employee Names",min_length=2,max_length=50)
        email: str = Field(...,description="Employee Email",min_length=13,max_length=50)
        phone: Optional[int] = Field(None ,description="Employee Phone Number")
        role: str = Field(None ,description="Employee Role")
        schedule: str = Field(None ,description="Employee Daily Schedule")