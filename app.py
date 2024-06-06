from CataractScanner.Scanner.cataract_scanner import CataractDetector
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

import os

app = Flask(__name__)

# Define the upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check if a file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for uploading an image
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        print("FileType :::",type(file))
        # Process the uploaded image here (e.g., detect cataracts)
        # result = detect_cataracts(file_path)
        image_path='C:/Users/mmk20/OneDrive/Desktop/cataract/myProject/myCataract/CataractScanner/uploads'+'/'+filename
        print("ImagePath:::::",image_path)
        detector = CataractDetector()
        result=detector.detect_cataract(image_path)

        return render_template('result.html', result=result, filename=filename)
    else:
        return render_template('error.html')

# Function to detect cataracts (dummy function)
def detect_cataracts(image_path):
    # Dummy function for demonstration purposes
    # Replace this with your actual cataract detection algorithm
    return True

if __name__ == '__main__':
    app.run(debug=True)