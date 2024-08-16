from fastapi import FastAPI

app = FastAPI()

# Override `value` to be whatever you want your metrics-api response
#  to look like.
# Top-level recommended to be a dict/list but by no means necessary.
value = {
    "value": "default"
}


@app.get("/value")
async def get_value():
    return value


@app.post("/value")
async def set_value(value: dict):
    value = value