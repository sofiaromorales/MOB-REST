from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4

class Object(BaseModel):
    name: str
    date_created: Optional[str]
