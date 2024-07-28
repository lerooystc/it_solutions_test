from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class CreateAdvert(BaseModel):
    title: str = Field(..., min_length=30)
    author: str
    viewcount: int
    position: int


class ShowAdvert(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str = Field(..., min_length=30)
    author: str 
    viewcount: int
    position: int