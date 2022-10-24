from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
	brand: Optional[str] = None
	year: int
	electric: bool
	colors: object

# this class will be used to update items
# the items variables will be all optional so the  user doesn't have to add
# every single information in order to change a single one
class UpdateItem(BaseModel):
	brand: Optional[str] = None
	year: Optional[int] = None
	electric: Optional[bool] = None
	colors: Optional[object] = None

#initializes the FastAPI

# creates an endpoint (a "route", the path after the
# main domain)
# base url (ex:localhost)
# /something (ex:home, the endpoint)
# also contains the http method (get, post, put, delete etc) which we need
# the endpoint "to be"
# the route must be right above the function that will be triggered when going
# to the route/endpoint
app = FastAPI()

# run with python3 -m uvicorn app.working:app --reload
#@app.get("/")
#def home():
#	return {"Data": "Test"}
	# a python dictionary that is automatically converted into json object by
	# FastAPI.
	# The reverse also happens: in the response, the json body will be converted
	# into vanilla python types

#@app.get("/about")
#def about():
#    	return{"Data": "About"}

inventory = {}

# -> Working with Path()
# None is the default value when no valid value is passed, mandatory
# The Path() parameter adds the description to documentation
# gt and lt are used to define "less than" and "greater than" limits
@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="The Id of the item to view", gt=0)):
	return inventory[item_id]

# -> Working with Query
# accepts one query parameter -> brand:str
# get-by-brand?brand=Ford -> the "?" indicates a query, multiple will require
# ampersand "&"
# adding "=None" after the query parameter makes it optional, otherwise is
# mandatory
# it is also possible to import Optional from lib typing and use it for better
# readability and autocompletion (not mandatory)
# nice information about parameters order: "https://youtu.be/-ykeT6kk4bk?t=1978
# (min 32)"
# it is possible to combine Path parameters and query items.
@app.get("/get-by-brand/{item_id}")
def get_item(*, item_id: int, brand: Optional[str]):
	for item_id in inventory:
		# because we will be inserting "item objects" into our inventory using the "post" method, we need to change the way we are getting itens
		# if inventory[item_id]["brand"] == brand:
		if inventory[item_id].brand == brand:
			return inventory[item_id]
	# return {"Data": "Not Found"}
	raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
		detail="Item_id nor found in inventory")

# -> Working with request body Item
# item_id, as it is in the path. is a Path parameter
# to access the items from the object, we can use the "name": item.name"
# structure
@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
	if item_id in inventory:
	#	return {"Error! Item id already in the inventory"}
		raise HTTPException(status_code= status.HTTP_400_NOT_FOUND,
			detail="Item_id already found in inventory")
	# because fastAPI already automatically converts dictionaries into json
	# objects, we don't need to access the items using "name: name.item" while
	# using fastAPI
	# inventory[item_id] = {"brand": item.brand, "electric": item.electric,
	# "year": item.year, "colors": item.colors}
	inventory[item_id] = item
	return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
	if item_id not in inventory:
	#	return {"Error! Item id not in inventory"}
		raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
			detail="Item_id not found in inventory")

	if item.brand != None:
		inventory[item_id].brand = item.brand
	if item.year != None:
		inventory[item_id].year = item.year
	if item.electric != None:
		inventory[item_id].electric = item.electric
	if item.colors != None:
		inventory[item_id].colors = item.colors
	return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id: int = Query(...,
	description="The ID of the item to delete", gt = 0)):
	if item_id not in inventory:
	#	return {"Error! Id does not exist"}
		raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
			detail="Item_id not found in inventory")
	del inventory[item_id]
	#return {"Success": "Item successfully deleted from inventory"}
	raise HTTPException(status_code= status.HTTP_200_OK,
		detail="Successfully delete!")


