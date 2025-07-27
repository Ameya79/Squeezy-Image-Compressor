import threading
from flask import Flask, render_template, request, send_file
from PIL import Image
import uuid
import os  # just interacts with the underlying system
import cv2  # for image processing
import numpy as np  # to convert file buffer to array for OpenCV

app = Flask(__name__)  # start flask

@app.route('/')
def index():
    return render_template('index.html')  # homepage

@app.route('/upscale')
def upscale():
    return render_template('upscale.html')  # upscale page

@app.route('/compress', methods=['POST'])
def compress():
    # get file and inputs from form
    image_file = request.files['image']
    compression_percent = int(request.form['quality'])
    resize_percent = int(request.form['resize_percent'])
    quality = 100 - compression_percent

    # open image using PIL
    img = Image.open(image_file)

    # optionally resize the image if resize percent < 100
    if resize_percent < 100:
        width, height = img.size
        new_width = int(width * resize_percent / 100)
        new_height = int(height * resize_percent / 100)
        img = img.resize((new_width, new_height), Image.LANCZOS)

    # generate file name and path
    filename = f"{uuid.uuid4().hex}.jpg"
    output = os.path.join("temp", filename)
    os.makedirs("temp", exist_ok=True)

    # save compressed image using PIL
    img.save(output, optimize=True, quality=quality)

    # schedule delete after 5 seconds
    def delete_file(path):
        try:
            os.remove(path)
            print(f"Deleted: {path}")
        except Exception as e:
            print(f"Delete error: {e}")

    threading.Timer(5.0, delete_file, args=[output]).start()

    # return file to user
    return send_file(output, as_attachment=True)

@app.route('/upscale-process', methods=['POST'])
def upscale_process():
    # check if image is uploaded
    if 'image' not in request.files or request.files['image'].filename == '':
        return "No file uploaded", 400

    # get file and scale
    image_file = request.files['image']
    scale = int(request.form['scale'])

    try:
        # convert uploaded image file to array for OpenCV
        file_bytes = np.frombuffer(image_file.read(), np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        if img is None:
            return "Invalid image file", 400

        # upscale using cubic interpolation
        new_width = img.shape[1] * scale
        new_height = img.shape[0] * scale
        upscaled = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

        # apply strong sharpening filter
        sharpening_kernel = np.array([[0, -1, 0],
                                      [-1, 5.5, -1],
                                      [0, -1, 0]])
        sharpened = cv2.filter2D(upscaled, -1, sharpening_kernel)

        # save upscaled + sharpened image to temp
        filename = f"{uuid.uuid4().hex}_upscaled.jpg"
        output = os.path.join("temp", filename)
        os.makedirs("temp", exist_ok=True)
        cv2.imwrite(output, sharpened)

        # delete file after 5 seconds
        def delete_file(path):
            try:
                os.remove(path)
                print(f"Deleted: {path}")
            except Exception as e:
                print(f"Delete error: {e}")

        threading.Timer(5.0, delete_file, args=[output]).start()

        # return file
        return send_file(output, as_attachment=True)

    except Exception as e:
        print(f"Upscaling error: {e}")
        return f"Error occurred: {e}", 500


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # default port or from env
    app.run(debug=False, host="0.0.0.0", port=port)
