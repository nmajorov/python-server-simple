from unittest import TestCase

import threading
import requests
import server

from socketserver import  ThreadingMixIn
from http.server import HTTPServer



class TestHandler(TestCase):
    
    #web= threading.Thread(target=server.main)
    web = server.ThreadingHTTPServer(("localhost",server.PORT), server.Handler)

    def test_get(self):
        self.server_thread = threading.Thread(target=self.web.serve_forever)
        self.server_thread.start()
        response = requests.get('http://localhost:8080')
        self.assertTrue(response.status_code == 200)
        print("******* test done trying to stop server")

    def tearDown(self):
        self.web.shutdown()
