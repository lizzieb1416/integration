import socket

hoste = ''
port = 12800

main_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_connection.bind((hoste, port))
main_connection.listen(5)
print("The server is listening in the port {}".format(port))

connection_with_client, info_connection = main_connection.accept()

msg_received = b""
while msg_received != b"fin":
    msg_received = connection_with_client.recv(1024)
    print(msg_received.decode())
    connection_with_client.send(b"5 / 5")

print("Closing the connection")
print(info_connection)

connection_with_client.close()
main_connection.close()


