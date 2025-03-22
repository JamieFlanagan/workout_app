from fastapi import APIRouter
from pydantic import BaseModel

class BackExcerise(BaseModel):
    name:str
    description:str
    category:str

back_router = APIRouter(tags=["Back"])



@back_router.post("/users/back/exercise")
def post_back_excerise(back_exercise:BackExcerise):
    return back_exercise