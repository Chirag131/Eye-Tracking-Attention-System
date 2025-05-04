from . import db
from datetime import datetime

class UserSession(db.Model):
    __tablename__ = 'user_sessions'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    ended_at = db.Column(db.DateTime)

    # Relationship to logs
    logs = db.relationship('AttentionLog', backref='session', lazy=True)

class AttentionLog(db.Model):
    __tablename__ = 'attention_logs'
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey('user_sessions.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    event_type = db.Column(db.String(50), nullable=False)  
    # Examples: 'gaze_off', 'head_turned', 'tab_switch', 'returned_focus'

    confidence = db.Column(db.Float, nullable=True)  # Optional: ML/gaze confidence
    notes = db.Column(db.Text, nullable=True)        # Optional: extra info like "Looked left for 3s"
