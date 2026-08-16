import socket
import time

SERVER_IP = "tonor.bedrock.minekeep.gg"
SERVER_PORT = 25565

def ping_server():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((SERVER_IP, SERVER_PORT))
        s.close()
        print("Server is alive and pinged successfully!")
    except Exception as e:
        print(f"Ping failed: {e}")

if __name__ == "__main__":
    ping_server()
