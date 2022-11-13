from models import Score, CourseInterestModel
import uuid


def get_scores_txn(session):
    query = session.query(Score)
    return query.all()

def get_user_interest_txn(session, coursename):
    query = session\
        .query(CourseInterestModel)\
        .filter(CourseInterestModel.coursename == coursename)\
        .with_entities(CourseInterestModel.phone)
    return query.all()

def add_user_interest_txn(session, courseinterest):
    session.add(courseinterest)
