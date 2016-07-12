import os
import http.server
import socketserver
import subprocess
import threading
import time
from request_handler import Handler
os.chdir("dynamo-website")

if not os.path.exists("node_modules"):
    subprocess.run(["npm install"])
build = True
#A function to build the TS files in a loop 
def continuous_build():
    while build:
        subprocess.run(['node_modules/typescript/bin/tsc', 'src/main.ts', '--outFile', 'bin/script.js'])
        time.sleep(0.05)
#Build the files
threading.Thread(target = continuous_build).start()

PORT = 8000

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
try:
    httpd.serve_forever()
except:
    httpd.server_close()
build = False