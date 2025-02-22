import os
import subprocess
from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

# 1. Home route
@app.route("/")
def home():
    return "Welcome to my Flask app!"

# 2. htop route
@app.route("/htop")
def htop():
    # Replace with your full name
    full_name = "Ritik Kumar"

    
    try:
        system_username = os.getlogin()
    except OSError:
        system_username = os.environ.get("USER", "unknown")

    # Get current time in IST
    ist_timezone = pytz.timezone("Asia/Kolkata")
    now_ist = datetime.now(ist_timezone)

    # Get output of 'top' in batch mode
    top_output = subprocess.getoutput("top -b -n 1")

    # Build the response
    response = (
        f"Name: {full_name}\n"
        f"Username: {system_username}\n"
        f"Server Time (IST): {now_ist}\n"
        f"TOP output:\n{top_output}\n"
    )
    return f"<pre>{response}</pre>"

if __name__ == "__main__":
    # Run on host=0.0.0.0 so it can be exposed publicly in Codespaces
    app.run(host="0.0.0.0", port=8080)
