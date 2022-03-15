from my_app import db
from my_app.models import StudentAnswers

db.drop_all()
db.create_all()

value1 = StudentAnswers(
    student_id=1,
    module_id=1,
    assessment_id=1,
    question_id=1,
    answer_id=1,
    correct_answer=True,
    marks=1,
)
value2 = StudentAnswers(
    student_id=1,
    module_id=1,
    assessment_id=1,
    question_id=2,
    answer_id=1,
    correct_answer=False,
    marks=2,
)
value3 = StudentAnswers(
    student_id=1,
    module_id=1,
    assessment_id=1,
    question_id=4,
    answer_id=1,
    correct_answer=True,
    marks=3,
)
value4 = StudentAnswers(
    student_id=1,
    module_id=1,
    assessment_id=2,
    question_id=1,
    answer_id=1,
    correct_answer=True,
    marks=4,
)

db.session.add_all([value1, value2, value3, value4])

db.session.commit()
