from my_app import app, db
from my_app.models import StudentAnswers
from flask import render_template, redirect, url_for, jsonify
import json
from sqlalchemy.sql import func


@app.route("/")
def course_view():
    """
    Queries StudentAnswers table (using student_id)
    Makes [...]
    """

    # This value would come from Logged In user.
    student_id = 1

    list_of_student_answers = StudentAnswers.query.filter_by(
        student_id=student_id
    ).all()

    total_marks = sum([answer.marks for answer in list_of_student_answers])

    correct_marks = sum(
        [answer.marks for answer in list_of_student_answers if answer.correct_answer]
    )

    headline_marks = (correct_marks, total_marks)

    list_of_all_modules_in_course = list(
        set([answer.module_id for answer in list_of_student_answers])
    )

    dictionary_of_marks = {}
    for module in list_of_all_modules_in_course:
        correct_marks = sum(
            [
                answer.marks
                for answer in list_of_student_answers
                if answer.correct_answer and answer.module_id == module
            ]
        )
        total_marks = sum(
            [
                answer.marks
                for answer in list_of_student_answers
                if answer.module_id == module
            ]
        )

        dictionary_of_marks[module] = (correct_marks, total_marks)

    return render_template(
        "course_view.html",
        headline_marks=headline_marks,
        dictionary_of_marks=dictionary_of_marks,
    )


@app.route("/module/<int:module_id>")
def module_view(module_id):
    """
    Queries StudentAnswers table (using student_id)
    Makes [...]
    """

    # This value would come from Logged In user.
    student_id = 1

    list_of_student_answers = (
        StudentAnswers.query.filter_by(student_id=student_id)
        .filter_by(module_id=module_id)
        .all()
    )

    total_marks = sum([answer.marks for answer in list_of_student_answers])

    correct_marks = sum(
        [answer.marks for answer in list_of_student_answers if answer.correct_answer]
    )

    headline_marks = (correct_marks, total_marks)

    list_of_all_assessment_in_course = list(
        set([answer.assessment_id for answer in list_of_student_answers])
    )

    dictionary_of_marks = {}
    for assessment in list_of_all_assessment_in_course:
        correct_marks = sum(
            [
                answer.marks
                for answer in list_of_student_answers
                if answer.correct_answer and answer.assessment_id == assessment
            ]
        )
        total_marks = sum(
            [
                answer.marks
                for answer in list_of_student_answers
                if answer.assessment_id == assessment
            ]
        )

        dictionary_of_marks[assessment] = (correct_marks, total_marks)

    return render_template(
        "module_view.html",
        module_id=module_id,
        headline_marks=headline_marks,
        dictionary_of_marks=dictionary_of_marks,
    )


@app.route("/module/<int:module_id>/assessment/<int:assessment_id>")
def assessment_view(module_id, assessment_id):
    # This value would come from Logged In user.
    student_id = 1

    list_of_student_answers = (
        StudentAnswers.query.filter_by(student_id=student_id)
        .filter_by(module_id=module_id)
        .filter_by(assessment_id=assessment_id)
        .all()
    )

    total_marks = sum([answer.marks for answer in list_of_student_answers])

    correct_marks = sum(
        [answer.marks for answer in list_of_student_answers if answer.correct_answer]
    )

    headline_marks = (correct_marks, total_marks)

    list_of_all_assessment_in_course = list(
        set([answer.question_id for answer in list_of_student_answers])
    )

    dictionary_of_marks = {}
    for question in list_of_all_assessment_in_course:
        correct_marks = sum(
            [
                answer.marks
                for answer in list_of_student_answers
                if answer.correct_answer and answer.question_id == question
            ]
        )
        total_marks = sum(
            [
                answer.marks
                for answer in list_of_student_answers
                if answer.question_id == question
            ]
        )

        dictionary_of_marks[question] = (correct_marks, total_marks)

    return render_template(
        "assessment_view.html",
        module_id=module_id,
        assessment_id=assessment_id,
        headline_marks=headline_marks,
        dictionary_of_marks=dictionary_of_marks,
    )
