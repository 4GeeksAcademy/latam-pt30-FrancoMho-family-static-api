"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#FAMILY ROUTES
#GET ALL MEMBERS
@app.route('/members', methods=['GET'])
def get_members():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "family": members
    }

    return jsonify(response_body), 200

#GET A MEMBER BY ID
@app.route('/member/<int:member_id>', methods=['GET'])
def get_member():

    member = jackson_family.get_member()
    response_body = {
        "member": member
    }

    return jsonify(response_body), 200


#ADD A MEMBER
@app.route('/member', methods=['POST'])
def add_member():
    # Obtener los datos del cuerpo de la solicitud
    body = request.get_json()

# Verificar que se envíen los datos correctos
    if not body:
        return jsonify({"message": "Invalid input, must provide a valid JSON"}), 400
    if "first_name" not in body or "age" not in body or "lucky_numbers" not in body:
        return jsonify({"message": "Missing some required fields"}), 400
    
    new_member={
        "first_name": body["first_name"],
        "age": body["age"],
        "lucky_numbers": body["lucky_numbers"]
    }

    # Agregar el nuevo miembro a la familia
    jackson_family.add_member(new_member)

    return jsonify({"message": "Member added successfully", "member": new_member}), 200

#DELETE MEMBER
@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    # Intentar eliminar el miembro con el id proporcionado
    member = jackson_family.get_member(id)

    if member:
        jackson_family.delete_member(id)
        return jsonify({"message": f"Member with id {id} deleted successfully"}), 200
    else:
        return jsonify({"message": "Member not found"}), 404
    

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
