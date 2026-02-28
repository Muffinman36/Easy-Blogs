from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import get_session, add_blog, list_blogs

app = FastAPI()


class BlogCreate(BaseModel):
    title: str
    content: str


@app.get("/blogs")
async def get_blogs(db: Session = Depends(get_session)):
    return list_blogs(db)


@app.post("/blog")
async def add_blog_endpoint(blog: BlogCreate, db: Session = Depends(get_session)):
    return add_blog(db, blog.title, blog.content)
