from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'

@app.route('/analyze', methods=['POST'])
def analyze_text():
    text = request.form.get('text')
    file = request.files.get('file')

    # Handle file uploads
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        with open(filepath, 'r') as f:
            text = f.read()

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # Dummy key points generation (replace with your analysis logic)
    summary = ' '.join(text.split()[:10])  # Example: First 10 words
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
