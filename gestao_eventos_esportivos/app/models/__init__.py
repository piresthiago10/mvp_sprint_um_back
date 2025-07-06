from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

from app.models.base import Base

db_path = "database/"
if not os.path.exists(db_path):
    os.makedirs(db_path)

from app.models.endereco import Endereco
from app.models.trajeto import Trajeto
from app.models.evento import Evento

db_url = "sqlite:///%s/db.sqlite3" % db_path
engine = create_engine(db_url, echo=False)

if not database_exists(engine.url):
    create_database(engine.url)

Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

