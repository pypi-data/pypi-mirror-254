from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Model:
    name: str
    columns: List[str]
    filter: Optional[str] = None
