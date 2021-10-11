from fastapi import status, HTTPException
from .. import models


# s>> POST methods
def create_event(request, db):
    new_user = models.User(name=request.name, email=request.email, password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# GET methods
def get_all_events(db):
    all_users = db.query(models.User).all()
    return all_users

def get_event_by_id(id, db):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} is not available!')
    return user


# DELETE methods
def delete_event_by_id(id, db):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} is not available!')

    db.delete(user)
    db.commit()
    return {"Info": f"User on id {id} has been deleted successfully!"}


# PUT methods
def put_event_by_id(id, request, db):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} is not available!')

    user.name = request.name
    user.email = request.email
    user.password = request.password

    db.commit()
    return {"Info": f"User on id {id} has been updated successfully!"}
