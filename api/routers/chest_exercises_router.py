from fastapi import APIRouter
from pydantic import BaseModel

class ChestExercise(BaseModel):
    exercise_name:str
    number_reps: int
    sets_completed:int
    muscle_group:str
    category:str
    description:str


chest_router = APIRouter(tags=["Chest"])

@chest_router.post("/users/chest/exercise")
def add_chest_exercise(chest_exercise:ChestExercise):
    return chest_exercise