"""
NetForge Web Dashboard HTTP Server
Serves the dark-mode web telemetry dashboard on localhost.
"""

import http.server
import socketserver
import os
import sys
import argparse

PORT = 8080

class NetForgeDashboardHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP handler serving the NetForge Web Dashboard."""
    
    def do_GET(self):
        ui_dir = os.path.abspath(os.path.dirname(__file__))
        if self.path in ("/", "/index.html", "/dashboard"):
            dashboard_file = os.path.join(ui_dir, "web_dashboard.html")
            try:
                with open(dashboard_file, "rb") as f:
                    content = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(content)))
                self.end_headers()
                self.wfile.write(content)
                return
            except Exception as e:
                self.send_error(500, f"Failed to load dashboard: {e}")
                return
        
        return super().do_GET()

def start_server(port=PORT):
    ui_dir = os.path.abspath(os.path.dirname(__file__))
    os.chdir(ui_dir)
    
    with socketserver.TCPServer(("0.0.0.0", port), NetForgeDashboardHandler) as httpd:
        print("=" * 65)
        print(f"      NETFORGE WEB DASHBOARD RUNNING AT: http://localhost:{port}")
        print("=" * 65)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nDashboard server stopped.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start NetForge Dashboard Server")
    parser.add_argument("--port", type=int, default=8080, help="Port to listen on (default 8080)")
    args = parser.parse_args()
    start_server(args.port)
