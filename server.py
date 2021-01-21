# Modules
import socket,sys

# Variables to be used
HOST = "0.0.0.0"
PORT = 80
BUFFER = 1024

# Waiting for connection
def listener():
  global incoming,s
  s = socket.socket()
  s.bind((HOST,PORT))
  s.listen(1)
  print(f"Listening as {HOST}:{PORT}")
  incoming,addr = s.accept()
  print(f"Connected to {addr[0]}:{addr[1]}")
  print("\nListening for keystrokes")
  
# Start listening
if __name__ == "__main__":
  listener()
  while True:
    try:
      print(incoming.recv(1024).decode())
    except KeyboardInterrupt:
      print("Exiting...")
      s.close()
      sys.exit()
    except ConnectionResetError:
      print("The connection was closed by the client")
      sys.exit()