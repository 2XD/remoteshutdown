# Lightweight Remote Shutdown using Flask and NGROK

A secure API to remotely shut down your PC using Flask, featuring brute-force protection, password hashing, and more.

## Setup Instructions

### 1. Install Dependencies
Make sure you have Python installed, then install the required dependencies:
```sh
pip install -r requirements.txt
```

### 2. Generate Your Hashed Password and Secret Key
Run the `generate_hash.py` script to create a hashed password and secret key, which will be saved in the `.env` file.
```sh
python generate_hash.py
```
You can generate a new key each time you use it or just once, depending on your preference.

## Setting Up NGROK

### 1. Download and Install NGROK
Go to [NGROK's official website](https://ngrok.com/) and sign up for an account.

### 2. Get Your Authentication Key
After signing up, go to your NGROK dashboard and find your authentication token.

### 3. Set Up NGROK in Command Line
Run the following command in your terminal or command prompt, replacing `YOUR_AUTH_TOKEN` with your actual token:
```sh
ngrok authtoken YOUR_AUTH_TOKEN
```

### 4. Start NGROK Tunnel
Run NGROK to expose your Flask app to the internet:
```sh
ngrok http 5000
```
Copy the public URL provided by NGROK, as you'll use this to access the remote shutdown page.

## Running the Server
Once NGROK is set up, start the Flask server:
```sh
python app.py
```
The public NGROK URL will be printed in the terminal. Use it to access your shutdown page.

## How to Use From Phone
Now the server is accessible from your phone or any other device. The URL will be printed in the terminal upon running `app.py`, or you can access it directly using:
```
https://your-ngrok-url/shutdown?token=YOUR_GENERATED_JWT_TOKEN
```
Ensure you keep your token secure, as it is required for authentication.

