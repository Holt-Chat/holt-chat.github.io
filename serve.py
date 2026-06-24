import os, sys
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])) if getattr(sys, "frozen", False) else os.path.dirname(os.path.abspath(__file__)))
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
PORT=int(os.environ.get("PORT", 3317))
HOST=os.environ.get("HOST", "0.0.0.0")

class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        super().end_headers()
    def log_message(self, fmt, *args): print(f"[holt-site] {self.address_string()} {fmt%args}")

if __name__=="__main__":
    with ThreadingHTTPServer((HOST, PORT), Handler) as httpd:
        print(f"Holt marketing site serving on http://{HOST}:{PORT}")
        try: httpd.serve_forever()
        except KeyboardInterrupt: print("\nstopped")
