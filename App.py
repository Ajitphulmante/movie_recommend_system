from fastapi import FastAPI
from pydantic import BaseModel
from pratice import predict
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


app = FastAPI()

# CORS settings
origins = [
    "http://localhost:3000",  # Add your frontend origin(s) here
]

# Add the middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    movie_name: str

@app.get("/")
async def home():
    return {"hello world"}

@app.post("/recommed")
async def recommed(data: InputData):
    prediction = predict(data.movie_name)
    return {"prediction": prediction}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)