
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.auth_server.services.assignment import AssignmentService
from auth.auth_server.schemas.assignment import AssignmentCreate
from auth.auth_server.models.db_factory import get_db


router = APIRouter(prefix="/auth/v1/assignments", tags=["Assignments"])


def get_assignment_service(db: Session = Depends(get_db)):
    return AssignmentService(db)


@router.post("")
def create_assignment(
    data: AssignmentCreate,
    service: AssignmentService = Depends(get_assignment_service)
):
    assignment = service.create_assignment(data)
    return {"id": assignment.id, "resource_id": assignment.resource_id}


@router.get("")
def list_assignments(
    service: AssignmentService = Depends(get_assignment_service)
):
    assignments = service.get_assignments()
    return [{"id": a.id, "resource_id": a.resource_id} for a in assignments]


@router.put("/{assignment_id}")
def update_assignment(
    assignment_id: int,
    data: AssignmentCreate,
    service: AssignmentService = Depends(get_assignment_service)
):
    assignment = service.update_assignment(assignment_id, data)
    return {"id": assignment.id, "resource_id": assignment.resource_id}


@router.delete("/{assignment_id}")
def delete_assignment(
    assignment_id: int,
    service: AssignmentService = Depends(get_assignment_service)
):
    service.delete_assignment(assignment_id)
    return {"detail": "Assignment deleted successfully"}
