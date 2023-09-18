#associations schema
#--------------------------------------------------------

from .db import db
from .user import User
from .event import Event
from .association import Association

class Associations(db.Model):
    __tablename__ = 'associations'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) #user_id
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False) #event_id
    association_id = db.Column(db.Integer, db.ForeignKey('associations.id'), nullable=False) #association_id
    association = db.relationship('Association', back_populates='associations')
    user = db.relationship('User', back_populates='associations')
    event = db.relationship('Event', back_populates='associations')