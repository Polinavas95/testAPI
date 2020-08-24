
from typing import List, Dict
from fastapi import FastAPI, HTTPException
from tortoise.contrib.fastapi import register_tortoise, HTTPNotFoundError
from models import Item, ItemPydantic, ItemInPydantic, DatePydantic
from schemas import Date_Item, ItemRequestModel, Status
from datetime import datetime


app = FastAPI()


@app.post('/items', response_model=ItemPydantic)
async def create_rate(item: ItemInPydantic):
	item_obj = await Item.create(**item.dict(exclude_unset=True))
	return await ItemPydantic.from_tortoise_orm(item_obj)



@app.get('/items')
async def get_rate():
    qs = Item.all()
    dates = await DatePydantic.from_queryset(qs.only('date',))
    resp_dict = {}
    for date in dates:
        q = await ItemPydantic.from_queryset(qs.filter(date=date.date))
        resp_dict[date.date] = q
    return resp_dict



@app.delete('/items', responses={404: {'model': HTTPNotFoundError}})
async def delete_user(id: int):
    deleted_count = await Item.filter(id=id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f'Order {id} not found')
    return Status(message=f'Order {id} was delete')


register_tortoise(
    app,
    db_url="sqlite://sql_app.db",
    modules={"models": ["models"]},
    generate_schemas=True,

)