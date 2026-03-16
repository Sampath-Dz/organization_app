from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core_apis_server.models.models import Team
from core_apis_server.models.db_factory import get_db
from core_apis_server.crud.generic import create_item, get_all_items, get_item, update_item, delete_item

router = APIRouter(prefix="/core/v1/teams", tags=["Teams"])

@router.post("")
def create_team(data: dict, db: Session = Depends(get_db)):
    return create_item(db, Team, data)

@router.get("")
def list_teams(db: Session = Depends(get_db)):
    return get_all_items(db, Team)

@router.get("/{team_id}")
def get_team(team_id: int, db: Session = Depends(get_db)):
    team = get_item(db, Team, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

@router.put("/{team_id}")
def update_team(team_id: int, data: dict, db: Session = Depends(get_db)):
    team = get_item(db, Team, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return update_item(db, team, data)

@router.patch("/{team_id}")
def patch_team(team_id: int, data: dict, db: Session = Depends(get_db)):
    team = get_item(db, Team, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return update_item(db, team, data)

@router.delete("/{team_id}")
def delete_team(team_id: int, db: Session = Depends(get_db)):
    team = get_item(db, Team, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    delete_item(db, team)
    return {"detail": "Deleted successfully"}
