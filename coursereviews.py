from cockroachdb.sqlalchemy import run_transaction
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from transactions import add_user_interest_txn, get_user_interest_txn, get_course_reviews_txn


class CourseReviewsClass:
    def __init__(self, conn_string):
        self.engine = create_engine(conn_string, convert_unicode=True)
        self.sessionmaker = sessionmaker(bind=self.engine, expire_on_commit=False)

    def add_course_review(self, coursereview):
        run_transaction(self.sessionmaker,
                               lambda session: session.add(coursereview))

    def get_course_reviews(self, course):
        return run_transaction(self.sessionmaker,
                               lambda session: get_course_reviews_txn(session, course))

    def get_course_info(self, course):
        return run_transaction(self.sessionmaker,
                               lambda session: get_course_review_and_info(session, course))