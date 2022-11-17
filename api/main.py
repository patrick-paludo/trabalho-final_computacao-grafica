from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

from hooks.teste import teste

class Item(BaseModel):
  name: str
  age: str

app = FastAPI()

@app.get("/")
def home():
  return "Teste API"

@app.post('/testepost')
def testepost(item: Item):
  return teste(item.name, item.age)

@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}