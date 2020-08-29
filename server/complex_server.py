import socket
import select
import pylogging
import os


# Logs Dir Absolute Path
logs_path = os.path.dirname(os.path.abspath(__file__)) + '/logs/'
# Create Logger Instance
logger = pylogging.PyLogging(LOG_FILE_PATH = logs_path)

hoste = ''
port = 12800

main_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_connection.bind((hoste, port))
main_connection.listen(5)
print("The server is listening in the port {}".format(port))

cliets_answer = open('courses', "w") # Crash the content of the file if it already exists
cliets_answer.close()

server_launch = True
connected_clients = []
while server_launch:
    connection_requests, wlist, xlist = select.select([main_connection], [], [], 0.05) 

    for connection in connection_requests: 
        connection_with_client, info_connection = connection.accept()
        connected_clients.append(connection_with_client)
    
    clients_to_read = []

    try:
        clients_to_read, wlist, xlist = select.select(connected_clients, [], [], 0.05)
    except select.error:
        pass
    else:
        for client in clients_to_read:
            msg_received = client.recv(1024)
            msg_received = msg_received.decode()
            
            cliets_answer = open('courses', "a")
            cliets_answer.write("> {}\n".format(msg_received))
            
            print("Received: {}".format(msg_received))
            client.send(b"5/5")
            if msg_received == "fin":
                server_launch = False

print("Closing the connections")
for client in connected_clients:
    client.close()

cliets_answer.close()

main_connection.close()



