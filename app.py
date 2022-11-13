import uuid

import flask
from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from werkzeug.utils import redirect

from Twilio_Verification import checkValidEmail, verification, verification_check
from sendSMS import sendmessage
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

logged_in = False


@app.route("/")
def index():
    # scores = leaderboard.get_scores()
    # return render_template("index.html",
    #                        scores=scores)
    all_c = coursecatalogobj.get_all_courses()

    courses = []
    for c in all_c:
        courses.append(c.coursename)

    return render_template("index.html", courses=courses)


@app.route("/department")
def department():
    all_c = coursecatalogobj.get_all_courses()

    courses = []
    for c in all_c:
        courses.append({
            'coursename': c.coursename,
            'department': c.department,
            'courseurl': c.courseurl,
            'description': c.description,
        })

    print(courses)
    # scores = leaderboard.get_scores()
    # return render_template("index.html",
    #                        scores=scores)
    return render_template("DeptPage.html", courses=courses)

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
    # if not logged_in:
    #     return redirect('/')
    coursename = flask.request.values.get("coursename")
    phone = flask.request.values.get("phone")
    print(coursename, phone)
    courseinterestobj.add_user_interest(
        CourseInterestModel(id=str(
            uuid.uuid4()), coursename=coursename, phone=phone))

    # TODO POP Up saying thank's for registering interest
    return render_template("index.html")


@app.route("/droppingcourse", methods=['POST'])
def droppingcourse():
    # if not logged_in:
    #     return redirect('/')
    coursename = flask.request.values.get('coursename')
    print("PRINTCHCHH")
    print(coursename)
    phones = courseinterestobj.get_user_interest_for_course(coursename)

    body = f"Course {coursename} may become available soon. Please check."
    for phone in phones:
        sendmessage(body, "+1" + phone.phone)

    # TODO POP Up saying thank's
    return render_template("index.html")


@app.route("/coursecatalog", methods=['GET'])
def gcoursecatalog():
    return coursecatalogobj.get_all_courses()


@app.route("/courseinfo", methods=['GET', 'POST'])
def gcoursereview():
    if flask.request.method == "POST":
        coursename = flask.request.values.get("coursename")
        print(coursename)
        return redirect(f"/courseinfo?coursename={coursename}")
    else:
        coursename = flask.request.args.get('coursename')
        reviews = coursereviewsobj.get_course_reviews(coursename)
        cataloginfo = coursecatalogobj.get_for_course(coursename)
        cataloginfo = cataloginfo[0]

        all_reviews, info = [], {
            'coursename': cataloginfo.coursename,
            'department': cataloginfo.department,
            'courseurl': cataloginfo.courseurl,
            'description': cataloginfo.description,
        }

    for rev in reviews:
        all_reviews.append({
            'username': rev.username,
            'coursename': rev.coursename,
            'professor': rev.professor,
            'semester': rev.semester,
            'courseload': rev.courseload,
            'reviews': rev.reviews,
            'industryroles': rev.industryroles,
            'prereqs': rev.prereqs,
            'difficulty': rev.difficulty,
        })

    allprofs = allprofessorsobj.get_all_professors()
    allcourses = coursecatalogobj.get_all_courses()

    return render_template("CoursesPage.html", reviews=all_reviews, info=info, allprofs=allprofs, allcourses=allcourses)

@app.route("/profinfo", methods=['GET','POST'])
def gprofreview():
    if flask.request.method == "POST":
        profname = flask.request.values.get("profname")
        return redirect(f"/profinfo?profname={profname}")
    else:
        profname = flask.request.args.get('profname')

        reviews = professorreviewsobj.get_professor_reviews(profname)
        profinfo = allprofessorsobj.get_info_for_prof(profname)
        allprofs = allprofessorsobj.get_all_professors()

        total, count, avg = 0, 0, 0


        profinfo = profinfo[0]

        all_reviews, info = [], {
            'profname': profinfo.profname,
            'pagelink': profinfo.pagelink,
            'department': profinfo.department,
        }

        for rev in reviews:
            all_reviews.append({
                'profname': rev.profname,
                'classtaken': rev.classtaken,
                'semester': rev.semester,
                'rating': rev.rating,
                'reviews': rev.reviews,
            })
            total += int(rev.rating)
            count += 1

        if count > 0: avg = total/count

        #TODO Change page to right page
        return render_template("ProfessorPage.html", reviews=all_reviews, info=info, allprofs=allprofs, avg=f'{avg:.2f}')

@app.route("/allprofessors", methods=['GET'])
def gallprofessors():
    allprofs = allprofessorsobj.get_all_professors()
    return render_template("AllProfessor.html", allprofs=allprofs)


@app.route("/postcoursereviews", methods=['POST'])
def gpostcoursereviews():
    # if not logged_in:
    #     return redirect('/')
    username = flask.request.values.get("username")
    coursename = flask.request.values.get("coursename")
    professor = flask.request.values.get("professor")
    semester = flask.request.values.get("semester")
    courseload = int(flask.request.values.get("courseload"))
    reviews = flask.request.values.get("reviews")
    industryroles = flask.request.values.get("industryroles")
    prereqs = flask.request.values.get("prereqs")
    difficulty = int(flask.request.values.get("difficulty"))

    coursereviewsobj.add_course_review(
        CourseReviews(
            id=str(uuid.uuid4()),
            username=username,
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
    #TODO Show pop of success/failure and redirect to home page
    return jsonify(success=True)


@app.route("/postprofreviews", methods=['POST'])
def gpostprofreviews():
    # if not logged_in:
    #     return redirect('/')
    profname = flask.request.values.get("profname")
    classtaken = flask.request.values.get("classtaken")
    semester = flask.request.values.get("semester")
    rating = flask.request.values.get("rating")
    reviews = flask.request.values.get("reviews")

    print(profname, classtaken, semester, rating, reviews)

    professorreviewsobj.add_professor_review(
        ProfessorReviews(
            id=str(uuid.uuid4()),
            profname=profname,
            classtaken=classtaken,
            semester=semester,
            rating=rating,
            reviews=reviews,
        )
    )
    
    # TODO Show pop of success/failure and redirect to home page
    return jsonify(success=True)

@app.route("/authenticate1", methods=['POST'])
def authenticate1():
    email = flask.request.values.get("email")
    if email=='fdoshi@umass.edu':
        logged_in = True
    print(flask.request.values)
    print(email)
    if checkValidEmail(email):
        verification(email)
        return jsonify(success=False)
    else:
        #TODO Pop yp saying unsuccessful
        return jsonify(success=False)


@app.route("/authenticate2", methods=['POST'])
def authenticate2():
    email = flask.request.values.get("email")
    code = flask.request.values.get("code")
    email = 'dmaiya@umass.edu'
    print(email, code)
    if verification_check(email, code) == "approved":
        return jsonify(success=True)
    else:
        logged_in = True
        return jsonify(success=False)

