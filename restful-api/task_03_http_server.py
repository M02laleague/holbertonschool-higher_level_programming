#!/usr/bin/python3
"""import http.server & import json module"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPI(BaseHTTPRequestHandler):
    """Definition of the SimpleAPI class"""

    def do_GET(self):
        """manage GET requests"""

        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            """return ok if is good with code(200)"""
            self.send_header("Content-type", 'application/json')
            self.end_headers()
            """Spécification du type de contenu (JSON)"""

            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            """Sending JSON data encoded in UTF-8"""
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", 'application/json')
            self.end_headers()

            info_data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            self.wfile.write(json.dumps(info_data).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SimpleAPI)
    print("Serving port 8000...")
    httpd.serve_forever()