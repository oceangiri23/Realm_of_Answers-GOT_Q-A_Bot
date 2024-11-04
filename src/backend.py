from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
from main import define_query 


app = FastAPI()

class InputModel(BaseModel):
    text: str


@app.post("/query")
def output(input: InputModel):
    if input.text == "CLS":
        raise HTTPException(status_code=400, detail="Error: 'CLS' is not a valid query.")
    
    response = "The answer is :", define_query(input.text)
    return response
