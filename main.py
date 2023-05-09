from fastapi import FastAPI, UploadFile
from extractText import extractSummary
from extractImage import *
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"])

@app.post("/api/startup/")
async def startup_event():
    await delete_files()

@app.post("/api/uploadfile/")
async def create_upload_file(file: UploadFile, num_sentences: int = 10):
    await extractImages(file.file)
    summary = await extractSummary(file.file, num_sentences)
    return summary
    
