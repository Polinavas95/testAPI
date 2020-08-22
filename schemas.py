from datetime import datetime

from pydantic import BaseModel


class ItemRequestModel(BaseModel):
    rate: float
    cargo_type: str


class Date_Item(BaseModel):
    date: datetime


class Status(BaseModel):
    message: str