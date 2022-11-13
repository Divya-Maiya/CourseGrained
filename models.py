from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import INT, VARCHAR, CHAR


Base = declarative_base()

class Score(Base):
    __tablename__ = 'scores'
    id = Column(UUID, primary_key=True)
    avatar = Column(INT)
    playername = Column(String)
    points = Column(INT)


class CourseInterestModel(Base):
    __tablename__ = 'courseinterest'
    id = Column(UUID, primary_key=True)
    coursename = Column(VARCHAR)
    emailid = Column(VARCHAR)
    phone = Column(CHAR)


class CourseCatalog(Base):
    __tablename__ = 'coursecatalog'
    coursename = Column(VARCHAR, primary_key=True)
    department = Column(VARCHAR)
    courseurl = Column(VARCHAR)
    description = Column(VARCHAR)


class Professors(Base):
    __tablename__ = 'professors'
    profname = Column(VARCHAR, primary_key=True)
    pagelink = Column(VARCHAR)
    department = Column(VARCHAR)


class CourseReviews(Base):
    __tablename__ = 'coursereviews'
    id = Column(UUID, primary_key=True)
    username = Column(VARCHAR)
    coursename = Column(VARCHAR)
    professor = Column(VARCHAR)
    semester = Column(VARCHAR)
    courseload = Column(INT)
    reviews = Column(VARCHAR)
    industryroles = Column(VARCHAR)
    prereqs = Column(VARCHAR)
    difficulty = Column(INT)


class ProfessorReviews(Base):
    __tablename__ = 'profreviews'
    id = Column(UUID, primary_key=True)
    profname = Column(VARCHAR)
    classtaken = Column(VARCHAR)
    semester = Column(VARCHAR)
    rating = Column(INT)
    reviews = Column(VARCHAR)

