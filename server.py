import os
import http.server
import socketserver
import subprocess
import threading
import time
os.chdir("dynamo-website")

if not os.path.exists("node_modules"):
    subprocess.run(["npm install"])

#A function to build the TS files in a loop 
def continuous_build():
    while True:
        subprocess.run(['node_modules/typescript/bin/tsc', 'src/main.ts', '--outFile', 'bin/script.js'])
        time.sleep(0.05)
#Build the files
threading.Thread(target = continuous_build).start()

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()
