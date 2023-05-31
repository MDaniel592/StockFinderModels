import os
import socket

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

HOSTNAME = os.environ.get("HOSTNAME", False)
DATABASE = os.environ.get("POSGRESQL_DATABASE")

LOCAL_USER = os.environ.get("POSGRESQL_LOCAL_USER")
LOCAL_USER_PASSWORD = os.environ.get("POSGRESQL_LOCAL_USER_PASSWORD")
LOCAL_URL = os.environ.get("POSGRESQL_LOCAL_URL")
LOCAL_PORT = os.environ.get("POSGRESQL_LOCAL_PORT")

REMOTE_USER = os.environ.get("POSGRESQL_REMOTE_USER")
REMOTE_USER_PASSWORD = os.environ.get("POSGRESQL_REMOTE_USER_PASSWORD")
REMOTE_URL = os.environ.get("POSGRESQL_REMOTE_URL")
REMOTE_PORT = os.environ.get("POSGRESQL_REMOTE_PORT")


if HOSTNAME == "Docker":
    print("Localhost / Docker")
    # Localhost / Docker
    engine = create_engine(f"postgresql://{LOCAL_USER}:{LOCAL_USER_PASSWORD}@{LOCAL_URL}:{LOCAL_PORT}/{DATABASE}")
else:
    print("Remote Host")
    # Remote Host
    engine = create_engine(f"postgresql://{REMOTE_USER}:{REMOTE_USER_PASSWORD}@{REMOTE_URL}:{REMOTE_PORT}/{DATABASE}")

Session = sessionmaker(bind=engine)

Base = declarative_base()
