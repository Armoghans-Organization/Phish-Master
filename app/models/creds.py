from app import db
from datetime import datetime


class Creds(db.Model):
    __tablename__ = 'creds'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    ip = db.Column(db.String(50), nullable=False)
    site = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # Relationship to the Media model
    medias = db.relationship('Media', backref='creds', lazy=True)
    # Relationship to the Info model
    infos = db.relationship('Info', backref='creds', lazy=True)

    def __repr__(self):
        return f"Creds(username='{self.username}', ip='{self.ip}', site='{self.site}')"