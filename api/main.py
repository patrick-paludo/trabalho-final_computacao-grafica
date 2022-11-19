from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from pydantic import BaseModel

from hooks.cv import checkFile

class Item(BaseModel):
  name: str
  age: str

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
  return "A API está rodando!"

@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    imagem = checkFile(file)
    return Response(content=imagem, media_type="image/png")