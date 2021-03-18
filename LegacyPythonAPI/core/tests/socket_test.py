import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 8052))

client.send(b"hello server")

while True:
  try:
    server_msg = client.recv(1024)
    print(server_msg);
  except KeyboardInterrupt:
    client.close()
    print("Disconnected")