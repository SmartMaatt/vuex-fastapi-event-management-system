from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from ..functions import user
from ..database import get_db
from .. import schemas

router = APIRouter(
    tags=['Users']
)

# >>> POST methods
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_event(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_event(request, db)


# >>> GET methods
@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowUser])
def get_all_events(db: Session = Depends(get_db)):
    return user.get_all_events(db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_event_by_id(id: int, db: Session = Depends(get_db)):
    return user.get_event_by_id(id, db)


# >>> DELETE methods
@router.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
def delete_event_by_id(id: int, db: Session = Depends(get_db)):
    return user.delete_event_by_id(id, db)


# >>> PUT methods
@router.put('/{id}', status_code=status.HTTP_200_OK)
def put_event_by_id(id: int, request: schemas.User, db: Session = Depends(get_db)):
    return user.put_event_by_id(id, request, db)
