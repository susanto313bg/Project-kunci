from datetime import datetime
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html")


@app.route("/api/login", methods=["POST"])
def login():
  data = request.get_json() or {}
  password = data.get("password", "").strip()

  # SILAHKAN UBAH PASSWORD DI SINI SESUAI KEINGINAN ANDA
  # Contoh password saat ini diset: "1234"
  if password == "1234":
    now = datetime.now()
    user_info = {
        "id": "BG-8899",
        "name": "TEKNISI BEKASI",
        "role": "TEKNISI",
        "today_date": now.strftime("%d-%m-%Y"),
        "login_time": now.strftime("%H:%M:%S"),
    }
    return jsonify({"success": True, "user": user_info})
  else:
    return jsonify({"success": False, "message": "Password salah!"})


if __name__ == "__main__":
  app.run(debug=True)
