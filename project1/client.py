# client.py
import socket
import json
import random


def generate_name():
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    
    name = ""
    for _ in range(1):
        name += random.choice(consonants)
        name += random.choice(vowels)
    
    return name.capitalize()



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 9999))



# client.sendall(b"Hello from client!")


# print("Server says:", response.decode())

statusList = {
    "100" : "INFO",
    "200" : "WARNING",
    "300" : "ERROR"
}

def requestLoops(dict) :
    loops = 0
    values = list(dict.values())
    keys = list(dict.keys())


    while loops <= 120 :
        i = random.randint(0, 2)
        name = generate_name()
        
        info = {
            keys[i] : values[i],
            "name" : name
        }
        jsonInfo = json.dumps(info).encode("utf-8")
        client.sendall(jsonInfo)
        # response = client.recv(1024)

        loops += 1   
    
    client.close()



requestLoops(statusList)





# make a 120 request loops
# make a random status 
# and sent them into server


