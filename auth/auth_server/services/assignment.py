
from auth.auth_server.services.base import BaseService
from auth.auth_server.models.models import Assignment
from auth.auth_server.schemas.assignment import AssignmentCreate


class AssignmentService(BaseService):

    def get_assignment_by_id(self, assignment_id: int):
        assignment = self.db.query(Assignment).filter(Assignment.id == assignment_id).first()
        if not assignment:
            raise Exception("Assignment not found")
        return assignment

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

    def update_assignment(self, assignment_id: int, data: AssignmentCreate):
        assignment = self.get_assignment_by_id(assignment_id)

        assignment.resource_id = data.resource_id
        assignment.role_id = data.role_id
        assignment.type_id = data.type_id
        assignment.user_id = data.user_id

        return self.update(assignment)

    def delete_assignment(self, assignment_id: int):
        assignment = self.get_assignment_by_id(assignment_id)
        self.delete(assignment)
        return True
