from pydantic import BaseModel


class Validator(BaseModel):
    order_id: int
    user_id: int