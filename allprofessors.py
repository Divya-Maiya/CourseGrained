from cockroachdb.sqlalchemy import run_transaction
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from transactions import get_prof_info_txn
from models import Professors


class AllProfessorsClass:
    def __init__(self, conn_string):
        self.engine = create_engine(conn_string, convert_unicode=True)
        self.sessionmaker = sessionmaker(bind=self.engine, expire_on_commit=False)

    def get_all_professors(self):
        return run_transaction(self.sessionmaker,
                               lambda session: session.query(Professors).all())


    def get_info_for_prof(self, profname):
        return run_transaction(self.sessionmaker,
                               lambda session: get_prof_info_txn(session, profname))