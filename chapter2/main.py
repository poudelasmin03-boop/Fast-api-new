from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
  return {
    "message":"This is home page.."
  }

@app.get("/user/{user_id}")
async def get_user(user_id :int):
  return {
    "userid":user_id,
    "message":f"{user_id} this is page of user"
  }