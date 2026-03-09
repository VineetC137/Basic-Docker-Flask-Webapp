from flask import Flask, render_template_string
import datetime
import random

app = Flask(__name__)

quotes = [
    "Small steps every day lead to big results.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "First solve the problem, then write the code.",
    "Dream big. Start small. Act now.",
    "Consistency beats talent when talent doesn’t work hard."
]

html_template = """
<!DOCTYPE html>
<html>
<head>
<title>Flask Smart Dashboard</title>
<style>
body{
    font-family: Arial;
    background: linear-gradient(135deg,#1f4037,#99f2c8);
    color:white;
    text-align:center;
    padding-top:100px;
}
.card{
    background:rgba(0,0,0,0.3);
    padding:30px;
    border-radius:10px;
    width:500px;
    margin:auto;
}
h1{
    font-size:40px;
}
p{
    font-size:20px;
}
</style>
</head>
<body>

<div class="card">
<h1>Welcome Vineet 🚀</h1>
<p><b>Current Time:</b> {{time}}</p>
<p><b>Motivation:</b> "{{quote}}"</p>
<p>Your Flask Docker App is running successfully!</p>
</div>

</body>
</html>
"""

@app.route("/")
def home():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    quote = random.choice(quotes)

    return render_template_string(html_template, time=current_time, quote=quote)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)