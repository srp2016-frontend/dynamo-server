from http.server import SimpleHTTPRequestHandler
from data_manager import DataManager
manager = DataManager()

class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['content-length'])
        data_string = self.rfile.read(length)
        frame = int(data_string)
        response = manager.get(frame)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Content-length',str(len(response)))
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))
        