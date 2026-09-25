from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Inventory System API"}


@app.get("/health")
def health():
    return {"status": "ok"}