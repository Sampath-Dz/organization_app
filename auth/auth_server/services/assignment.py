from .base import BaseService
from ..models.models import Assignment
from ..schemas.assignment import AssignmentCreate

class AssignmentService(BaseService):

    def create_assignment(self, data: AssignmentCreate):
        assignment = Assignment(
            resource_id=data.resource_id,
            role_id=data.role_id,
            type_id=data.type_id,
            user_id=data.user_id
        )
        return self.create(assignment)

    def get_assignments(self):
        return self.db.query(Assignment).all()

    def get_assignment(self, assignment_id: int):
        return self.db.query(Assignment).filter(Assignment.id == assignment_id).first()

    def update_assignment(self, assignment_id: int, data: AssignmentCreate):
        assignment = self.get_assignment(assignment_id)
        if not assignment:
            return None
        assignment.resource_id = data.resource_id
        assignment.role_id = data.role_id
        assignment.type_id = data.type_id
        assignment.user_id = data.user_id
        self.update()
        return assignment

    def delete_assignment(self, assignment_id: int):
        assignment = self.get_assignment(assignment_id)
        if not assignment:
            return False
        self.delete(assignment)
        return True
