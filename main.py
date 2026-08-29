"""
NetForge Enterprise Application Entry Point
Executable CLI and simulation engine launcher.
"""

import sys
import os
import argparse

sys.path.insert(0, os.path.dirname(__file__))

from netforge.core.buffer import RingBufferComponent_1
from netforge.protocols.ethernet import EthernetFrameComponent_1
from netforge.proxy.load_balancer import LoadBalancerComponent_1
from netforge.ui.dashboard_server import start_server

def main():
    parser = argparse.ArgumentParser(description="NetForge Enterprise Networking Application")
    parser.add_argument("--mode", choices=["server", "benchmark", "verify"], default="server", help="Mode to execute")
    parser.add_argument("--port", type=int, default=8080, help="Port for web dashboard (default 8080)")
    args = parser.parse_args()

    print("=" * 65)
    print("         NETFORGE ENTERPRISE NETWORKING APPLICATION             ")
    print("=" * 65)

    if args.mode == "server":
        print(f"Starting NetForge Engine & Web Telemetry Server on port {args.port}...")
        start_server(args.port)
    elif args.mode == "benchmark":
        print("Running NetForge benchmark...")
        from scripts.benchmark_networking import run_benchmark
        run_benchmark()
    elif args.mode == "verify":
        print("Running NetForge LOC & Test verifier...")
        from scripts.verify_loc import count_lines
        count_lines(os.path.dirname(__file__))

if __name__ == "__main__":
    main()
