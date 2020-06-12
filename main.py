from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from typing import List

from validator import Validator
from sf import sf

app = FastAPI()


class Response(BaseModel):
    order_id: int
    error: dict
    code: List[int]


@app.post('/path', response_model=Response)
async def main_function(item: Validator):
    item = item.dict()
    r = Response(order_id=item['order_id'], error={}, code=[1])
    return r





#
# if __name__ == '__main__':
#     uvicorn.run(app, host='0.0.0.0', port=8000)
