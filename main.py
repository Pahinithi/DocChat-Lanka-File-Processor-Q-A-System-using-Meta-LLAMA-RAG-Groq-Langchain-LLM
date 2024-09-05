from flask import Flask, request, render_template
import numpy as np
import tensorflow as tf
from PIL import Image
import fitz  # PyMuPDF
from io import BytesIO

# Create a Flask application instance
app = Flask(__name__)

# Load your trained model
model = tf.keras.models.load_model('Doc_and_QA.h5')

# Initialize a list to keep track of history
history = []

# Define a route for the homepage
@app.route("/")
def home():
    return render_template("index.html")

# Define a route for processing the file
@app.route("/process", methods=["POST"])
def process():
    # Get the uploaded file
    file = request.files['file']
    file_type = file.content_type
    
    if file:
        if 'image' in file_type:
            # Process the uploaded image
            img = Image.open(file)
            img = img.resize((32, 32))
            img = np.array(img) / 255.0
            img = np.expand_dims(img, axis=0)
            
            # Make a prediction using the model
            predictions = model.predict(img)
            predicted_class = np.argmax(predictions, axis=1)[0]
            
            # Mapping predicted class to label (update as needed)
            labels_dictionary = {0: 'Class1', 1: 'Class2', 2: 'Class3'}  # Modify this as per your model
            prediction_text = f'The predicted class is: <strong>{labels_dictionary.get(predicted_class, "Unknown")}</strong>'
        
        elif 'pdf' in file_type:
            # Extract text from PDF
            pdf_document = fitz.open(stream=file.read(), filetype="pdf")
            text = ""
            for page in pdf_document:
                text += page.get_text()
            
            prediction_text = f"Extracted text from PDF: <pre>{text}</pre>"
        
        else:
            prediction_text = "Unsupported file type."
        
        # Save the result to history
        history.append(prediction_text)
        
        return render_template("index.html", result=prediction_text)
    
    return render_template("index.html", result="No file uploaded.")

# Define a route for the history page
@app.route("/history")
def show_history():
    return render_template("history.html", history=history)

# Start the Flask application
if __name__ == "__main__":
    app.run(debug=True)
