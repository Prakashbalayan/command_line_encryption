# command_line_encryption
A simple command-line tool to encrypt files using AES encryption (via Python's cryptography library). Takes a password and securely encrypts the content of any file, saving it with a .enc extension.
Here’s a complete and beginner-friendly **`README.md`** file for your GitHub project:


### 📌 Features

* 🔒 AES encryption using Fernet (AES-128)
* 🔑 Password-based key generation
* 📁 File-level encryption
* 🖥 Command-line interface (CLI)
* 💡 Easy to use for beginners


### 🛠️ Requirements

* Python 3.x
* `cryptography` library

Install the required package using:

bash
pip install cryptography


### 🚀 How to Use

#### 1. 📄 Prepare Your File

Place the file you want to encrypt (e.g., `sample.txt`) in the same folder as the script.

#### 2. ▶️ Run the Script
bash
python file_encrypt.py --file sample.txt --algorithm AES --key mysecretpassword


* `--file`: path to the input file
* `--algorithm`: set as `AES` (only AES is supported)
* `--key`: your secret password (used to generate encryption key)

#### ✅ Output

A new encrypted file will be created: `sample.txt.enc`

---

### 📂 Example Folder Structure


project-folder/
├── file_encrypt.py
├── sample.txt
└── sample.txt.enc
```

---

### 🔧 How It Works

* The password you enter is converted into a 32-byte key using **SHA-256**.
* The file contents are encrypted using **Fernet (AES-based)**.
* The encrypted content is saved as a `.enc` file.

---

### 📌 Note

* This script supports **only encryption**. You can add decryption support if needed.
* Use a strong password to ensure security.


### 🧑‍💻 Author

Made by \Prakash.B
📧 Email: \ prakashbalayan1@gmail.com 
