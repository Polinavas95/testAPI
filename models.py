from tortoise import models, fields
from tortoise.contrib.pydantic import pydantic_model_creator



class Item(models.Model):
	"""A model of items
	"""
	id = fields.IntField(pk=True)
	cargo_type = fields.TextField()
	rate = fields.FloatField()
	date = fields.DateField(auto_now=True)

	async def save(self, *args, **kwargs) -> None:
		self.rate = 12.5
		await super().save(*args, **kwargs)

	class PydanticMeta:
		allow_cycles = False


#Pydantic schemas
ItemPydantic = pydantic_model_creator(Item, name='Items')
ItemInPydantic = pydantic_model_creator(Item, name='ItemsIn', exclude_readonly=True)