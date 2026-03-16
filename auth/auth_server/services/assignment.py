from .base import BaseService
from ..models.models import Assignment

class AssignmentService(BaseService):
    def create_assignment(self, data):
        assignment = Assignment(
            resource_id=data.resource_id,
            role_id=data.role_id,
            type_id=data.type_id,
            user_id=data.user_id
        )
        return self.create(assignment)

    def get_assignments(self):
        return self.db.query(Assignment).all()
