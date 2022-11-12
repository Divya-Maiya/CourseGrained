from cockroachdb.sqlalchemy import run_transaction
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from transactions import add_user_interest_txn, get_user_interest_txn


class CourseInterest:
    def __init__(self, conn_string):
        self.engine = create_engine(conn_string, convert_unicode=True)
        self.sessionmaker = sessionmaker(bind=self.engine)

    def add_user_interest(self, courseinterest):
        return run_transaction(self.sessionmaker,
                               lambda session: add_user_interest_txn(session, courseinterest))

    def get_user_interest_for_course(self, course):
        return run_transaction(self.sessionmaker,
                               lambda session: self.get_user_interest(session, course))

    def get_user_interest(self, session, course):
        return get_user_interest_txn(session, course)
