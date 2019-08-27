from unittest import TestCase

import threading
import requests
import server


class TestServer(TestCase):
    
    web= threading.Thread(target=server.main)
    

    def test_get(self):
        self.web.start()
        
        response = requests.get('http://localhost:8080')
        self.assertTrue(response.status_code == 200)
        print("******* test done trying to stop server")
        self.web.join() 
