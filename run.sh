# Download packages and pip
curl "https://bootstrap.pypa.io/get-pip.py" -o pip.py
python pip.py
python -m pip install -r requirements.txt
python client.py