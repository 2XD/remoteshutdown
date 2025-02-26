import os
import socket
import psutil
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment and hashed secrets
load_dotenv()
app = Flask(__name__)
secret_key = os.getenv('SECRET_KEY')
hashed_password = os.getenv('HASHED_PASSWORD')


# Define the shutdown function
def shutdown():
    if psutil.WINDOWS:
        os.system("shutdown /s /f /t 1")
    else:
        os.system("shutdown now")


# Get the local IP address dynamically
def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip


# Route for shutdown
@app.route('/shutdown', methods=['GET'])
def remote_shutdown():
    password = request.args.get('password')
    key = request.args.get('key')
    
    # Verify the password and key
    if password == hashed_password and key == secret_key:
        shutdown()
        return jsonify({"message": "Shutdown started!"}), 200
    else:
        return jsonify({"ERROR": "Either the password or key is wrong."}), 403


# Start the app
if __name__ == '__main__':
    local_ip = get_local_ip()  # Get local IP address
    print(f"Running the server on http://{local_ip}:5000/")
    print(f"To remote shutdown from your phone or another device, go to: http://{local_ip}:5000/shutdown?password={hashed_password}&key={secret_key}")
    app.run(host='0.0.0.0', port=5000)
