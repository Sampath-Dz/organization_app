from core_service.core_apis_server.services.base import BaseService
from core_service.core_apis_server.models.models import Member, Team, Organization
from core_service.core_apis_server.schemas.member import MemberCreate, MemberUpdate
from core_service.core_apis_server.exceptions import NotFoundException


class MemberService(BaseService):

    def create_member(self, data: MemberCreate):
        team = self.db.query(Team).filter(
            Team.id == data.team_id
        ).first()

        if not team:
            raise NotFoundException("Team not found")

        member = Member(
            auth_user_id=data.auth_user_id,
            team_id=data.team_id
        )

        org = self.db.query(Organization).filter(
            Organization.id == team.organization_id
        ).first()

        if org:
            org.members_count += 1

        return self.create(member)

    def get_members(self):
        return self.db.query(Member).all()

    def get_member(self, member_id: int):
        member = self.db.query(Member).filter(
            Member.id == member_id
        ).first()

        if not member:
            raise NotFoundException("Member not found")

        return member

    def update_member(self, member_id: int, data: MemberUpdate):
        member = self.get_member(member_id)

        if data.team_id is not None:
            team = self.db.query(Team).filter(
                Team.id == data.team_id
            ).first()

            if not team:
                raise NotFoundException("Team not found")

            member.team_id = data.team_id

        if data.auth_user_id is not None:
            member.auth_user_id = data.auth_user_id

        return self.update(member)

    def patch_member(self, member_id: int, data: MemberUpdate):
        return self.update_member(member_id, data)

    def delete_member(self, member_id: int):
        member = self.get_member(member_id)

        team = self.db.query(Team).filter(
            Team.id == member.team_id
        ).first()

        if team:
            org = self.db.query(Organization).filter(
                Organization.id == team.organization_id
            ).first()

            if org and org.members_count > 0:
                org.members_count -= 1

        self.delete(member)
        return True
