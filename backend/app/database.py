import os
from sqlalchemy import create_engine, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(DATABASE_URL)


class Base(DeclarativeBase):
    pass


class Blog(Base):
    __tablename__ = "blogs"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    content: Mapped[str] = mapped_column(Text)


Base.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


def add_blog(session: Session, title: str, content: str) -> Blog:
    blog = Blog(title=title, content=content)
    session.add(blog)
    session.commit()
    session.refresh(blog)
    return blog


def list_blogs(session: Session) -> list[Blog]:
    return session.query(Blog).all()
