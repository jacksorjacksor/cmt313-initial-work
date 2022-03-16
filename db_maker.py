from my_app import db
from my_app.models import StudentAnswers

db.drop_all()
db.create_all()

value1 = StudentAnswers(
    student_id=1,
    course_id=1,
    module_id=1,
    assessment_id=1,
    question_id=1,
    answer_id=1,
    correct_answer=True,
    marks=4,
)
value2 = StudentAnswers(
    student_id=1,
    course_id=1,
    module_id=2,
    assessment_id=1,
    question_id=1,
    answer_id=1,
    correct_answer=False,
    marks=2,
)
value3 = StudentAnswers(
    student_id=1,
    course_id=1,
    module_id=3,
    assessment_id=1,
    question_id=1,
    answer_id=1,
    correct_answer=True,
    marks=44,
)
value4 = StudentAnswers(
    student_id=1,
    course_id=1,
    module_id=3,
    assessment_id=1,
    question_id=1,
    answer_id=1,
    correct_answer=False,
    marks=100,
)
value5 = StudentAnswers(
    student_id=1,
    course_id=1,
    module_id=3,
    assessment_id=1,
    question_id=1,
    answer_id=1,
    correct_answer=False,
    marks=4,
)
value6 = StudentAnswers(
    student_id=1,
    course_id=1,
    module_id=3,
    assessment_id=2,
    question_id=1,
    answer_id=1,
    correct_answer=True,
    marks=4,
)
value7 = StudentAnswers(
    student_id=1,
    course_id=1,
    module_id=1,
    assessment_id=2,
    question_id=1,
    answer_id=1,
    correct_answer=True,
    marks=4,
)
value8 = StudentAnswers(
    student_id=2,
    course_id=1,
    module_id=1,
    assessment_id=2,
    question_id=1,
    answer_id=1,
    correct_answer=True,
    marks=4,
)

db.session.add_all([value1, value2, value3, value4, value5, value6, value7, value8])

db.session.commit()
