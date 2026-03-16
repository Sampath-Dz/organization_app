from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.assignment import AssignmentCreate, AssignmentRead
from ..services.assignment import AssignmentService
from ..models.db_factory import get_db

router = APIRouter(prefix="/auth/v1/assignments", tags=["Assignments"])

@router.post("", response_model=AssignmentRead)
def create_assignment(data: AssignmentCreate, db: Session = Depends(get_db)):
    service = AssignmentService(db)
    return service.create_assignment(data)

@router.get("", response_model=list[AssignmentRead])
def list_assignments(db: Session = Depends(get_db)):
    service = AssignmentService(db)
    return service.get_assignments()
