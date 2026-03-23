from core_service.core_apis_server.services.base import BaseService
from core_service.core_apis_server.models.models import Team, Organization
from core_service.core_apis_server.schemas.team import TeamCreate, TeamUpdate
from core_service.core_apis_server.exceptions import NotFoundException


class TeamService(BaseService):

    def create_team(self, data: TeamCreate):
        org = self.db.query(Organization).filter(
            Organization.id == data.organization_id
        ).first()

        if not org:
            raise NotFoundException("Organization not found")

        team = Team(
            name=data.name.strip(),
            organization_id=data.organization_id,
            parent_id=data.parent_id
        )

        org.teams_count += 1

        return self.create(team)

    def get_teams(self):
        return self.db.query(Team).all()

    def get_team(self, team_id: int):
        team = self.db.query(Team).filter(
            Team.id == team_id
        ).first()

        if not team:
            raise NotFoundException("Team not found")

        return team

    def update_team(self, team_id: int, data: TeamUpdate):
        team = self.get_team(team_id)

        if data.name is not None:
            team.name = data.name.strip()

        if data.organization_id is not None:
            org = self.db.query(Organization).filter(
                Organization.id == data.organization_id
            ).first()

            if not org:
                raise NotFoundException("Organization not found")

            team.organization_id = data.organization_id

        if data.parent_id is not None:
            team.parent_id = data.parent_id

        return self.update(team)

    def patch_team(self, team_id: int, data: TeamUpdate):
        return self.update_team(team_id, data)

    def delete_team(self, team_id: int):
        team = self.get_team(team_id)

        org = self.db.query(Organization).filter(
            Organization.id == team.organization_id
        ).first()

        if org and org.teams_count > 0:
            org.teams_count -= 1

        self.delete(team)
        return True
