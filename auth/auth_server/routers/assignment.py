from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from ..utils import get_db
from ..models.models import Assignment

router=APIRouter(prefix="/auth/v1/assignments")


@router.get("")
def get_assignments(db:Session=Depends(get_db)):

    return db.query(Assignment).all()

from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from ..utils import get_db
from ..models.models import Assignment

router=APIRouter(prefix="/auth/v1/assignments")


@router.post("")
def create_assignment(data:dict,db:Session=Depends(get_db)):

    assignment=Assignment(**data)

    db.add(assignment)

    db.commit()

    db.refresh(assignment)

    return assignment


@router.get("")
def get_assignments(db:Session=Depends(get_db)):

    return db.query(Assignment).all()


@router.delete("/{id}")
def delete_assignment(id:int,db:Session=Depends(get_db)):

    obj=db.query(Assignment).filter(Assignment.id==id).first()

    db.delete(obj)

    db.commit()

    return {"message":"deleted"}
