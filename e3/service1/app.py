import subprocess
from flask import Flask, jsonify
import socket
import psutil
import time
import requests


app = Flask(__name__)

@app.route('/', methods=['GET'])
def respond():
    ip_address = socket.gethostbyname(socket.gethostname()) 

    ps = subprocess.check_output(['ps', '-aux'])
    df = subprocess.check_output(['df'])
    start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(psutil.boot_time()))

    s2_response = requests.get('http://service2:5000').json()


    response = {"service1": {
        "ip_address": str(ip_address),
        "running_processes": str(ps),
        "disk_space": str(df),
        "start_time": str(start_time)
    },
    "service2": s2_response
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)