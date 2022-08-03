from fastapi import FastAPI
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
)

"""
CORS or "Cross-Origin Resource Sharing" :-
refers to the situations when a frontend running in a browser has JavaScript code that communicates with a backend, and the backend is in a
different "origin" than the frontend.
"""

@app.get("/tasks")
async def all():
    return []
