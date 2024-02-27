from pydantic import BaseModel, Field
from typing import Optional

class Update_employee_request(BaseModel):
        name: str = Field(...,description="Employee Names",min_length=2,max_length=50)
        email: str = Field(...,description="Employee Email",min_length=13,max_length=50)
        phone: Optional[int] = Field(None ,description="Employee Phone Number")