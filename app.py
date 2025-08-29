from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(_name_)
CORS(app)

# User details
FULL_NAME = "john_doe"
DOB = "17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

def process_data(data):
    odd_numbers = []
    even_numbers = []
    alphabets = []
    special_chars = []
    total_sum = 0

    for item in data:
        if item.isdigit():
            num = int(item)
            total_sum += num
            if num % 2 == 0:
                even_numbers.append(item)
            else:
                odd_numbers.append(item)
        elif item.isalpha():
            alphabets.append(item.upper())
        else:
            special_chars.append(item)

    concat_string = ""
    combined_alpha = "".join(alphabets)[::-1]
    for i, ch in enumerate(combined_alpha):
        concat_string += ch.lower() if i % 2 else ch.upper()

    return {
        "is_success": True,
        "user_id": f"{FULL_NAME}_{DOB}",
        "email": EMAIL,
        "roll_number": ROLL_NUMBER,
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_chars,
        "sum": str(total_sum),
        "concat_string": concat_string
    }

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/bfhl", methods=["POST"])
def bfhl():
    try:
        data = request.json.get("data", [])
        if not isinstance(data, list):
            return jsonify({"is_success": False, "message": "Invalid input format"}), 400

        result = process_data(data)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 500

if _name_ == "_main_":
    app.run(debug=True)