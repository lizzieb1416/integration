import socket
import pylogging
import os

# Logs Dir Absolute Path
logs_path = os.path.dirname(os.path.abspath(__file__)) + '/logs/'
# Create Logger Instance
logger = pylogging.PyLogging(LOG_FILE_PATH = logs_path)
# Log Info Message
# logger.info("Info Message")
# # Log Warning Message
# logger.warning("Warning Message.")
# # Log Error Message
# logger.error("Error Message.")
# # Log Critical Message
# logger.critical("Critical Message.")
# Log Normal Message
logger.log("Normal Log Message.")

hoste = "192.168.1.22"
port = 12800 #'localhost' with change for the Raspberry IP

connection_with_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection_with_server.connect((hoste, port)) 
print("Established connection with server in port {}".format(port))
logger.info("Connection OK")

msg_to_send = b""
while msg_to_send != b"fin":
    msg_to_send = input("> ")
    msg_to_send = msg_to_send.encode()
    connection_with_server.send(msg_to_send)
    logger.log("Message envoyé : {}".format(msg_to_send.decode()))
    msg_received = connection_with_server.recv(1024)
    print(msg_received.decode())

print("Closing the connection")
connection_with_server.close()


connection_with_server.close()

