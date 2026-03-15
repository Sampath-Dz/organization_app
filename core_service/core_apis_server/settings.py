<<<<<<< HEAD
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=require"

CORE_PORT = int(os.getenv("CORE_PORT"))
=======
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_HOST=os.getenv("DATABASE_HOST")
DATABASE_PORT=os.getenv("DATABASE_PORT")
DATABASE_NAME=os.getenv("DATABASE_NAME")
DATABASE_USER=os.getenv("DATABASE_USER")
DATABASE_PASSWORD=os.getenv("DATABASE_PASSWORD")

DATABASE_URL=f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"


JWT_SECRET="supersecretkey"
JWT_ALGORITHM="HS256"

>>>>>>> 9073f23830fbf94017b86571b180ab41644f2c8b
