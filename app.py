import flask
from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from werkzeug.utils import redirect
from leaderboard import Leaderboard
from courseinterest import CourseInterest
from coursecatalog import CourseCatalogClass
from allprofessors import AllProfessorsClass
from os import environ

from models import Score

DEFAULT_ROUTE_LEADERBOARD = "index"
DEFAULT_ROUTE_PLAYER = "player"

app = Flask(__name__)
Bootstrap(app)

conn_string = environ.get("DB_URI")
leaderboard = Leaderboard(conn_string)

courseinterestobj = CourseInterest(conn_string)
coursecatalogobj = CourseCatalogClass(conn_string)
allprofessorsobj = AllProfessorsClass(conn_string)


@app.route("/")
def index():
    # scores = leaderboard.get_scores()
    # return render_template("index.html",
    #                        scores=scores)
    return "Hi"

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


@app.route("/courseinterest")
def gcourseinterest():
    phones = courseinterestobj.get_user_interest_for_course("520")
    print(phones)


@app.route("/coursecatalog")
def gcoursecatalog():
    return coursecatalogobj.get_all_courses()


@app.route("/allprofessors")
def gallprofessors():
    return allprofessorsobj.get_all_professors()

# @app.route("/professors")
# def gcoursecatalog():
#     print(phones)

# @app.route("/profreviews", method=['POST'])
# def gprofreviews():
#     pass

# @app.route("/coursereviews", method=['POST'])
# def gcoursereviews():
#     pass
