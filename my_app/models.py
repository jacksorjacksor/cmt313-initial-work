from my_app import db, models
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property


class StudentAnswers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    module_id = db.Column(db.Integer)
    assessment_id = db.Column(db.Integer)
    question_id = db.Column(db.Integer)
    answer_id = db.Column(db.Integer)
    correct_answer = db.Column(db.Boolean, default=False, nullable=False)
    marks = db.Column(db.Integer)

    @property
    def serialized(self):
        """Return object data in serializeable format"""
        return {
            "id": self.id,
            "student_id": self.student_id,
            "timestamp": self.timestamp,
            "module_id": self.module_id,
            "assessment_id": self.assessment_id,
            "question_id": self.question_id,
            "answer_id": self.answer_id,
            "correct_answer": self.correct_answer,
            "marks": self.marks,
        }
