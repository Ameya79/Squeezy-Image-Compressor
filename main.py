import threading
from flask import Flask, render_template, request, send_file
import uuid
import os  # just interacts with the underlying system
import cv2  # for image processing
import numpy as np  # to convert image files into array format for OpenCV

app = Flask(__name__)  # start Flask app

@app.route('/')
def index():
    return render_template('index.html')  # serve homepage

@app.route('/upscale')
def upscale():
    return render_template('upscale.html')  # serve upscale page

@app.route('/compress', methods=['POST'])
def compress():
    # get image file and form inputs from frontend
    image_file = request.files['image']
    compression_percent = int(request.form['quality'])  # user selected quality to reduce
    resize_percent = int(request.form['resize_percent'])  # optional resize (scale down)
    quality = 100 - compression_percent  # convert to OpenCV compatible quality

    # read image into memory as an array OpenCV can work with
    file_bytes = np.frombuffer(image_file.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if img is None:
        return "Invalid image", 400

    # if user selected resize below 100%, apply it
    if resize_percent < 100:
        new_width = int(img.shape[1] * resize_percent / 100)
        new_height = int(img.shape[0] * resize_percent / 100)
        img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)

    # generate a unique filename to avoid overwriting
    filename = f"{uuid.uuid4().hex}.jpg"
    output = os.path.join("temp", filename)

    # create temp folder if not already present
    os.makedirs("temp", exist_ok=True)

    # save compressed image with given quality
    cv2.imwrite(output, img, [int(cv2.IMWRITE_JPEG_QUALITY), quality])

    # auto-delete after 5 seconds to save storage and maintain privacy
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

    # get image and user-selected scale from frontend
    image_file = request.files['image']
    scale = int(request.form['scale'])  # scale = 2 or 4 (for 2x or 4x)

    try:
        # read uploaded image as OpenCV image array
        file_bytes = np.frombuffer(image_file.read(), np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        if img is None:
            return "Invalid image file", 400

        # calculate new size based on scale value
        new_width = img.shape[1] * scale
        new_height = img.shape[0] * scale

        # resize using CUBIC interpolation which is better for upscaling
        upscaled = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

        # generate unique filename and path
        output_filename = f"{uuid.uuid4().hex}_upscaled.jpg"
        output_path = os.path.join("temp", output_filename)

        # make temp folder if missing
        os.makedirs("temp", exist_ok=True)

        # save the upscaled image
        cv2.imwrite(output_path, upscaled)

        # auto-delete upscaled image after 5 seconds
        def delete_file(path):
            try:
                os.remove(path)
                print(f"Deleted: {path}")
            except Exception as e:
                print(f"Delete error: {e}")

        threading.Timer(5.0, delete_file, args=[output_path]).start()

        # return upscaled image file to user
        return send_file(output_path, as_attachment=True)

    except Exception as e:
        print(f"Upscaling error: {e}")
        return f"Error occurred: {e}", 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # set port from env or use 5000
    app.run(debug=False, host="0.0.0.0", port=port)  # run Flask app publicly
