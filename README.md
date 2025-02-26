# Secure Flask Remote Shutdown

A secure API to remotely shut down your PC using Flask, featuring brute-force protection, password hashing, and more.

# Setup Script
Install dependencies (pip install -r requirements.txt)

Generate your hashed password and secret key by opening generate_hash.py. You can do this every time you use it or just once, totally up to you.
This is saved as the .env file

# Setup Port to Access
The bot is made to access port 5000 as this is port is openable on almost any device but feel free to change it if you want.
First go to security and make sure you allow python to communicate through both public and private firewall.
Then run wf.msc (windows + R and type in wf.msc)
Go to inbound rules and create a new rule 
Rule Type: Port
Protocols and Ports: TCP and enter whatever port you chose (make sure you change in app.py as well if you arent using 5000)
Action: Allow the connection
Profile: Private and Public
Name: Whatever you want
Run the app.py next

# How to Use From Phone
Now it is ready to accessed from your phone or any other device! The link to access is printed when you run app.py or you can access it from:
http://<your-ip>:5000/shutdown?password=<your-password>&key=<your-secret-key>
