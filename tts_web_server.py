#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'''
            <html>
            <head>
                <title>ESP32 TTS</title>
            </head>
            <body>
                <h1>ESP32 Text-to-Speech</h1>
                <form method="POST">
                    <textarea name="text" rows="10" cols="50"></textarea><br><br>
                    <input type="submit" value="Speak">
                </form>
            </body>
            </html>
        ''')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        text = post_data.decode('utf-8').split('=')[1]
        print(f"Received text to speak: {text}")
        # In a real application, this text would be sent to the TTS engine
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<html><body><h1>Text received!</h1></body></html>')

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Starting httpd on port 8000...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()


