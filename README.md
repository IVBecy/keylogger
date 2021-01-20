# Keylogger

### This script was made as a proof of concept, I have no sinister intentions with it

# How it works:
On the host machine, `server.py` needs to be run. After that, put and run `client.py` or `run.sh` on the
"victims" machine. Note that `client.py` will only run if python and all packages are installed. If not,
run `run.sh`, that will install pip and all the packages that will be needed, keep in mind that python itself still
needs to be installed. 

# Libraries:
- keyboard
- socket.py
- sys
- to install all packages, just run `pip install -r requirements.txt`
