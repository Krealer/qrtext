from flask import Flask, render_template, request
import qrcode
import os
import uuid

app = Flask(__name__)
QR_FOLDER = "static/qr_codes"
os.makedirs(QR_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_filename = None
    if request.method == "POST":
        text = request.form.get("text")
        if text:
            qr_id = str(uuid.uuid4())[:8]
            qr_path = os.path.join(QR_FOLDER, f"{qr_id}.png")

            img = qrcode.make(text)
            img.save(qr_path)

            qr_filename = f"{qr_id}.png"

    return render_template("index.html", qr_filename=qr_filename)

if __name__ == "__main__":
    print("QRText running at: http://localhost:5000")
    app.run(debug=True)
