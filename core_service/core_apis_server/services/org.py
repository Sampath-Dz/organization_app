from sqlalchemy.orm import Session
from ..models.models import Organization
from ..crud.generic import create_item, get_all_items, get_item, update_item, delete_item

class OrganizationService:
    def __init__(self, db: Session):
        self.db = db

    def create_organization(self, data: dict):
        return create_item(self.db, Organization, data)

    def get_organizations(self):
        return get_all_items(self.db, Organization)

    def get_organization(self, org_id: int):
        return get_item(self.db, Organization, org_id)

    def update_organization(self, org_id: int, data: dict):
        org = self.get_organization(org_id)
        if not org:
            return None
        for key, value in data.items():
            setattr(org, key, value)
        update_item(self.db)
        return org

    def delete_organization(self, org_id: int):
        org = self.get_organization(org_id)
        if not org:
            return False
        delete_item(self.db, org)
        return True
