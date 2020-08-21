from typing import List
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from .models import Item, ItemPydantic, ItemInPydantic

app = FastAPI()



@app.post('/items', response_model=ItemPydantic)
async def create_rate(item: ItemInPydantic):
	item_obj = await Item.create(**item.dict(exclude_unset=True))
	return await ItemPydantic.from_tortoise_orm(item_obj)


@app.get('/items', response_model=List[ItemPydantic])
async def get_rate():
	return await ItemPydantic.from_queryset(Item.all())


register_tortoise(
    app,
    db_url='sqlite://sql_app.db',
	models={'models':['models']},
	generate_schemas=True,
	add_exception_handlers=True,
)
