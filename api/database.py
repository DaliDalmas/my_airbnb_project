from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from  . import connection_params as cp

# Create a database URL for SQLAlchemy
SQLALCHEMY_DATABASE_URL = f"postgresql://{cp.user}:{cp.password}@localhost/youtube"

# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a SessionLocal class
sessionLocal1 = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class
Base = declarative_base()