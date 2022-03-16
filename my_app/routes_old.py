from my_app import app, db
from my_app.models import StudentAnswers
from flask import render_template, redirect, url_for, jsonify
import json
from sqlalchemy.sql import func

"""
REQUIREMENTS
So what does this actual need?
- This will PRIMARILY be for ONE student's details.
-- notable exception is for introduction of class ranking

- Student ID should come from LOGGED IN USER
-- While in dev can have a default "user_id==1"

FEATURES REQUIRED
- Course results view [ list view ]
-- Shows all modules so far
-- Shows predicted grade

- Module results view [ list view ]
-- Shows questions and gives breakdown of average/total score so far
-- Should be able to click on an Assessment to go to an Assessment view

- Assessment results view [ list view ]
-- Shows questions and gives breakdown of average/total score so far
-- Should be able to click on a Question to get a Question view


- Question view [ detail view ]
-- Unsure on what this would show but worth considering.

DETAILS REQUIRED
- Assessment results view [ list view ]
-- Calculated fields:

--# PRIMARY
--- Marks achieved
--- Marks possible

--# SECONDARY
--- Answers submitted
--- Answers possible
---- If questions have categories then could have a category breakdown

----- FUNCTIONALITY: 
must be able to export all data as .csv

"""

##############################################################
# OLD
##############################################################


# For more complicated things we should use numpy/pandas.


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
# >> Can you send a querySet to a route? POST method maybe??
# @app.route("/")
# def root():

#     list_of_student_answers = StudentAnswers.query.all()
#     average_mark = average_mark_calc(list_of_student_answers)

#     return render_template(
#         "index.html",
#         list_of_student_answers=list_of_student_answers,
#         average_mark=average_mark,
#     )


class AssessmentSummary:
    def __init__(self, assessment_id):
        self.assessment_id = assessment_id
        self.count_correct_answer = None
        self.count_incorrect_answer = None
        self.marks_awarded = None
        self.marks_possible = None

    def __repr__(self):
        return f"Assessment Summary: {self.assessment_id}"


# Filter: student_id
@app.route("/old/student/<int:student_id>")
def student_filter(student_id):

    # Dictionary of question and average score
    dictionary_of_question_and_average_score = {}

    # Get all the student's answers
    # # May need to check this against the actual assessment table as student may not have answered all
    list_of_student_answers = StudentAnswers.query.filter_by(
        student_id=student_id
    ).all()

    # Get list of assessment
    list_of_assessments = list(
        set([answer.assessment_id for answer in list_of_student_answers])
    )

    # Go through the assessments and gather the data:
    # globals()
    # https://www.delftstack.com/howto/python/python-dynamic-variable-name/

    # THIS IS SO IMMENSELY OVERCOMPLICATED.

    list_of_class_objects = []
    # Make a class...
    for assessment in list_of_assessments:
        globals()[f"assessment_{assessment}"] = AssessmentSummary(assessment)
        list_of_class_objects.append(globals()[f"assessment_{assessment}"])

    print(f"list_of_assessment: {list_of_assessments} ")
    # We want:
    # > a list of classes with attributes
    # > for each question:
    # > > number of correct answers
    # > > number of incorrect answers
    # > > number of marks awarded
    # > > number of marks possible

    print(list_of_student_answers)

    for item in list_of_student_answers:
        print(type(item))

    # Gives the marks, NOT THE QUESTIONS - separate list of questions?
    av_query = (
        db.session.query(db.func.avg(StudentAnswers.marks))
        .filter_by(student_id=student_id)
        .filter_by(correct_answer=True)
        .group_by(StudentAnswers.question_id)
        .all()
    )

    print(av_query)

    av_query_id = (
        StudentAnswers.query.filter_by(student_id=student_id)
        .filter_by(correct_answer=True)
        .group_by(StudentAnswers.question_id)
        .all()
    )

    print(av_query_id)
    for question in av_query_id:
        print(question.question_id)

    average_mark = average_mark_calc(list_of_student_answers)
    return render_template(
        "index.html",
        list_of_student_answers=list_of_student_answers,
        average_mark=average_mark,
    )


# Filter: module_id
@app.route("/old/module/<int:module_id>")
def module_filter(module_id):
    list_of_student_answers = StudentAnswers.query.filter_by(module_id=module_id).all()
    average_mark = average_mark_calc(list_of_student_answers)
    return render_template(
        "index.html",
        list_of_student_answers=list_of_student_answers,
        average_mark=average_mark,
    )


# Filter: question_id
@app.route("/old/question/<int:question_id>")
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
