import os
import http.server
import socketserver
import subprocess
import threading
import time
import request_handler
from request_handler import Handler
import data_manager

os.chdir("dynamo-website")


if not os.path.exists("node_modules"):
    os.system("npm install")
build = True
#A function to build the TS files in a loop 
def continuous_build():
    while build:
        if os.name == 'nt':
            os.system("node node_modules/typescript/lib/tsc.js src/main.ts --outFile bin/script.js")
        else:
            subprocess.run(['node_modules/typescript/bin/tsc', 'src/main.ts', '--outFile', 'bin/script.js'])
        print("Build completed")
        time.sleep(0.5)

#Build the files
threading.Thread(target = continuous_build).start()

PORT = 8000

httpd = socketserver.TCPServer(("", PORT), Handler)
#A thread for user input commands
def commands():
    global build
    while build:
        user = input()
        if user == "quit":
            httpd.shutdown()
            build = False
        elif user == "reload":
            request_handler.manager = data_manager.DataManager()
threading.Thread(target = commands).start()

print("serving at port", PORT)
try:
    httpd.serve_forever()
except:
    httpd.server_close()
build = False
