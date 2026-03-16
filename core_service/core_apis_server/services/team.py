from sqlalchemy.orm import Session
from ..models.models import Team
from ..crud.generic import create_item, get_all_items, get_item, update_item, delete_item

class TeamService:
    def __init__(self, db: Session):
        self.db = db

    def create_team(self, data: dict):
        return create_item(self.db, Team, data)

    def get_teams(self):
        return get_all_items(self.db, Team)

    def get_team(self, team_id: int):
        return get_item(self.db, Team, team_id)

    def update_team(self, team_id: int, data: dict):
        team = self.get_team(team_id)
        if not team:
            return None
        for key, value in data.items():
            setattr(team, key, value)
        update_item(self.db)
        return team

    def delete_team(self, team_id: int):
        team = self.get_team(team_id)
        if not team:
            return False
        delete_item(self.db, team)
        return True
