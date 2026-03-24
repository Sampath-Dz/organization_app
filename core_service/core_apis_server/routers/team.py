from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from core_service.core_apis_server.schemas.team import (
    TeamCreate,
    TeamUpdate,
    TeamResponse,
    TeamListResponse
)
from core_service.core_apis_server.services.team import TeamService
from core_service.core_apis_server.models.db_factory import DBFactory

router = APIRouter(prefix="/core/v1/teams", tags=["Teams"])

def get_service(db: Session = Depends(DBFactory().get_db)):
    return TeamService(db)

@router.post("", response_model=TeamResponse, status_code=status.HTTP_201_CREATED)
def create_team(data: TeamCreate, service: TeamService = Depends(get_service)):
    return service.create_team(data)

@router.get("", response_model=List[TeamResponse])
def list_teams(service: TeamService = Depends(get_service)):
    return service.get_teams()

@router.get("/{team_id}", response_model=TeamResponse)
def get_team(team_id: str, service: TeamService = Depends(get_service)):
    return service.get_team(team_id)

@router.put("/{team_id}", response_model=TeamResponse)
def update_team(team_id: str, data: TeamUpdate, service: TeamService = Depends(get_service)):
    return service.update_team(team_id, data)

@router.patch("/{team_id}", response_model=TeamResponse)
def patch_team(team_id: str, data: TeamUpdate, service: TeamService = Depends(get_service)):
    return service.patch_team(team_id, data)

@router.delete("/{team_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_team(team_id: str, service: TeamService = Depends(get_service)):
    service.delete_team(team_id)
    return {"detail": "Team deleted"}