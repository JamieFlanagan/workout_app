"""Here is where I will have the main and all of my routers

I want to have chest, shoulders, biceps, triceps, abs, legs, cardio 
Each one of these will have its own router

A workout will have minimum 4 of these exercices. It will have a time stamp for start and end
Users will also be able to name their workouts too

"""

from fastapi import FastAPI, APIRouter

from .routers.chest_exercises_router import chest_router
from .routers.back_exercise_router import back_router
from .routers.workout_router import workout_router
from .routers.user_router import user_router

from db.workout_db_sql import engine
from db.models.entities import Base


app = FastAPI()

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

app.include_router(chest_router)
app.include_router(back_router)
app.include_router(workout_router)
app.include_router(user_router)
