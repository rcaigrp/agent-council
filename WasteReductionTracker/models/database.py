from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

database_url = os.getenv('DATABASE_URL', 'sqlite:///waste_tracker.db')
engine = create_engine(database_url)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    # Import all models here so they get registered with Base
    from .waste_item import WasteItem
    from .sustainability_goal import SustainabilityGoal
    Base.metadata.create_all(bind=engine)
