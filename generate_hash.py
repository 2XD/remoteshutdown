import hashlib
import secrets
import socket

# Get the user's local IP address
def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

# Ask user for a password
password = input("Enter a secure password (any length): ")

# Hash the password and limit to 8 characters
hashed_password = hashlib.sha256(password.encode()).hexdigest()[:8]
print(f"Your hashed password: {hashed_password}")

# Generate a random 8-character secret key
secret_key = secrets.token_hex(4)  # 8 characters long
print(f"Your secret key: {secret_key}")

# Save to .env file
with open(".env", "w") as env_file:
    env_file.write(f"HASHED_PASSWORD={hashed_password}\n")
    env_file.write(f"SECRET_KEY={secret_key}\n")

# Get the user's local IP address
ip_address = get_local_ip()

# Display the shutdown link
shutdown_link = f"http://{ip_address}:5000/shutdown?password={hashed_password}&key={secret_key}"
print("Hashed password and secret key saved to .env.")
print(f"To remote shutdown from your phone, run app.py and use this link: {shutdown_link}")
