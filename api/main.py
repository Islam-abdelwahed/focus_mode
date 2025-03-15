from http.server import BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open('static/index.html', 'r') as file:
            self.wfile.write(file.read().encode())


# For Vercel deployment
def vercel_handler(request):
    handler = Handler()
    return handler
