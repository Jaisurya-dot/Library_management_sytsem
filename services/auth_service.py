from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from models.story import Users
from schemas.user import UserCreate
from core.security import hash_password


def create_user(db: Session, user: UserCreate):

    existing_user = (
        db.query(Users)
        .filter(Users.email == user.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    new_user = Users(
        full_name=user.full_name,
        email=user.email,
        password=hash_password(user.password),
        role="user",
        is_active=True,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user