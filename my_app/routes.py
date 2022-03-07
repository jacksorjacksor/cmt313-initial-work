from my_app import app
from my_app.models import StudentAnswers
from flask import render_template


@app.route("/")
def all_queries():
    list_of_student_answers = StudentAnswers.query.all()

    return render_template(
        "index.html", list_of_student_answers=list_of_student_answers
    )
