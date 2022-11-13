import uuid

import flask
from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from werkzeug.utils import redirect
from courseinterest import CourseInterest
from coursecatalog import CourseCatalogClass
from allprofessors import AllProfessorsClass

from coursereviews import CourseReviewsClass
from professorreviews import ProfessorReviewsClass

from flask import jsonify
from os import environ

from models import ProfessorReviews, CourseReviews, CourseInterestModel

DEFAULT_ROUTE_LEADERBOARD = "index"
DEFAULT_ROUTE_PLAYER = "player"

app = Flask(__name__)
Bootstrap(app)

conn_string = environ.get("DB_URI")

courseinterestobj = CourseInterest(conn_string)
coursecatalogobj = CourseCatalogClass(conn_string)
allprofessorsobj = AllProfessorsClass(conn_string)

coursereviewsobj = CourseReviewsClass(conn_string)
professorreviewsobj = ProfessorReviewsClass(conn_string)


@app.route("/")
def index():
    # scores = leaderboard.get_scores()
    # return render_template("index.html",
    #                        scores=scores)
    return render_template("index.html")

@app.route("/department")
def department():
    # scores = leaderboard.get_scores()
    # return render_template("index.html",
    #                        scores=scores)
    return render_template("DeptPage.html")

# @app.route("/player", methods=["GET", "POST"])
# def player():
#     if flask.request.method == "POST":
#         id = flask.request.values.get("id")
#         avatar = flask.request.values.get("avatar")
#         playername = flask.request.values.get("playername")
#         points = flask.request.values.get("points")
#         leaderboard.add_score(
#             Score(id=id, avatar=avatar, playername=playername, points=points)
#         )
#
#         return redirect(url_for(DEFAULT_ROUTE_LEADERBOARD))
#     else:
#         avatars = leaderboard.get_avatar_dic()
#         score = Score(avatar="0", playername="", points=0)
#         return render_template("player.html", score=score, avatars=avatars)


@app.route("/courseinterest", methods=['POST'])
def gcourseinterest():
    coursename = flask.request.values.get("coursename")
    phone = flask.request.values.get("phone")
    courseinterestobj.add_user_interest(
        CourseInterestModel(id=str(
            uuid.uuid4()), coursename=coursename, phone=phone))

    #TODO POP Up saying thank's for registering interest
    return render_template("index.html")


@app.route("/coursecatalog", methods=['GET'])
def gcoursecatalog():
    return coursecatalogobj.get_all_courses()

@app.route("/courseinfo", methods=['GET'])
def gcoursereview():
    coursename = flask.request.args.get('coursename')
    return coursereviewsobj.get_course_info(coursename)

@app.route("/allprofessors", methods=['GET'])
def gallprofessors():
    return allprofessorsobj.get_all_professors()


@app.route("/postcoursereviews", methods=['POST'])
def gpostcoursereviews():
    coursename = flask.request.values.get("coursename")
    professor = flask.request.values.get("professor")
    semester = flask.request.values.get("semester")
    courseload = flask.request.values.get("courseload")
    reviews = flask.request.values.get("reviews")
    industryroles = flask.request.values.get("industryroles")
    prereqs = flask.request.values.get("prereqs")
    difficulty = flask.request.values.get("difficulty")

    print(coursename, professor, semester, courseload, reviews, industryroles, prereqs, difficulty)

    coursereviewsobj.add_course_review(
        CourseReviews(
            coursename=coursename, 
            professor=professor, 
            semester=semester,
            courseload=courseload,
            reviews=reviews,
            industryroles=industryroles,
            prereqs=prereqs,
            difficulty=difficulty,
        )
    )
    return jsonify(success=True)


@app.route("/postprofreviews", methods=['POST'])
def gpostprofreviews():
    profname = flask.request.values.get("profname")
    classtaken = flask.request.values.get("classtaken")
    semester = flask.request.values.get("semester")
    rating = flask.request.values.get("rating")
    reviews = flask.request.values.get("reviews")

    print(profname, classtaken, semester, rating, reviews)

    professorreviewsobj.add_professor_review(
        ProfessorReviews(
            profname=profname, 
            classtaken=classtaken, 
            semester=semester,
            rating=rating,
            reviews=reviews,
        )
    )
    return jsonify(success=True)
