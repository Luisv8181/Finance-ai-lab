import http.server
import socketserver
import os
from utils.logger import setup_logger

logger = setup_logger("server")

PORT = 8080
DIRECTORY = "."

# Files and directories that should NEVER be served
BLOCKED_PATHS = ['.env', 'api-key', '.gitignore', 'logs', '__pycache__', 
                 'utils', 'collectors', 'delivery', '.git']

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def do_GET(self):
        # Security: block access to sensitive files/directories
        clean_path = self.path.strip('/').split('?')[0]
        for blocked in BLOCKED_PATHS:
            if clean_path == blocked or clean_path.startswith(blocked + '/'):
                logger.warning(f"BLOCKED access attempt: {self.path}")
                self.send_error(403, "Access Denied")
                return
        
        if self.path == '/':
            self.path = '/dashboard/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

def start_server():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        logger.info(f"Dashboard serving at http://localhost:{PORT}")
        print(f"\n[!!!] DASHBOARD READY: http://localhost:{PORT}")
        print("Press Ctrl+C to stop the server.\n")
        httpd.serve_forever()

if __name__ == "__main__":
    start_server()
