import sqlite3
from sqlalchemy import Column, Row, Integer, String, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func
from datetime import datetime

Base = declarative_base()

class Workouts(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String(50), nullable=False)
    date = Column(DateTime, server_default=func.now())

    user = relationship("User", back_populates="workouts")
    workout_exercises = relationship("WorkoutExercise", back_populates="workout")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True) 
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    workouts = relationship("Workouts", back_populates="user")


class Exercise(Base):
    __tablename__ = "exercises"

    id=Column(Integer, primary_key=True)
    name=Column(String(50), unique=True, nullable=False)
    description=Column(String(100), nullable=False)
    muscle_group=Column(String(50), nullable=False)

    workout_exercises = relationship("WorkoutExercise", back_populates="exercise")

class WorkoutExercise(Base):
    __tablename__ = "workout_exercises"

    id= Column(Integer, primary_key=True)
    workout_id=Column(Integer, ForeignKey("workouts.id"), nullable=False)
    exercise_id=Column(Integer, ForeignKey("exercises.id"), nullable=False)
    sets = Column(Integer, nullable=False)
    reps = Column(Integer, nullable=False)

    workout = relationship("Workouts", back_populates="workout_exercises")
    exercise = relationship("Exercise", back_populates="workout_exercises")