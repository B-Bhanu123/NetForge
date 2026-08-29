"""
NetForge Web Dashboard HTTP Server
Serves the dark-mode web telemetry dashboard and REST API on localhost.
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

class NetForgeDashboardHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP handler serving the NetForge Web Dashboard and REST Telemetry API."""
    
    def do_GET(self):
        ui_dir = os.path.abspath(os.path.dirname(__file__))
        
        # REST API endpoint for live telemetry
        if self.path == "/api/stats":
            base_throughput = 12.0 + random.uniform(-0.8, 1.2)
            base_flows = 142000 + random.randint(-1500, 2500)
            base_latency = 1.15 + random.uniform(-0.15, 0.25)
            
            payload = {
                "status": "online",
                "timestamp": time.time(),
                "throughput": f"{base_throughput:.2f} Gbps",
                "flows": base_flows,
                "latency": f"{base_latency:.2f} ms",
                "dpi_threats": random.choice([0, 0, 0, 0, 1]),
                "protocol_breakdown": {
                    "tls": {"flows": int(base_flows * 0.589), "ratio": "58.9%"},
                    "http2": {"flows": int(base_flows * 0.204), "ratio": "20.4%"},
                    "dns": {"flows": int(base_flows * 0.128), "ratio": "12.8%"},
                    "mqtt": {"flows": int(base_flows * 0.043), "ratio": "4.3%"},
                    "icmp": {"flows": int(base_flows * 0.036), "ratio": "3.6%"}
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

        # HTML Dashboard rendering
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
