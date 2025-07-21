# 🔐 Secure File Sharing System

A simple yet secure file sharing web application built with **Python Flask** and **AES-256 encryption**.  
This project was developed as part of **Task 3 – Future Interns Cybersecurity Internship (2025)**.

---

## **Features**
- **Upload and download files securely.**
- **AES-256 encryption** (CBC mode) applied to all files at rest.
- **Automatic decryption** during downloads.
- **User-friendly interface** with flash messages and live file listing.
- Lightweight and easy to run locally.

---

## **Security Highlights**
- **AES-256 encryption** ensures strong data confidentiality.
- **Key management:** The AES key is stored in `key.key` (kept outside code).
- **Integrity:** Encrypted files are unreadable without the correct key.
- **Flask flash messages** enhance user awareness of file operations.

---

## **Getting Started**

### **Prerequisites**
- Python 3.8+  
- Virtual environment (recommended)

### **Setup Steps**
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/secure_file_sharing.git
cd secure_file_sharing

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python3 app.py


