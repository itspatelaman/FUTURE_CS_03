from flask import Flask, render_template, request, send_file, redirect, url_for, flash
from werkzeug.utils import secure_filename
from encrypt_utils import encrypt_data, decrypt_data, load_key
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # For flashing messages

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

key = load_key()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file selected!')
        return redirect(url_for('index'))
    
    file = request.files['file']
    if file.filename == '':
        flash('No selected file!')
        return redirect(url_for('index'))

    filename = secure_filename(file.filename)
    file_data = file.read()
    encrypted_data = encrypt_data(file_data, key)

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename + '.enc')
    with open(filepath, 'wb') as f:
        f.write(encrypted_data)

    flash('File uploaded and encrypted successfully!')
    return redirect(url_for('index'))

@app.route('/download/<filename>')
def download_file(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    if not os.path.exists(filepath):
        flash('File not found!')
        return redirect(url_for('index'))

    with open(filepath, 'rb') as f:
        encrypted_data = f.read()

    decrypted_data = decrypt_data(encrypted_data, key)

    decrypted_path = os.path.join(app.config['UPLOAD_FOLDER'], 'decrypted_' + filename.replace('.enc', ''))
    with open(decrypted_path, 'wb') as f:
        f.write(decrypted_data)

    return send_file(decrypted_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
