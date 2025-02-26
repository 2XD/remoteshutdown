import os
import psutil
import hashlib
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import requests

# Load environment and hashed secrets
load_dotenv()
app = Flask(__name__)
secret_key = os.getenv('SECRET_KEY')
hashed_password = os.getenv('HASHED_PASSWORD')

# shutdown the computer after 1 second using built in windows commands
def shutdown():
    if psutil.WINDOWS:
        os.system("shutdown /s /f /t 1")
    else:
        os.system("shutdown now")

# Function to get public IP address
def get_public_ip():
    try:
        ip = requests.get('https://api.ipify.org').text
        return ip
    except requests.RequestException:
        return "Unable to fetch IP"

# Route for shutdown
@app.route('/shutdown', methods=['GET'])
def remote_shutdown():
    password = request.args.get('password')
    key = request.args.get('key')
    
    # Get the client's IP address
    client_ip = request.remote_addr
    
    # Verify the password and key
    if password == hashed_password and key == secret_key:
        shutdown()
        return jsonify({"message": f"Shutdown started from IP: {client_ip}!"}), 200
    else:
        return jsonify({"ERROR": "Either the password or key is wrong."}), 403

# Start the app
if __name__ == '__main__':
    # Get the public IP address dynamically
    public_ip = get_public_ip()
    
    # Display the running server message with dynamic public IP
    print(f"Running the server on http://{public_ip}:5000/")
    print(f"To remote shutdown from your phone or another device, go to: http://{public_ip}:5000/shutdown?password={hashed_password}&key={secret_key}")
    
    app.run(host='0.0.0.0', port=5000)
