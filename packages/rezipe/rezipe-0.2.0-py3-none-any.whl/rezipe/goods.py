from decimal import Decimal
import marvin
from pydantic import BaseModel
from dataclasses import dataclass

@dataclass
class Goods:
    name: str
    notes: str | None = None
    price: Decimal | None = None
    per_unit: str | None = None
    source: str | None = None
