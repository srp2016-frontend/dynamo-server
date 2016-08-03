from http.server import SimpleHTTPRequestHandler
from data_manager import DataManager
import json
manager = DataManager()

class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['content-length'])
        data_string = str(self.rfile.read(length))[2:-1].split(":")
            dataset = data_string[0]
        frame = int(data_string[1])
        response = json.dumps(manager.get(dataset, frame))
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Content-length',str(len(response)))
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))
        
