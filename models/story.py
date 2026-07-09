from sqlalchemy import Column, Integer,String, DateTime,Boolean,ForeignKey,JSON,VARCHAR,TEXT,UUID,DATE  

from sqlalchemy.sql import func

from sqlalchemy.orm import relationship

from db.database import Base

# __tablename__="stories"

#     id=Column(Integer,primary_key=True, index=True)
#     title=Column(String,index=True)
#     session_id=Column(String,index=True)

#     created_at=Column(DateTime(timezone=True),server_default=func.now())

#     nodes= relationship("StoryNode", back_populates="story")
class Users(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,index=True)
    full_name=Column(VARCHAR(150),unique=True,nullable=False)
    email=Column(VARCHAR(150),unique=True,nullable=False)
    password=Column(TEXT,nullable=False)
    role=Column(VARCHAR,nullable=False)
    is_active=Column(Boolean)
    created_at=Column(DateTime(timezone=True),server_default=func.now())


class Books_Table(Base):
    __tablename__="books_table"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(VARCHAR(250),unique=True,nullable=False)
    author=Column(VARCHAR(100),nullable=False)
    isbn=Column(VARCHAR(100),nullable=False)
    category=Column(VARCHAR(150),nullable=False)
    quatity=Column(Integer(500))
    available_quantity=Column(Integer(500))
    description=Column(TEXT)
    cover_image=Column(TEXT)
    created_at=Column(DateTime(timezone=True),server_default=func.now())



class Borrow_Table(Base):
    __tablename__="borrow_tabe"
    id=Column(UUID,primary_key=True,nullable=False)
    user_id=Column(UUID,unique=True,nullable=False)
    book_id=Column(UUID,unique=True,nullable=False)
    borrow_date=Column(DATE)
    due_date=Column(DATE)
    return_date=Column(DATE)
    status=Column(VARCHAR(100))