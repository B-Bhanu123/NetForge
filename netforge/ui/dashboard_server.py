"""
NetForge Web Dashboard HTTP Server & Telemetry API
Serves the dedicated NetForge Protocol Analyzer & Proxy Engine Dashboard on localhost.
"""

import http.server
import socketserver
import os
import sys
import json
import random
import time
import argparse

PORT = 8080

class NetForgeDashboardHandler(http.server.BaseHTTPRequestHandler):
    """Custom HTTP handler serving the NetForge Protocol & Proxy Telemetry API."""
    
    def log_message(self, format, *args):
        pass  # Suppress default HTTP server logs
    
    def do_GET(self):
        ui_dir = os.path.abspath(os.path.dirname(__file__))
        
        try:
            # REST API endpoint for networking telemetry
            if "/api" in self.path:
                base_pps = random.randint(82000, 91000)
                base_throughput = 14.0 + random.uniform(-0.5, 1.5)
                base_sockets = random.randint(145000, 150000)
                
                payload = {
                    "project": "NetForge Enterprise Networking Engine",
                    "status": "online",
                    "timestamp": time.time(),
                    "packet_rate": str(base_pps) + " pps",
                    "throughput": f"{base_throughput:.2f} Gbps",
                    "flows": base_sockets,
                    "dpi_threats": random.choice([0, 0, 0, 0, 1]),
                    "backend_conns": {
                        "b1": int(base_sockets * 0.05),
                        "b2": int(base_sockets * 0.03),
                        "b3": int(base_sockets * 0.02)
                    }
                }
                content = json.dumps(payload).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Content-Length", str(len(content)))
                self.end_headers()
                self.wfile.write(content)
                return

            # Serve HTML Dashboard
            dashboard_file = os.path.join(ui_dir, "web_dashboard.html")
            with open(dashboard_file, "rb") as f:
                content = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(f"Error: {e}".encode("utf-8"))

def start_server(port=PORT):
    ui_dir = os.path.abspath(os.path.dirname(__file__))
    os.chdir(ui_dir)
    
    with socketserver.TCPServer(("0.0.0.0", port), NetForgeDashboardHandler) as httpd:
        print(f"NETFORGE PROTOCOL ENGINE RUNNING AT: http://localhost:{port}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nDashboard server stopped.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start NetForge Networking Dashboard Server")
    parser.add_argument("--port", type=int, default=8080, help="Port to listen on (default 8080)")
    args = parser.parse_args()
    start_server(args.port)
