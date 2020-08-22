from typing import List, Dict
from fastapi import FastAPI, HTTPException
from tortoise.contrib.fastapi import register_tortoise, HTTPNotFoundError
from models import Item, ItemPydantic, ItemInPydantic
from schemas import Date_Item, ItemRequestModel, Status
from datetime import datetime


app = FastAPI()


@app.post('/items', response_model=ItemPydantic)
async def create_rate(item: ItemInPydantic):
	item_obj = await Item.create(**item.dict(exclude_unset=True))
	return await ItemPydantic.from_tortoise_orm(item_obj)



@app.get('/items', response_model=List[ItemPydantic])
async def get_rate():
	return await ItemPydantic.from_queryset(Item.all())



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