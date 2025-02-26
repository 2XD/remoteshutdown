# Secure Flask Remote Shutdown API

A secure API to remotely shut down your PC using Flask, featuring brute-force protection, password hashing, and more.

# Setup
Install dependencies (pip install -r requirements.txt)

Generate your hashed password and secret key by opening generate_hash.py
This is saved as a .env file

Add allowed ips to allowedips.env, if not just leave empty

Run the app.py next

# How to Use From Phone

Now it is ready to accessed from your phone you can access it from.
http://<your-ip>:5000/shutdown?password=<your-password>&key=<your-secret-key>
