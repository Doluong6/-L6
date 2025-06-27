from fastapi import FastAPI
from modules import (
    bao_gia,
    upload_pyc,
    upload_bienban,
    upload_kemtheo
)

app = FastAPI()

# Gắn các router từ từng module
app.include_router(bao_gia.router)
app.include_router(upload_pyc.router)
app.include_router(upload_bienban.router)
app.include_router(upload_kemtheo.router)

@app.get("/")
def root():
    return {"message": "✅ Backend FastAPI is running"}
