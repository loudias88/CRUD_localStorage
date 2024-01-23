from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class MyHttpRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

# Set the directory where the HTML file is located
os.chdir(os.path.expanduser('~/Área de Trabalho/Projects/python-lab/CRUD'))

# Server settings
server_address = ('localhost', 8000)
httpd = HTTPServer(server_address, MyHttpRequestHandler)

# Run the server
print("Server running on port 8000...")
httpd.serve_forever()
#
