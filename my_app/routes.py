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


@app.route("/")
def course_view():
    # This value would come from Logged In user.
    student_id = 1

    list_of_student_answers = StudentAnswers.query.filter_by(
        student_id=student_id
    ).all()

    # Dictionary of dictionaries
    dictionary_of_modules_with_possible_marks = {}
    dictionary_of_modules_with_total_marks = {}

    list_of_all_modules_in_course = list(
        set([answer.module_id for answer in list_of_student_answers])
    )

    for module in list_of_all_modules_in_course:
        dictionary_of_possible_marks = {}
        dictionary_of_total_marks = {}

        list_of_all_assessments_in_module = list(
            set(
                [
                    answer.assessment_id
                    for answer in list_of_student_answers
                    if answer.module_id == module
                ]
            )
        )

        # Make dictionary{question ID: possible marks}
        for assessment in list_of_all_assessments_in_module:
            dictionary_of_possible_marks[assessment] = sum(
                [
                    answer.marks
                    for answer in list_of_student_answers
                    if answer.assessment_id == assessment
                ]
            )

        # Make dictionary{question ID: actual marks}
        for assessment in list_of_all_assessments_in_module:
            dictionary_of_total_marks[assessment] = sum(
                [
                    answer.marks
                    for answer in list_of_student_answers
                    if answer.assessment_id == assessment and answer.correct_answer
                ]
            )

        dictionary_of_modules_with_possible_marks.setdefault(module, []).append(
            dictionary_of_possible_marks
        )
        dictionary_of_modules_with_total_marks.setdefault(module, []).append(
            dictionary_of_total_marks
        )

    # Get rid of nested list (shouldn't have been there anyway)
    dictionary_of_modules_with_total_marks = {
        key: value[0] for key, value in dictionary_of_modules_with_total_marks.items()
    }

    dictionary_of_modules_with_possible_marks = {
        key: value[0]
        for key, value in dictionary_of_modules_with_possible_marks.items()
    }

    results_dict = {}
    for module_id, assessments in dictionary_of_modules_with_possible_marks.items():
        results_dict[module_id] = {}
        for assessment_id, possible_marks in assessments.items():
            total_marks = dictionary_of_modules_with_total_marks[module_id][
                assessment_id
            ]
            output_tuple = (total_marks, possible_marks)
            results_dict[module_id][assessment_id] = output_tuple

    total_marks = 0
    available_marks = 0
    module_totals = {}
    for module_id, assessments_dict in results_dict.items():
        for assessment, marks_tuple in assessments_dict.items():
            total_marks += marks_tuple[0]
            available_marks += marks_tuple[1]
        module_totals[module_id] = (total_marks, available_marks)

    course_total_marks = 0
    course_available_marks = 0

    for _, results_tuple in module_totals.items():
        course_total_marks += results_tuple[0]
        course_available_marks += results_tuple[1]

    final_results = (course_total_marks, course_available_marks)

    # For testing - sending a class object to Jinja2? God I'm tired...

    return render_template(
        "course_view.html",
        final_results=final_results,  # (total_marks, possible_marks),
        module_totals=module_totals,  # {module: (total_marks, possible_marks)}
        results_dict=results_dict,  # {module: {assessment: (total_marks, possible_marks)}}
    )


@app.route("/module/<int:module_id>")
def module_view(module_id):
    # This value would come from Logged In user.
    student_id = 1

    list_of_student_answers = (
        StudentAnswers.query.filter_by(student_id=student_id)
        .filter_by(module_id=module_id)
        .all()
    )

    dictionary_of_possible_marks = {}
    dictionary_of_total_marks = {}
    dictionary_of_modules_with_possible_marks = {}
    dictionary_of_modules_with_total_marks = {}

    list_of_all_assessments_in_module = list(
        set(
            [
                answer.assessment_id
                for answer in list_of_student_answers
                if answer.module_id == module_id
            ]
        )
    )

    # Make dictionary{question ID: possible marks}
    for assessment in list_of_all_assessments_in_module:
        dictionary_of_possible_marks[assessment] = sum(
            [
                answer.marks
                for answer in list_of_student_answers
                if answer.assessment_id == assessment
            ]
        )

    # Make dictionary{question ID: actual marks}
    for assessment in list_of_all_assessments_in_module:
        dictionary_of_total_marks[assessment] = sum(
            [
                answer.marks
                for answer in list_of_student_answers
                if answer.assessment_id == assessment and answer.correct_answer
            ]
        )

    dictionary_of_modules_with_possible_marks.setdefault(module_id, []).append(
        dictionary_of_possible_marks
    )

    dictionary_of_modules_with_total_marks.setdefault(module_id, []).append(
        dictionary_of_total_marks
    )

    # Get rid of nested list (shouldn't have been there anyway)
    dictionary_of_modules_with_total_marks = {
        key: value[0] for key, value in dictionary_of_modules_with_total_marks.items()
    }

    dictionary_of_modules_with_possible_marks = {
        key: value[0]
        for key, value in dictionary_of_modules_with_possible_marks.items()
    }

    results_dict = {}
    for module_id, assessments in dictionary_of_modules_with_possible_marks.items():
        results_dict[module_id] = {}
        for assessment_id, possible_marks in assessments.items():
            total_marks = dictionary_of_modules_with_total_marks[module_id][
                assessment_id
            ]
            output_tuple = (total_marks, possible_marks)
            results_dict[module_id][assessment_id] = output_tuple

    total_marks = 0
    available_marks = 0
    module_totals = {}
    for module_id, assessments_dict in results_dict.items():
        for assessment, marks_tuple in assessments_dict.items():
            total_marks += marks_tuple[0]
            available_marks += marks_tuple[1]
        module_totals[module_id] = (total_marks, available_marks)

    course_total_marks = 0
    course_available_marks = 0

    for _, results_tuple in module_totals.items():
        course_total_marks += results_tuple[0]
        course_available_marks += results_tuple[1]

    final_results = (course_total_marks, course_available_marks)

    # For testing - sending a class object to Jinja2? God I'm tired...

    return render_template(
        "module_view.html",
        module_id=module_id,
        final_results=final_results,  # (total_marks, possible_marks),
        module_totals=module_totals,  # {module: (total_marks, possible_marks)}
        results_dict=results_dict,  # {module: {assessment: (total_marks, possible_marks)}}
    )


@app.route("/assessment/<int:assessment_id>")
def assessment_view(assessment_id):
    # This value would come from Logged In user.
    student_id = 1
    module_id = 1
    assessment_id = 1

    list_of_student_answers = (
        StudentAnswers.query.filter_by(student_id=student_id)
        .filter_by(module_id=module_id)
        .filter_by(assessment_id=assessment_id)
        .all()
    )
    print(list_of_student_answers)

    total_possible_marks_for_assessment = sum(
        [answer.marks for answer in list_of_student_answers]
    )
    print(f"total_possible_marks_for_assessment: {total_possible_marks_for_assessment}")

    total_marks_for_assessment = sum(
        [answer.marks for answer in list_of_student_answers if answer.correct_answer]
    )
    print(f"total_marks_for_assessment: {total_marks_for_assessment}")

    # For module view we can make a list of lists (assessments),
    # then pass in each of those into a functional version

    return render_template(
        "index.html",
        average_mark=0,
        list_of_student_answers=list_of_student_answers,
    )
