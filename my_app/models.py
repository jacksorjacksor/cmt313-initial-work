from my_app import db, models
from datetime import datetime


class StudentAnswers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    course_id = db.Column(db.Integer)
    module_id = db.Column(db.Integer)
    assessment_id = db.Column(db.Integer)
    question_id = db.Column(db.Integer)
    answer_id = db.Column(db.Integer)
    correct_answer = db.Column(db.Boolean, default=False, nullable=False)
    marks = db.Column(db.Integer)
