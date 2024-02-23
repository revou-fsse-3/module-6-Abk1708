from pydantic import BaseModel, Field
from typing import Optional

class Update_animal_request(BaseModel):
        species: str = Field(...,description="Animal Species Type",min_length=2,max_length=50)
        age: Optional[int] = Field(None ,description="Animal Age")
        gender: str = Field(None ,description="Animal gender")