import psycopg2
from pathlib import Path
from dotenv import load_dotenv
import os
import pandas as pd
from sqlalchemy import create_engine

path_db = Path(__file__).resolve().parent.parent / "env" / ".env"


load_dotenv(path_db)


user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
localhost = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
name = os.getenv("DB_NAME")


engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{localhost}:{port}/{name}")


def create_table(df,table_name):

    df.to_sql(
      table_name,
      engine,
      if_exists = "replace",
      index = False
    )

    print('-- Tabela inserida com sucesso ')
    
