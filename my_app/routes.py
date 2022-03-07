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
def root():
    list_of_student_answers = StudentAnswers.query.all()
    average_mark = average_mark_calc(list_of_student_answers)

    return render_template(
        "index.html",
        list_of_student_answers=list_of_student_answers,
        average_mark=average_mark,
    )


# Filter: student_id
@app.route("/student/<int:student_id>")
def student_filter(student_id):
    list_of_student_answers = StudentAnswers.query.filter_by(
        student_id=student_id
    ).all()

    average_mark = average_mark_calc(list_of_student_answers)
    return render_template(
        "index.html",
        list_of_student_answers=list_of_student_answers,
        average_mark=average_mark,
    )


# Filter: module_id
@app.route("/module/<int:module_id>")
def module_filter(module_id):
    list_of_student_answers = StudentAnswers.query.filter_by(module_id=module_id).all()
    average_mark = average_mark_calc(list_of_student_answers)
    return render_template(
        "index.html",
        list_of_student_answers=list_of_student_answers,
        average_mark=average_mark,
    )


# Filter: question_id
@app.route("/question/<int:question_id>")
def question_filter(question_id):
    list_of_student_answers = StudentAnswers.query.filter_by(
        question_id=question_id
    ).all()
    average_mark = average_mark_calc(list_of_student_answers)
    return render_template(
        "index.html",
        list_of_student_answers=list_of_student_answers,
        average_mark=average_mark,
    )
