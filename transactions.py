from models import Score, CourseInterestModel, CourseReviews, CourseCatalog, ProfessorReviews, Professors
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


def get_course_reviews_txn(session, coursename):
    query = session\
        .query(CourseReviews)\
        .filter(CourseReviews.coursename == coursename)
    return query.all()

def get_prof_reviews_txn(session, profname):
    query = session\
        .query(ProfessorReviews)\
        .filter(ProfessorReviews.profname == profname)
    return query.all()

def get_prof_info_txn(session, profname):
    query = session\
        .query(Professors)\
        .filter(Professors.profname == profname)
    return query.all()

# def get_course_review_and_info(session, course):
#     query = session.query(CourseReviews).\
#         join(CourseCatalog, coursename == CourseReviews.coursename).\
#         filter(CourseReviews.coursename == course)
#     return query.all()


def add_user_interest_txn(session, courseinterest):
    session.add(courseinterest)

def get_course_info_txn(session, coursename):
    query = session\
        .query(CourseCatalog)\
        .filter(CourseCatalog.coursename == coursename)
    return query.all()