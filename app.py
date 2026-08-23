from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Data user login sementara
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

# Rute untuk halaman cetak dokumen per team (1 team = 1 halaman cetak)
@app.route("/cetak-dokumen")
def cetak_dokumen():
    # Data simulasi team yang akan dicetak
    data_team = [
        {
            "nama_team": "TEAM RPL MALAM 1",
            "items": [
                {"tid": "k,k..", "lokasi": "ATM-k,k.. (BEKASI)", "barcode": "RPL-k,k..-99", "rak": "R-01", "baris": "B-01", "kolom": "K-01", "keterangan": "Ready"},
                {"tid": "k,k2..", "lokasi": "ATM-k,k2 (BEKASI)", "barcode": "RPL-k,k2-99", "rak": "R-01", "baris": "B-01", "kolom": "K-02", "keterangan": "Ready"}
            ]
        },
        {
            "nama_team": "TEAM RPL MALAM 2",
            "items": [
                {"tid": "ghgtnhm", "lokasi": "ATM-ghgtnhm (BEKASI)", "barcode": "RPL-ghgtnhm-99", "rak": "R-01", "baris": "B-01", "kolom": "K-01", "keterangan": "Ready"}
            ]
        }
    ]
    return render_template("cetak_team.html", list_team=data_team)

# Baris ini penting agar Vercel mendeteksi aplikasi Flask
if __name__ == "__main__":
    app.run(debug=True)
