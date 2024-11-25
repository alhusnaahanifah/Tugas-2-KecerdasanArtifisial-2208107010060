from flask import Flask, render_template, request, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Load model
model = load_model("trashfix_model.h5")
print("Model berhasil dimuat.")

# Daftar kelas
class_names = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]

# Folder untuk menyimpan gambar yang diunggah
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Periksa apakah ada file yang diunggah
        if "file" not in request.files:
            return "Tidak ada file yang diunggah"
        file = request.files["file"]
        
        if file.filename == "":
            return "File tidak valid"
        
        if file:
            # Simpan file
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)
            
            # Prediksi gambar
            try:
                img = image.load_img(filepath, target_size=(150, 150))  # Sesuaikan ukuran
                img_array = image.img_to_array(img) / 255.0
                img_array = np.expand_dims(img_array, axis=0)

                predictions = model.predict(img_array)
                class_idx = np.argmax(predictions[0])
                class_names = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]
                
                predicted_class = class_names[class_idx]

                return render_template(
                    "index.html",
                    predicted_class=predicted_class,
                    image_path=filepath,
                )
            except Exception as e:
                # return f"Terjadi kesalahan saat memproses gambar: {e}"
                return render_template(
                    "index.html",
                    predicted_class= "Gambar tidak terdefinisi",
                    image_path=filepath,
                )
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)