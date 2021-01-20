# Download packages and pip and py
curl "https://bootstrap.pypa.io/get-pip.py" -o pip.py
python pip.py
# Install packages
python -m pip install -r requirements.txt
python client.py