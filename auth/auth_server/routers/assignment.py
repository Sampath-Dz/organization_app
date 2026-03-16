from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..services.assignment import AssignmentService
from ..schemas.assignment import AssignmentCreate
from ..models.db_factory import get_db

router = APIRouter(prefix="/auth/v1/assignments", tags=["Assignments"])

@router.post("", response_model=dict)
def create_assignment(data: AssignmentCreate, db: Session = Depends(get_db)):
    service = AssignmentService(db)
    assignment = service.create_assignment(data)
    return {"id": assignment.id, "resource_id": assignment.resource_id}

@router.get("", response_model=list[dict])
def list_assignments(db: Session = Depends(get_db)):
    service = AssignmentService(db)
    assignments = service.get_assignments()
    return [{"id": a.id, "resource_id": a.resource_id} for a in assignments]

@router.put("/{assignment_id}", response_model=dict)
def update_assignment(assignment_id: int, data: AssignmentCreate, db: Session = Depends(get_db)):
    service = AssignmentService(db)
    assignment = service.update_assignment(assignment_id, data)
    if not assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")
    return {"id": assignment.id, "resource_id": assignment.resource_id}

@router.delete("/{assignment_id}")
def delete_assignment(assignment_id: int, db: Session = Depends(get_db)):
    service = AssignmentService(db)
    success = service.delete_assignment(assignment_id)
    if not success:
        raise HTTPException(status_code=404, detail="Assignment not found")
    return {"detail": "Assignment deleted successfully"}
