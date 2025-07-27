from flask import Flask, render_template, request, jsonify
import string
import random

app = Flask(__name__)

# Common breached passwords
breached_words = ["password", "123456", "admin", "qwerty", "letmein"]

def generate_password(length=12, use_digits=True, use_symbols=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def check_strength(pw):
    score = 0
    suggestions = []

    if len(pw) >= 8:
        score += 1
    else:
        suggestions.append("- Add more characters (minimum 8)")

    if any(c.islower() for c in pw):
        score += 1
    else:
        suggestions.append("- Include lowercase letters")

    if any(c.isupper() for c in pw):
        score += 1
    else:
        suggestions.append("- Include uppercase letters")

    if any(c.isdigit() for c in pw):
        score += 1
    else:
        suggestions.append("- Include digits (0-9)")

    if any(c in string.punctuation for c in pw):
        score += 1
    else:
        suggestions.append("- Include symbols like ! @ #")

    if any(b in pw.lower() for b in breached_words):
        suggestions.append("- Avoid using common passwords")
        score = 0

    if score <= 2:
        return "Weak", suggestions
    elif score <= 4:
        return "Moderate", suggestions
    else:
        return "Strong", suggestions

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    pw = data.get("password", "")
    strength, tips = check_strength(pw)
    return jsonify({"strength": strength, "tips": tips})

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    length = int(data.get("length", 12))
    use_digits = data.get("digits", True)
    use_symbols = data.get("symbols", True)
    password = generate_password(length, use_digits, use_symbols)
    return jsonify({"password": password})

if __name__ == '__main__':
    app.run(debug=True)
