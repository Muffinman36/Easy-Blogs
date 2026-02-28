import os
import re
from datetime import datetime
from sqlalchemy import create_engine, String, Text, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(DATABASE_URL)


class Base(DeclarativeBase):
    pass


class Blog(Base):
    __tablename__ = "blogs"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    slug: Mapped[str] = mapped_column(String(200), unique=True)
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


Base.metadata.create_all(engine)


def _slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text.strip())
    return text


def get_session():
    with Session(engine) as session:
        yield session


def add_blog(session: Session, title: str, content: str, slug: str | None = None) -> Blog:
    blog = Blog(title=title, content=content, slug=slug or _slugify(title))
    session.add(blog)
    session.commit()
    session.refresh(blog)
    return blog


def list_blogs(session: Session, page: int = 1, page_size: int = 10) -> dict:
    total = session.query(Blog).count()
    total_pages = max(1, -(-total // page_size))  # ceiling division
    blogs = (
        session.query(Blog)
        .order_by(Blog.created_at.desc())
        .offset((page - 1) * page_size)
        .limit(page_size)
        .all()
    )
    return {"page": page, "total_pages": total_pages, "blogs": blogs}


def get_blog_by_slug(session: Session, slug: str) -> Blog | None:
    return session.query(Blog).filter(Blog.slug == slug).first()
