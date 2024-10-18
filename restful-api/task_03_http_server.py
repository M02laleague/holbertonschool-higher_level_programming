#!/usr/bin/python3

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# Define the handler class for processing HTTP requests


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    # Handle GET requests
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)  # OK status
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)  # OK status
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            # Convert dictionary to JSON and write the response
            self.wfile.write(json.dumps(response).encode('utf-8'))

        elif self.path == "/status":
            self.send_response(200)  # OK status
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"status": "OK"}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        
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
            # Handle undefined endpoints with 404 Not Found
            self.send_response(404)  # Not Found status
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(response).encode('utf-8'))

# Function to start the server


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}")
    httpd.serve_forever()


# Entry point for the script
if __name__ == "__main__":
    run()
