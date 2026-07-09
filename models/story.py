from sqlalchemy import Column, Integer,String, DateTime,Boolean,ForeignKey,JSON,VARCHAR,TEXT,DATE  

from sqlalchemy.sql import func

from sqlalchemy.orm import relationship

from db.database import Base

import uuid

from sqlalchemy.dialects.postgresql import UUID


class Users(Base):
    __tablename__='users'
    id=Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    full_name=Column(VARCHAR(150),unique=True,nullable=False)
    email=Column(VARCHAR(150),unique=True,nullable=False)
    password=Column(TEXT,nullable=False)
    role = Column(VARCHAR(20), nullable=False, default="user")
    is_active = Column(Boolean, default=True)
    created_at=Column(DateTime(timezone=True),server_default=func.now())
    borrowed_books = relationship(
    "Borrow_Table",
    back_populates="user",
    cascade="all, delete"
)

class Books_Table(Base):
    __tablename__="books_table"
    id=Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    title=Column(VARCHAR(250),unique=True,nullable=False)
    author=Column(VARCHAR(100),nullable=False)
    isbn=Column(VARCHAR(100),nullable=False)
    category=Column(VARCHAR(150),nullable=False)
    quantity=Column(Integer)
    available_quantity=Column(Integer)
    description=Column(TEXT)
    cover_image=Column(TEXT)
    created_at=Column(DateTime(timezone=True),server_default=func.now())
    borrow_records = relationship(
    "Borrow_Table",
    back_populates="book",
    cascade="all, delete"
)


class Borrow_Table(Base):
    __tablename__="borrow_table"
    id=Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    user_id=Column(UUID(as_uuid=True),ForeignKey("users.id"))
    book_id=Column(UUID(as_uuid=True),ForeignKey("books_table.id"))
    borrow_date=Column(DATE)
    due_date=Column(DATE)
    return_date=Column(DATE)
    status=Column(VARCHAR(100))
    user = relationship(
    "Users",
    back_populates="borrowed_books"
)

    book = relationship(
    "Books_Table",
    back_populates="borrow_records"
)
