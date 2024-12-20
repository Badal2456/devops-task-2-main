import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis import Redis

load_dotenv()

client = Redis.from_url(os.environ["REDIS_URI"], decode_responses=True)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    try:
        hits = client.incr("hits")  # Increment the key
        return {"hits": hits}
    except Exception as e:
        return {"error": str(e)}  # Return error message if Redis fails


@app.get("/hits")
def get_hits():
    try:
        hits = client.get("hits")  # Get the current value of hits
        if hits is None:
            hits = 0  # Default value if the key does not exist
        return {"hits": int(hits)}
    except Exception as e:
        return {"error": str(e)}  # Return error message if Redis fails
