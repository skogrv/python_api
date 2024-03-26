import os


db = "postgres"
port = 5432
password = os.environ.get("POSTGRES_PASSWORD", "postgres")
user = "postgres"
host = "db"
DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}'
