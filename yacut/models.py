from datetime import datetime

from yacut import db

from .constants import MAX_LENGTH

class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(128), nullable=False)
    short = db.Column(db.String(MAX_LENGTH))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)


    def to_dict(self):
        return dict(
            id = self.id,
            original = self.original,
            short = self.short,
            timestamp = self.timestamp,
        )
    
    def from_dict(self, data):
        for field in ['original', 'short']:
            if field in data:
                setattr(self, field, data[field]) 