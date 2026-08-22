from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Data user login
PASSWORDS = {
    "00": {"role": "TEKNISI", "name": "TEKNISI BRANKAS", "id": "1471190"},
    "01": {"role": "ADMIN KUNCI", "name": "ADMIN KUNCI", "id": "1471191"}
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    pwd = data.get("password", "").strip()
    if pwd in PASSWORDS:
        user_info = PASSWORDS[pwd].copy()
        user_info.update({
            "login_time": datetime.now().strftime("%H:%M"), 
            "today_date": datetime.now().strftime("%d %b, %Y")
        })
        return jsonify({"success": True, "user": user_info})
    return jsonify({"success": False, "message": "Password salah!"})

# Handler wajib untuk Vercel Serverless Python
def handler(request, response):
    return app(request, response)

if __name__ == "__main__":
    app.run(debug=True)
