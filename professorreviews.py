from cockroachdb.sqlalchemy import run_transaction
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from transactions import add_user_interest_txn, get_user_interest_txn, get_prof_reviews_txn


class ProfessorReviewsClass:
    def __init__(self, conn_string):
        self.engine = create_engine(conn_string, convert_unicode=True)
        self.sessionmaker = sessionmaker(bind=self.engine)

    def add_professor_review(self, profreview):
        return run_transaction(self.sessionmaker,
                               lambda session: session.add(profreview))

    def get_professor_reviews(self, prof):
        return run_transaction(self.sessionmaker,
                               lambda session: get_prof_reviews_txn(session, prof))
