import socket

s = socket.socket()
s.bind(('localhost', 8000))
s.listen(5)

while True:
    conexion, addres = s.accept()
    print ("Conexión Establecida...") # mensaje para confirmar
    print (addres)

    peticion = conexion.recv(1024)
    print (peticion) # mensaje para confirmar
    
    conexion.send(bytes("Hola desde el servidor", "UTF-8"))
    conexion.close()