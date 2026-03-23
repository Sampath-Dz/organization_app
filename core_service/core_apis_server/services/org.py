from core_service.core_apis_server.services.base import BaseService
from core_service.core_apis_server.models.models import Organization
from core_service.core_apis_server.schemas.org import OrganizationCreate, OrganizationUpdate
from core_service.core_apis_server.exceptions import NotFoundException, AlreadyExistsException


class OrganizationService(BaseService):

    def create_organization(self, data: OrganizationCreate):
        existing = self.db.query(Organization).filter(
            Organization.name == data.name
        ).first()

        if existing:
            raise AlreadyExistsException("Organization already exists")

        org = Organization(
            name=data.name.strip()
        )

        return self.create(org)

    def get_organizations(self):
        return self.db.query(Organization).all()

    def get_organization(self, org_id: int):
        org = self.db.query(Organization).filter(
            Organization.id == org_id
        ).first()

        if not org:
            raise NotFoundException("Organization not found")

        return org

    def update_organization(self, org_id: int, data: OrganizationUpdate):
        org = self.get_organization(org_id)

        if data.name is not None:
            existing = self.db.query(Organization).filter(
                Organization.name == data.name
            ).first()

            if existing and existing.id != org_id:
                raise AlreadyExistsException("Organization name already exists")

            org.name = data.name.strip()

        return self.update(org)

    def patch_organization(self, org_id: int, data: OrganizationUpdate):
        return self.update_organization(org_id, data)

    def delete_organization(self, org_id: int):
        org = self.get_organization(org_id)
        self.delete(org)
        return True
