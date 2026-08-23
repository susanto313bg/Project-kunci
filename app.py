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

# Rute untuk memproses dan menampilkan halaman cetak secara dinamis (Realtime)
@app.route("/cetak-dokumen", methods=["POST", "GET"])
def cetak_dokumen():
    if request.method == "POST":
        # Menangkap data yang dikirim secara realtime dari form web
        nama_team = request.form.get("nama_team", "TEAM TANPA NAMA")
        list_tid = request.form.getlist("tid[]") # Menangkap semua input TID
        
        # Menyusun data ke format item tabel
        items = [{"tid": tid} for tid in list_tid if tid.strip() != ""]
        
        data_team = [
            {
                "nama_team": nama_team,
                "items": items if items else [{"tid": "-"}]
            }
        ]
    else:
        # Data default jika diakses langsung via URL (GET)
        data_team = [
            {
                "nama_team": "SUSANTO",
                "items": [{"tid": "48494998+"}, {"tid": "465846596"}, {"tid": "369596565"}]
            }
        ]
        
    return render_template("cetak_team.html", list_team=data_team)

# Baris ini penting agar Vercel mendeteksi aplikasi Flask
if __name__ == "__main__":
    app.run(debug=True)
