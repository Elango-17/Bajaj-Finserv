from flask import Flask, request, jsonify
from flask_cors import CORS
import string
import random

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/bfhl', methods=['POST', 'GET'])
def handle_request():
    if request.method == 'POST':
        data = request.get_json()
        user_id = "john_doe_17091999"  # Replace with actual user id generation logic if needed
        email = "john@xyz.com"         # Replace with actual email
        roll_number = "ABCD123"        # Replace with actual roll number

        numbers = [item for item in data['data'] if item.isdigit()]
        alphabets = [item for item in data['data'] if item.isalpha()]

        highest_alphabet = [max(alphabets, key=str.upper)] if alphabets else []

        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }
        return jsonify(response)

    elif request.method == 'GET':
        return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
