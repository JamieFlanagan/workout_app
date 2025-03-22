from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from typing import List


workout_router = APIRouter(tags=["Workouts"])

class Exercise(BaseModel):
    name:str
    description:str
    muscle_group:str
    reps:int
    sets:int

class Workout(BaseModel):
    start_time:datetime
    excerises:List[Exercise]
    workout_name:str

@workout_router.post("/users/workout/add")
def add_workout(workout:Workout):
    return workout



"""
Users: Store user information.

Workouts: Store workout details (e.g., date, type).

Exercises: Store exercise details (e.g., name, description).

Workout Logs: Store user-specific workout logs (e.g., date completed, weight lifted).

One user can have many workouts 1-n
One workout can have many exercies 1-n
One exercise can belong to many workouts 1-n
"""

