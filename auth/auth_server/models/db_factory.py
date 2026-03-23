from auth.auth_server.models.db_postgre import postgres_db

def get_db():
    db = postgres_db.get_session()
    try:
        yield db
    finally:
        db.remove()