from typing import List, Optional

from pydantic import BaseModel

class ModelCard(BaseModel):
    id: str
    object: str
    created: int
    owned_by: str
    root: Optional[str] = None
    parent: Optional[str] = None


class ModelList(BaseModel):
    object: str
    data: List[ModelCard]
