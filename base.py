import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE = os.environ.get("POSGRESQL_DATABASE")
USER     = os.environ.get("POSGRESQL_USER")
PASSWORD = os.environ.get("POSGRESQL_PASSWORD")
URL      = os.environ.get("POSGRESQL_URL")
PORT     = os.environ.get("POSGRESQL_PORT")

engine = create_engine(f"postgresql://{USER}:{PASSWORD}@{URL}:{PORT}/{DATABASE}")
Session = sessionmaker(bind=engine)

Base = declarative_base()
