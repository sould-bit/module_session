from fastapi import FastAPI
from app.register.endpoint import router as register_router
from app.session.endpoint import router as loguin_router
from app.baseconfig import create_db_and_table

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_table()

app.include_router(register_router, prefix="/api/v1", tags=["register"])
app.include_router(loguin_router, prefix="/api/v1", tags=["login"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="[IP_ADDRESS]", port=8000)
