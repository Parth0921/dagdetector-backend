from pydantic import BaseModel 
from typing import List


# defining the request body 
class Edge(BaseModel):
    source: str
    target: str

class PipelineData(BaseModel):
    nodes: List[str]
    edges: List[Edge]


