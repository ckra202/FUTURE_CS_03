from flask import Flask, render_template, request, send_from_directory, redirect, url_for, flash
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Flask app configuration
app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Used for flash messages (can be improved in production)

# Upload folder (encrypted files are stored here)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load AES encryption key from file
def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

AES_KEY = load_key()  # AES-256 key

# Encrypt a file using AES-CBC
def encrypt_file(data):
    cipher = AES.new(AES_KEY, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    return cipher.iv + ct_bytes  # Prepend IV for decryption

# Decrypt a file using AES-CBC
def decrypt_file(data):
    iv = data[:16]
    cipher = AES.new(AES_KEY, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(data[16:]), AES.block_size)
    return pt

# Home route (shows upload form and available files)
@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('upload.html', files=files)

# Upload route (encrypts and saves file)
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(url_for('index'))

    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('index'))

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file_data = file.read()
    encrypted_data = encrypt_file(file_data)

    with open(filepath, "wb") as f:
        f.write(encrypted_data)

    flash(f"File {file.filename} uploaded and encrypted successfully!")
    return redirect(url_for('index'))

# Download route (decrypts file on download)
@app.route('/download/<filename>')
def download_file(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    with open(filepath, "rb") as f:
        encrypted_data = f.read()

    decrypted_data = decrypt_file(encrypted_data)
    temp_path = os.path.join(app.config['UPLOAD_FOLDER'], "decrypted_" + filename)
    with open(temp_path, "wb") as f:
        f.write(decrypted_data)

    flash(f"File {filename} decrypted and ready for download!")
    return send_from_directory(app.config['UPLOAD_FOLDER'], "decrypted_" + filename, as_attachment=True)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
