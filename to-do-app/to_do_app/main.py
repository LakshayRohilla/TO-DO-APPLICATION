from sqlite3 import DatabaseError
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, Hashmodel


#1. Create a FastAPI app
app = FastAPI()

# 2. Add CORS middleware
"""
CORS or "Cross-Origin Resource Sharing" :-
refers to the situations when a frontend running in a browser has JavaScript code that communicates with a backend, and the backend is in a
different "origin" than the frontend.
"""
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

# 3. This is how we connect to redis database. 
redis_db = get_redis_connection(
    host="redis-10976.c305.ap-south-1-1.ec2.cloud.redislabs.com:10976",
    port = 10976,
    password = "sXci5kTjKJFxuz9drzS1NLYXRS3omoIE",
    decode_responses = True,
)

# 4. Data that we want to store in redis database.
class Task(Hashmodel):
    name: str
    complete: bool
    # 4.1 To add the model to redis database we make class meta.
    class Meta:
        database = redis_db

#1 
@app.get("/tasks")
async def all():
    # 5. Return all the tasks in the database.
    return Task.all_pks()
    
