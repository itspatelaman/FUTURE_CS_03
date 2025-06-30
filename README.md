# 🔐 Secure File Sharing System

A secure file upload and download web application built using Flask and AES encryption. This project demonstrates a simple yet effective implementation of data confidentiality through symmetric key encryption using Python's `cryptography` library.

> 🚀 Developed as part of Task 3 for the **Future Interns Cybersecurity Internship Program**.

---

## 📌 Project Objective

To simulate a **real-world secure file transfer system** where uploaded files are **encrypted** using AES (Fernet), securely stored, and can later be **decrypted** and downloaded by the user.

---

## 👨‍💻 Intern Details

- **Name**: Aman Patel  
- **Role**: Cybersecurity & Ethical Hacking Enthusiast  
- **Program**: Future Interns – Cybersecurity Internship  
- **Task**: Secure File Sharing System (Task 3)

---

## ⚙️ Features

- 🔐 AES-based encryption using `cryptography.fernet`
- 📤 File Upload → Encrypted & stored securely
- 📥 File Download → Decrypted in real-time
- 💡 Clean and simple HTML interface using Flask & Bootstrap
- 🛡️ Sensitive files ignored via `.gitignore`

---

## 🧰 Tools & Technologies Used

- 🐍 Python 3
- 🧪 Flask
- 🔐 Cryptography (Fernet AES Encryption)
- 💻 VSCode
- 📁 HTML/CSS for frontend

---

## 📁 Project Structure
```
secure-file-sharing/
├── app.py # Flask backend
├── encrypt_utils.py # Encryption & decryption logic
├── secret.key # AES key (generated once)
├── templates/
│ └── index.html # UI for upload/download
├── uploads/ # Encrypted file storage
├── .gitignore # Ignored sensitive/temp files
├── requirements.txt # Dependencies
└── README.md # Project overview
```

---

## 🚀 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/secure-file-sharing.git
   cd secure-file-sharing
    ```
Create a virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate      # Windows
# OR
source venv/bin/activate   # Linux/macOS
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Generate encryption key

bash
Copy
Edit
python -c "from encrypt_utils import generate_key; generate_key()"
Run the Flask app

bash
Copy
Edit
python app.py
Open your browser and visit:
http://127.0.0.1:5000