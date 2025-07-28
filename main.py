import io
import threading
import os
import uuid

from flask import Flask, render_template, request, send_file
from PIL import Image, ImageFile

# Allow large image processing
Image.MAX_IMAGE_PIXELS = None
ImageFile.LOAD_TRUNCATED_IMAGES = True

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 40 * 1024 * 1024  # 40MB max per uploaded file

@app.route('/')
def index():
    # loads homepage with compressor
    return render_template('index.html')

@app.route('/convert-to-pdf')
def pdf_form():
    # loads image-to-PDF page
    return render_template('convert_to_pdf.html')

@app.route('/compress', methods=['POST'])
def compress():
    # get uploaded image and form inputs
    image_file = request.files['image']
    compression_percent = int(request.form['quality'])
    resize_percent = int(request.form['resize_percent'])
    quality = 100 - compression_percent  # Pillow expects 1–100

    # open image using PIL
    img = Image.open(image_file)

    # block extremely large images for speed
    if img.width * img.height > 100_000_000:
        return "Image too large to process quickly.", 400

    # resize the image if requested
    if resize_percent < 100:
        w, h = img.size
        new_w = int(w * resize_percent / 100)
        new_h = int(h * resize_percent / 100)
        img = img.resize((new_w, new_h), Image.LANCZOS)

    # generate unique filename and save to disk
    filename = f"{uuid.uuid4().hex}.jpg"
    output_path = os.path.join("temp", filename)
    os.makedirs("temp", exist_ok=True)
    img.save(output_path, optimize=True, quality=quality)

    # schedule file deletion after 5 seconds
    def delete_file(path):
        try:
            os.remove(path)
            print(f"Deleted: {path}")
        except Exception as e:
            print(f"Delete error: {e}")

    threading.Timer(5.0, delete_file, args=[output_path]).start()

    # return the saved file to user
    return send_file(output_path, as_attachment=True)

@app.route('/convert-to-pdf', methods=['POST'])
def convert_to_pdf():
    # get list of uploaded images
    files = request.files.getlist('images[]')
    images = []

    # open each file and convert to RGB
    for file in files:
        try:
            img = Image.open(file).convert("RGB")
            # block per-image huge sizes (about ~40MB uncompressed RGB)
            if img.width * img.height > 14_000_000:
                return "One image too large.", 400
            images.append(img)
        except Exception as e:
            return f"Error processing image: {e}", 400

    if not images:
        return "No valid images uploaded.", 400

    # save all pages into a PDF in memory
    buf = io.BytesIO()
    images[0].save(buf, format='PDF', save_all=True, append_images=images[1:])
    buf.seek(0)

    # return in-memory PDF to user
    return send_file(
        buf,
        as_attachment=True,
        download_name=f"{uuid.uuid4().hex}_merged.pdf",
        mimetype='application/pdf'
    )

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
