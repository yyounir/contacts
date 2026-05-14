# CRUD
# Create
# - first_name
# - last_name
# - email
# localhost:5000/create_contact

# Request:
# GET: Access a type a resource
# POST: Creating a new contact
# PUT/PATCH: Updating a contact
# DELETE: Delete a contact, pass the data to delete the contact

# Response:
# The frontend sends the request to the backend, the backend returns a response
# Response may return a status, aka 404 which is not found, 400 - bad request, 403 - Forbidden



# Read
# Update
# Delete

from flask import request, jsonify
from config import app, db              # From config.py
from models import Contact              # From models.py

@app.route("/contacts", methods=["GET"])
# Decorator, creates a new route, specify a route, and specify a valid method aka GET

def get_contacts():
    contacts = Contact.query.all() 
    # Uses flask alchemy as our ORM, gets all the contacts inside of our contacts database
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    # Takes all the elements to the list and applies a function to them and gives the result to the new list

    return jsonify({"contacts": json_contacts})

@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return (
            jsonify({"message": "You must include a first name, last name, and email to create a contact!"}), 
            400,
        )
    
    new_contact = Contact(first_name = first_name, last_name=last_name, email=email)
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "User created!"}), 201

@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)
    # Check if contact doesnt exist
    if not contact:
        return jsonify({"message": "User not found"}), 404
    
    data = request.json
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)

    db.session.commit()

    return jsonify({"message": "User updated"}), 200

@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)
    # Check if contact doesnt exist
    if not contact:
        return jsonify({"message": "User not found"}), 404
    
    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "User deleted!"}), 200




# Run flask app
if __name__ == "__main__":  # Checks if main.py is running, avoids running the other files
    with app.app_context(): # Get context of application
        db.create_all()     # Create all different models that we have to find in our database

    app.run(debug=True)     # Runs the code