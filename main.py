import threading
from flask import Flask, render_template, request, send_file
from PIL import Image
import uuid
import os  # to interact with filesystem

app = Flask(__name__)  # initialize Flask app

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
    # gets uploaded image and form inputs
    image_file = request.files['image']
    compression_percent = int(request.form['quality'])
    resize_percent = int(request.form['resize_percent'])
    quality = 100 - compression_percent  # Pillow needs quality value from 1–100

    # open image using PIL
    img = Image.open(image_file)

    # resize the image if needed
    if resize_percent < 100:
        width, height = img.size
        new_width = int(width * resize_percent / 100)
        new_height = int(height * resize_percent / 100)
        img = img.resize((new_width, new_height), Image.LANCZOS)

    # create output path
    filename = f"{uuid.uuid4().hex}.jpg"
    output = os.path.join("temp", filename)
    os.makedirs("temp", exist_ok=True)

    # save compressed image
    img.save(output, optimize=True, quality=quality)

    # schedule file deletion after 5 seconds
    def delete_file(path):
        try:
            os.remove(path)
            print(f"Deleted: {path}")
        except Exception as e:
            print(f"Delete error: {e}")

    threading.Timer(5.0, delete_file, args=[output]).start()

    # return compressed file to user
    return send_file(output, as_attachment=True)

@app.route('/convert-to-pdf', methods=['POST'])
def convert_to_pdf():
    # receives multiple images as input
    files = request.files.getlist('images[]')
    images = []

    # convert all images to RGB and store
    for file in files:
        try:
            img = Image.open(file).convert("RGB")
            images.append(img)
        except Exception as e:
            return f"Error processing image: {e}", 400

    if not images:
        return "No valid images uploaded.", 400

    # output file name and path
    output_path = os.path.join("temp", f"{uuid.uuid4().hex}_merged.pdf")
    os.makedirs("temp", exist_ok=True)

    # save first image and append rest
    images[0].save(output_path, save_all=True, append_images=images[1:])

    # auto-delete PDF after 5 seconds
    threading.Timer(5.0, lambda: os.remove(output_path)).start()

    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)