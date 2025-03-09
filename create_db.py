import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

# connection
print(os.getenv("POSTGRESQL_DBNAME"))
conn = psycopg2.connect(dbname = os.getenv("    POSTGRESQL_DBNAME"), user = os.getenv("POSTGRESQL_USER"), password = os.getenv("POSTGRESQL_PASSWORD"), host = os.getenv("POSTGRESQL_HOST"), port = os.getenv("POSTGRESQL_PORT"))

# cursor
with conn.cursor() as cur:
    # create tables
    
