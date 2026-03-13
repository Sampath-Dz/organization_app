from pydantic import BaseModel


class TeamCreate(BaseModel):

    name:str
    organization_id:int
