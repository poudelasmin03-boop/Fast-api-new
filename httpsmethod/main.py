from fastapi import FastAPI,Path,HTTPException,Query
import json
app = FastAPI()

product = []

def load_product():
  with open("product.json",'r') as f:
    data  = json.load(f)

  return data  

@app.get("/")
async def home_views():
  return {
    "message":"This is home page"
  }

@app.get("/about")
async def about_views():
  return {
    "message":"This is a about page"
  }


@app.get("/product")
async def product_views():
  data  = load_product()
  return data



####Get single product

@app.get("/product/{id}")
####here 3 dot means required and other are it's attribute
async def get_product(id:int =  Path(...,description="product id",example="4")):
  data = load_product()

  for product in data:
    if product["id"] == id:
      return {
        "data":data[id]
      } 

    ##status code
  raise HTTPException(status_code=404,detail = "Product not found")


@app.get("/sort")
async def sort(sort_by: str = Query(...,description="Sort on the basis of product name"),order:str = Query('asc',description="Sort in a asc or des")):
  valid_fields = ["name"]
  
  if sort_by not in valid_fields:
    raise HTTPException(status_code=400,detail=f"Invalid fields {valid_fields}")

  data = load_product()
  sorted_order = True if order == 'desc' else False
  sorted_data = sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sorted_order)
  return sorted_data
  
