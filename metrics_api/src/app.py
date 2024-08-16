from fastapi import FastAPI
import logging

app = FastAPI()
logger = logging.getLogger(__name__)

# Override `value` to be whatever shape you expect your 
#  metrics-api response to look like.
# Top-level recommended to be a dict/list but by no means necessary.
value = {
    "stuff": 1
}

@app.get("/value")
async def get_value():
    print(f"Returning value: '{value}'")
    return value


@app.post("/value")
async def set_value(request_value: dict):
    global value
    value = request_value
    print(f"Value set to '{value}'")