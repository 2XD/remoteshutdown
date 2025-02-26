# Lightweight Remote Shutdown using Flask

A secure API to remotely shut down your PC using Flask, featuring brute-force protection, password hashing, and more.

# Setup Script

1. Install dependencies:

2. Generate your hashed password and secret key by opening `generate_hash.py`. You can do this every time you use it or just once, totally up to you.  
This is saved as the `.env` file.

# Setup Port to Access

The bot is designed to use port 5000, as this port is openable on most devices. However, feel free to change the port if needed.

### Steps to Allow Python Through the Firewall:

1. **Go to Security Settings**:
- Make sure you allow Python to communicate through both the public and private firewall.

2. **Run Windows Firewall Settings**:
- Press `Windows + R`, type `wf.msc`, and hit Enter to open Windows Firewall settings.

3. **Create a New Inbound Rule**:
- Go to **Inbound Rules** and click on **New Rule**.

4. **Configure Rule Type**:
- **Rule Type**: Select **Port**.
- **Protocols and Ports**: Choose **TCP** and enter the port you wish to use (make sure to update the port in `app.py` if you're not using port 5000).
- **Action**: Select **Allow the connection**.
- **Profile**: Choose **Private and Public**.
- **Name**: Enter a name for the rule (you can name it anything you like).

5. **Run the `app.py`**:
- After creating the rule, run the `app.py` script to start the server.

# How to Use From Phone

Now it is ready to be accessed from your phone or any other device! The link to access is printed when you run `app.py` or you can access it from:
http://(your-ip):5000/shutdown?password=(encryptedpass)&key=(encryptedkey)
