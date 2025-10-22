import qrcode
from PIL import Image
import flask
from flask import Flask, render_template, request, send_file

app = Flask(__name__) 

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form.get("data", "")
        if data:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img_path = "static/qr_code.png"
            img.save(img_path)
            return send_file(img_path, mimetype='image/png')
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
