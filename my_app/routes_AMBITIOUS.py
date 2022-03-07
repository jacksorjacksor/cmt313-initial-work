from my_app import app
from my_app.models import StudentAnswers
from flask import render_template, redirect, url_for, jsonify
import json


def average_mark_calc(list_of_student_answers):
    if list_of_student_answers:
        return sum(
            [
                student.marks
                for student in list_of_student_answers
                if student.correct_answer
            ]
        ) / len(list_of_student_answers)
    else:
        return 0


# All entries
@app.route("/")
def root(list_of_student_answers):
    average_mark = average_mark_calc(list_of_student_answers)

    return render_template(
        "index.html",
        list_of_student_answers=list_of_student_answers,
        average_mark=average_mark,
    )


# All entries
@app.route("/all/")
def all_entries():
    list_of_student_answers = StudentAnswers.query.all()

    # json_version = jsonify({"data": [l.serialized for l in list_of_student_answers]})
    # return redirect(url_for("root", list_of_student_answers=json_version))


# # Filter: student_id
# @app.route("/student/<int:student_id>")
# def student_filter(student_id):
#     query = StudentAnswers.query.filter_by(student_id=student_id).all()
#     return redirect(url_for("query_root", list_of_student_answers=query))


# # Filter: module_id
# @app.route("/module/<int:module_id>")
# def module_filter(module_id):
#     query = StudentAnswers.query.filter_by(module_id=module_id).all()
#     return redirect(url_for("query_root", list_of_student_answers=query))


# # Filter: question_id
# @app.route("/question/<int:question_id>")
# def question_filter(question):
#     query = StudentAnswers.query.filter_by(question_id=question_id).all()
#     return redirect(url_for("query_root", list_of_student_answers=query))
