from datetime import datetime
from omar import db

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(125), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    projects = db.relationship("project", backref="author", lazy=True)

    def __repr__(self):
        return f"user('{self.username}', '{self.email}')"

class projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"project('{self.name}', '{self.description}', '{self.link}')"


class course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(150), nullable=False)
    icon = db.Column(db.String(20), nullable=False, default="default_icon.jpg")
    projects = db.relationship("project", backref="course_name", lazy=True)

    def __repr__(self):
        return f"Course('{self.name}', '{self.description}', '{self.icon}')"