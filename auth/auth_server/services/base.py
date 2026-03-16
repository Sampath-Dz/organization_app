from sqlalchemy.orm import Session

class BaseService:
    def __init__(self, db: Session):
        self.db = db

    def create(self, obj):
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def update(self):
        self.db.commit()

    def delete(self, obj):
        self.db.delete(obj)
        self.db.commit()
