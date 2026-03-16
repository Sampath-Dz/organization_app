from sqlalchemy.orm import Session

def create_item(db: Session, model_class, obj_data: dict):
    db_obj = model_class(**obj_data)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_all_items(db: Session, model_class):
    return db.query(model_class).all()

def get_item(db: Session, model_class, item_id: int):
    return db.query(model_class).filter(model_class.id == item_id).first()

def update_item(db: Session, db_obj, update_data: dict):
    for key, value in update_data.items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_item(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()
    return True
