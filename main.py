from fastapi import FastAPI
from modules import (
    bao_gia,
    upload_pyc,
    upload_bienban,
    upload_kemtheo
)

app = FastAPI()

# Gắn các router từ từng modules
app.include_router(upload_pyc.router)
app.include_router(upload_bienban.router)
app.include_router(upload_kemtheo.router)
app.include_router(send_email.router)
app.include_router(log_utils.router)
app.include_router(bao_gia_core.router)

@app.get("/")
def root():
    return {"message": "✅ Backend FastAPI is running"}
