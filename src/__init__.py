from fastapi import FastAPI

version = "v1"

app = FastAPI(
 title="FastAPI Backend",
 description="Backend for Python-PostgreSQL setup",
 version=version
)

@app.get("/")
def test_route():
 return {"message": "Hello World"}