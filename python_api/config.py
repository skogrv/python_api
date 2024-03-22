# import os


db="postgres"
port=5432
password="password"
user="postgres"
host="db"
DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}'
print(DATABASE_CONNECTION_URI)