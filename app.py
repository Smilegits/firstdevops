from flask import Flask, request, render_template, jsonify
import magic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('smile1.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    file_info = {
        "filename": file.filename,
        "content_type": magic.from_buffer(file.read(), mime=True)
    }

    return jsonify(file_info), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
