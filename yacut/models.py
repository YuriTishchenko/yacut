from datetime import datetime

from yacut import db

from .constants import MAX_LENGTH


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_link = db.Column(db.String(128), nullable=False)
    custom_id = db.Column(db.String(MAX_LENGTH), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
