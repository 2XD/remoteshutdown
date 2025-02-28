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

# Generate a random 8-character secret key
secret_key = secrets.token_hex(4)  # 8 characters long
print(f"Your secret key: {secret_key}")

# Save to .env file
with open(".env", "w") as env_file:
    env_file.write(f"SECRET_KEY={secret_key}\n")

# Get the user's IP address

# Display the shutdown link
print("Secret key saved to .env.")
print(f"To remote shutdown from your phone, run app.py")
