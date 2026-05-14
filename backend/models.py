# Database models
from config import db # Import from config.py

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(80), unique = False, nullable = False)
    last_name = db.Column(db.String(80), unique = False, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    # phone = db.Column(db.String(120), unique = True, nullable = True)
    # location = db.Column(db.String(120), unique = False, nullable = True)
    # company = db.Column(db.String(120), unique = False, nullable = True)
    # links = db.Column(db.String(120), unique = False, nullable = True)
    # notes = db.Column(db.String(500), unique = False, nullable = True)

    def to_json(self):
        return {
            "id" : self.id,
            "firstName" : self.first_name,
            "lastName" : self.last_name,
            "email" : self.email,
            # "phone" : self.phone,
            # "location" : self.location,
            # "company" : self.company,
            # "links" : self.links,
            # "notes" : self.notes,
        }
