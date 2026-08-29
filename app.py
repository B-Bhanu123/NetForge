"""
NetForge Web Application Entry Point
Launches the interactive telemetry dashboard web app.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from netforge.ui.dashboard_server import start_server

def run_app():
    port = int(os.environ.get("PORT", 8080))
    print(f"Launching NetForge Web App on http://localhost:{port}")
    start_server(port)

if __name__ == "__main__":
    run_app()
