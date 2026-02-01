# server.py
import socket
import json




def connection() :
        
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 9999))
    server.listen(1)
    print("Server listening...")

    conn, addr = server.accept()
    print("Connected by", addr)
    
    data = b""
    while True:
        part = conn.recv(1024)
        if not part:
            break
        data += part

    try:
        decoded = json.loads(data.decode("utf-8"))
        print("Received:", decoded)
    except json.JSONDecodeError:
        print("Failed to decode JSON:", data)

    conn.sendall(b"Hello from server!")
    conn.close()



connection()


