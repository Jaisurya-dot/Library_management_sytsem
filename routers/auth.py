from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from schemas.user import UserCreate, UserResponse
from services.auth_service import create_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201
)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db, user)