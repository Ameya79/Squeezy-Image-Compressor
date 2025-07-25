import threading
from flask import Flask, render_template, request, send_file
from PIL import Image
import uuid
import os #just interacts with the underlying systems

app = Flask(__name__) #start flask

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compress', methods= ['POST'])
def compress():
    #necessities
    image_file = request.files['image'] # gets img from the form, via requesting the file
    compressionpercent = int(request.form['quality']) #gets the quality
    resizepercent = int(request.form['resize_percent']) #gets the quality
    quality = 100 - compressionpercent
    
    img = Image.open(image_file)

    if resizepercent <100:
        width,height = img.size
        new_width = int(width * resizepercent / 100)
        new_height = int(height * resizepercent / 100)
        img = img.resize((new_width, new_height), Image.LANCZOS)

#to open the uploaded img:

    #generate unique file names
    filename = f"{uuid.uuid4().hex}.jpg"
    output = os.path.join("temp",filename)

    #create a temp folder
    os.makedirs("temp",exist_ok=True)

    #compress and save
    img.save(output, optimize = True, quality = quality)

    #autodelete
  
    def remove_file(path):
        try:
            os.remove(path)
            print(f"Deleted: {path}")
        except Exception as e:
            print(f"Error deleting file: {e}")

    threading.Timer(5.0, remove_file, args=[output]).start()    
    #send back file
    return send_file(output, as_attachment=True)




if __name__ == '__main__': #start erver only if stuff is imported
    app.run(debug=True)
        
    

