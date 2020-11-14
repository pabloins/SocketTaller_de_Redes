import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8000))

s.send(bytes("Hola desde cliente", "UTF-8"))
respuesta = s.recv(1024)

print(respuesta.decode("UTF-8"))
s.close()