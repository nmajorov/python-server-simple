#!/usr/bin/env python

# simple rest echo server  

import http.server
import socketserver
from io import BytesIO
import os

PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):

    def do_POST(self):
        self.do_GET()

    def do_GET(self):
        """Serve a GET request."""

        hostname = os.uname()[1]
        try:
            f = BytesIO()
            f.write(b'')
            response = "{{\"echo\":\"form server {}\"}}".format(hostname)
            f.write(bytes(response, 'utf-8'))
            length = f.tell()
            f.seek(0)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Content-Length", str(length))
            self.end_headers()
            if f:
                self.copyfile(f, self.wfile)
                
        finally:
            f.close()

#MyHandler = Handler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
