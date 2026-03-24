from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional, List
from database import get_db, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class MovieCreate(BaseModel):
    title: str
    director: str
    year: Optional[int] = None

class MovieOut(MovieCreate):
    id: int
    class Config:
        from_attributes = True

@app.post("/movies", response_model=MovieOut, status_code=201)
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    db_movie = models.Movie(**movie.model_dump())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

@app.get("/movies/{movie_id}", response_model=MovieOut)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@app.get("/movies", response_model=List[MovieOut])
def list_movies(db: Session = Depends(get_db)):
    return db.query(models.Movie).all()