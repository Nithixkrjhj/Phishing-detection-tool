# 🛡️ Phishing Attack Simulation & Detection Report


## 1. Introduction
Phishing is one of the most common cyberattacks used to steal sensitive information such as login credentials and financial data. This project focuses on simulating phishing scenarios and detecting suspicious inputs using basic cybersecurity techniques.

---

## 2. Objective
The objective of this project is to:
- Simulate a phishing login page
- Analyze URLs and messages for malicious patterns
- Raise awareness about phishing attacks
- Provide a basic detection mechanism

---

## 3. Methodology

### 3.1 Phishing Simulation
A web interface resembling a login page was created using HTML and Flask. This simulates how attackers trick users into entering sensitive data.

### 3.2 URL Analysis
The system checks:
- If the URL uses HTTP instead of HTTPS
- Presence of suspicious symbols like '@' or '-'

### 3.3 Keyword Detection
The system scans messages for phishing-related keywords such as:
- verify
- urgent
- password
- bank
- security alert

### 3.4 Result Generation
Based on analysis, the system displays warnings and highlights suspicious indicators.

---

## 4. Tools & Technologies
- Python (Core programming)
- Flask (Web framework)
- HTML/CSS (Frontend)
- Regex (Pattern detection)

---

## 5. Results
The system successfully detects:
- Insecure URLs (HTTP)
- Suspicious keyword usage
- Potential phishing indicators

Example output:
## 👨‍💻 10. Author
Nitheesh Krishna P R