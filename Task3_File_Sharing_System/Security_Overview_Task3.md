
# **Security Overview – Task 3: Secure File Sharing System**

## **1. Introduction**
The **Secure File Sharing System** is a Flask-based web application designed to securely upload and download files. The system ensures **data confidentiality** by using **AES-256 encryption** to protect files both at rest (when stored on the server) and during download. This project simulates real-world secure file sharing scenarios where sensitive data must be protected from unauthorized access.

---

## **2. Encryption Implementation**

### **2.1 AES-256 Encryption (CBC Mode)**
- **AES (Advanced Encryption Standard)** is a symmetric encryption algorithm widely used for secure data protection.
- **256-bit key** is generated using `Crypto.Random.get_random_bytes(32)`.
- **CBC (Cipher Block Chaining) mode** is used, which combines each plaintext block with the previous ciphertext block for added security.
- Each encryption operation generates a **unique Initialization Vector (IV)** to ensure that identical files produce different ciphertext.

### **2.2 File Encryption Workflow**
1. **Upload:**  
   - The file is read as binary data.
   - The `encrypt_file()` function pads the data to match AES block size.
   - The IV and encrypted data are stored together in the `uploads/` directory.

2. **Download:**  
   - The `decrypt_file()` function reads the encrypted file.
   - It extracts the IV, decrypts the file, and removes padding.
   - A decrypted copy is generated and sent to the user.

---

## **3. Key Management**
- The AES key is stored in a binary file named **`key.key`**, not hardcoded in the application.
- The key is **generated once** using `Crypto.Random.get_random_bytes()` and reused for all encryption/decryption operations.
- Access to `key.key` is restricted to server-side operations; it is never transmitted over the network.

---

## **4. Security Considerations**
- **Confidentiality:** AES-256 provides industry-standard encryption strength.
- **Data Integrity:** While AES ensures confidentiality, checksums or HMAC can be added in future improvements to verify file integrity.
- **Secure File Handling:** Files are never stored in plaintext on the server.
- **Session Feedback:** Flash messages are used to inform users of upload/download success, reducing potential confusion or misuse.

---

## **5. Future Enhancements**
- Add **user authentication (Flask-Login)** to ensure only authorized users can upload/download files.
- Implement **HTTPS** with TLS for encrypted file transfer.
- Add **logging and intrusion detection** for enhanced monitoring.
- Introduce **file integrity checks (SHA-256 hashes)** to prevent tampering.

---

## **6. Conclusion**
This project demonstrates how **cryptography, secure coding practices, and web development** can be combined to create a practical file sharing system with robust security features. By using AES-256 encryption, proper key management, and a secure backend, the application achieves a high level of data protection suitable for real-world use cases.
