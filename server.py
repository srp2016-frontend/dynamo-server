import os
import http.server
import socketserver
import subprocess
os.chdir("dynamo-website")

#Build the files
subprocess.Popen('while : ; do ./build.sh ; done', shell = True)

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()
