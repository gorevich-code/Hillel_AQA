from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine("postgresql://postgres:postgres@localhost:5432/HillelDB")
auto_commit = engine.execution_options(isolation_level="AUTOCOMMIT")
session: Session = sessionmaker(auto_commit)()
