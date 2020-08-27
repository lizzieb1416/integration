import socket

hoste = "localhost"
port = 12800 #'localhost' with change for the Raspberry IP

connection_with_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection_with_server.connect((hoste, port)) 
print("Established connection with server in port {}".format(port))

msg_to_send = b""
while msg_to_send != b"fin":
    msg_to_send = input("> ")
    msg_to_send = msg_to_send.encode()
    connection_with_server.send(msg_to_send)
    msg_received = connection_with_server.recv(1024)
    print(msg_received.decode())

print("Closing the connection")
connection_with_server.close()


connection_with_server.close()

