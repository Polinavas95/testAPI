from datetime import date
from typing import List
from pydantic import BaseModel


class Rate(BaseModel):
    cargo_type: str
    rate: float

class Date_item(BaseModel):
    date: date
    rows: List[Rate]


class Status(BaseModel):
    message: str