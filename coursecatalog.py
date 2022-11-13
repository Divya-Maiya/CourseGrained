from cockroachdb.sqlalchemy import run_transaction
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from transactions import get_course_info_txn
from models import CourseCatalog


class CourseCatalogClass:
    def __init__(self, conn_string):
        self.engine = create_engine(conn_string, convert_unicode=True)
        self.sessionmaker = sessionmaker(bind=self.engine, expire_on_commit=False)

    def get_all_courses(self):
        return run_transaction(self.sessionmaker,
                               lambda session: session.query(CourseCatalog).all())

    def get_for_course(self, course):
        return run_transaction(self.sessionmaker,
                               lambda session: get_course_info_txn(session, course))