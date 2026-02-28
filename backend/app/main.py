from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import get_session, add_blog, list_blogs, get_blog_by_slug

app = FastAPI()


class BlogCreate(BaseModel):
    title: str
    content: str
    slug: str | None = None


def _excerpt(content: str) -> str:
    return content.split("\n\n")[0]


@app.get("/blogs")
async def get_blogs(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_session),
):
    result = list_blogs(db, page=page, page_size=page_size)
    return {
        "page": result["page"],
        "total_pages": result["total_pages"],
        "results": [
            {
                "id": b.id,
                "slug": b.slug,
                "title": b.title,
                "excerpt": _excerpt(b.content),
                "createdAt": b.created_at.date().isoformat(),
            }
            for b in result["blogs"]
        ],
    }


@app.get("/blogs/{slug}")
async def get_blog(slug: str, db: Session = Depends(get_session)):
    blog = get_blog_by_slug(db, slug)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return {
        "id": blog.id,
        "slug": blog.slug,
        "title": blog.title,
        "content": blog.content,
        "createdAt": blog.created_at.date().isoformat(),
    }


@app.post("/blog")
async def add_blog_endpoint(blog: BlogCreate, db: Session = Depends(get_session)):
    try:
        return add_blog(db, blog.title, blog.content, blog.slug)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="A blog with that slug already exists")
