from pydantic import Basemodel
from typing import Optional
from uuid import UUID,

class Object(BaseModel):
    id: UUID,
    name: str,
    date_created: str
