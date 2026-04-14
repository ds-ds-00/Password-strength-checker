# 🔐 Password Strength Checker

A simple yet powerful Python-based tool to analyze password strength and estimate how long it would take to crack it using brute-force techniques.

---

## 🚀 Features

* ✅ Password strength scoring (Weak → Very Strong)
* 🔢 Crack time estimation (based on brute-force attack)
* ⚠️ Detects common passwords using wordlist (rockyou.txt)
* ⏱ Human-readable time format (seconds → years)
* 🧠 Based on real-world cracking concepts

---

## 🛠️ Tech Stack

* Python 3

---

## 📂 Project Structure

```
password-analyzer/
│── password_analyzer.py
│── rockyou.txt   (you dont need to download this if you use kali linux)
│── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/password-analyzer.git
cd password-analyzer
mv </path_to_your_rockyou.txt/> <currend folder>
```

---

### 2. Download `rockyou.txt`

This project uses a common password wordlist.

👉 Download it from:

* https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt

OR (Linux users):

```bash
sudo apt install wordlists
```

Then copy:

```bash
cp /usr/share/wordlists/rockyou.txt .
```

⚠️ Make sure `rockyou.txt` is in the **same folder** as your Python script.

---

### 3. Run the program

```bash
python password_analyzer.py
```

---

## 💡 Example Output

```
Enter password: P@$$w0rd12#

Strength: Very Strong
Crack Time: 160.55 years
```

If found in leaked credentials:

```
This is a COMMON password! Extremely unsafe.
```

---

## 🧠 How It Works

* Calculates **character set size** based on:

  * lowercase
  * uppercase
  * digits
  * special characters

* Estimates total combinations:

```
charset ^ length
```

* Simulates cracking speed:

```
~10^12 guesses/sec (modern GPU estimate)
```

---

## 🔥 Future Improvements

* GUI version (Tkinter / Web UI)
* Password entropy calculation
* Real-time typing feedback
* Integration with breach APIs
* Hash cracking simulation


---

## ⭐ Support

If you like this project:

* Share with others
* Improve & contribute

---

> "Strong passwords are your first line of defense."

