import hashlib
import secrets
import socket

# Get the user's IP address
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # Try connecting to an address (Google DNS server)
        s.connect(('8.8.8.8', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'  # Default to localhost if no network connection is available
    finally:
        s.close()
    return ip

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

# Get the user's IP address
ip_address = get_ip()

# Display the shutdown link
shutdown_link = f"http://{ip_address}:5000/shutdown?password={hashed_password}&key={secret_key}"
print("Hashed password and secret key saved to .env.")
print(f"To remote shutdown from your phone, run app.py and use this link: {shutdown_link}")
