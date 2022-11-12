from models import Score, CourseInterest
import uuid


def get_scores_txn(session):
    query = session.query(Score)
    return query.all()

def get_user_interest_txn(session, coursename):
    query = session\
        .query(CourseInterest)\
        .filter(CourseInterest.coursename == coursename)\
        .with_entities(CourseInterest.phone)
    return query

def add_score_txn(session, avatar, playername, points):
    score = Score(
        id=str(
            uuid.uuid4()),
        avatar=avatar,
        playername=playername,
        points=points
    )
    session.add(score)


def add_user_interest_txn(session, courseinterest):
    session.add(courseinterest)
