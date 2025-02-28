import os
import jwt
from flask import Flask, request, jsonify, render_template_string
from dotenv import load_dotenv
from pyngrok import ngrok

# Load environment variables from .env
load_dotenv()

# Set up Flask app
app = Flask(__name__)

# Use the SECRET_KEY from the .env file
SECRET_KEY = os.getenv("SECRET_KEY")

# Generate a simple JWT Token
def generate_token():
    token = jwt.encode({}, SECRET_KEY, algorithm='HS256')
    return token

# Generate the token when the app starts
jwt_token = generate_token()

# Define a shutdown function to actually shut down the PC
def shutdown():
    print("Shutdown started!")  # This will print when the button is clicked
    os.system('shutdown /s /f /t 0')  # Windows command to shut down the PC

# Route for shutdown (JWT-protected)
@app.route('/shutdown', methods=['GET'])
def remote_shutdown():
    # Get token from URL
    token = request.args.get('token')

    if not token:
        return jsonify({"ERROR": "Missing token."}), 403

    try:
        # Decode and validate the token
        jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        shutdown()  # Call shutdown function
        return jsonify({"message": "Shutdown started!"}), 200
    except jwt.InvalidTokenError:
        return jsonify({"ERROR": "Invalid token."}), 403

# Route for home page with Shutdown button
@app.route('/')
def index():
    # Get token from URL query string
    token = request.args.get('token')

    # If the token is valid, enable the button, else disable it
    button_state = "enabled" if token else "disabled"
    
    # Embed HTML content with a shutdown button and the token in the URL
    html_content = f"""
    <html>
        <head>
            <title>Remote Shutdown</title>
        </head>
        <body>
            <h1>Remote Shutdown</h1>
            
            <form action="/shutdown" method="GET" id="shutdownForm">
                <input type="hidden" name="token" value="{token}"/>
                <button type="submit" id="shutdownBtn" {button_state}>Shutdown</button>
            </form>

            <script>
                // If token is missing or invalid, disable the button
                var token = "{token}";
                if (!token) {{
                    document.getElementById('shutdownBtn').disabled = true;
                    alert("Invalid or missing token! Button disabled.");
                }}
            </script>
        </body>
    </html>
    """
    return render_template_string(html_content)

# Start the app
if __name__ == '__main__':
    # Start Ngrok and get the public URL
    ngrok_tunnel = ngrok.connect(5000)
    public_url = ngrok_tunnel.public_url
    
    print("\nRemote Shutdown Server is Running!\n")
    print(f"Public Access: {public_url}/?token={jwt_token}\n")
    
    app.run(host='0.0.0.0', port=5000)
