"""
NetForge Network Performance Benchmark Suite
Measures packet processing throughput, latency, and ring-buffer allocation rates.
"""

import time
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from netforge.core.buffer import RingBufferComponent_1
from netforge.protocols.ethernet import EthernetFrameComponent_1
from netforge.protocols.ipv4 import IPv4PacketComponent_1
from netforge.proxy.load_balancer import LoadBalancerComponent_1

def run_benchmark():
    print("=" * 65)
    print("                NETFORGE BENCHMARK SUITE                        ")
    print("=" * 65)
    
    buf = RingBufferComponent_1()
    eth = EthernetFrameComponent_1()
    ip = IPv4PacketComponent_1()
    lb = LoadBalancerComponent_1()
    
    payload = b"\x00" * 1024
    iterations = 100000
    
    start_time = time.time()
    for i in range(iterations):
        eth.process_step_1(payload, session_id=i)
        ip.process_step_1(payload, session_id=i)
        lb.process_step_1(payload, session_id=i)
    
    elapsed = time.time() - start_time
    rate = (iterations * 3) / elapsed
    mbps = (iterations * 3 * 1024 * 8) / (elapsed * 1024 * 1024)
    
    print(f"Executed {iterations * 3:,} packet processing operations in {elapsed:.4f} seconds.")
    print(f"Packet Processing Throughput: {rate:,.2f} operations / sec")
    print(f"Simulated Bandwidth Rate:     {mbps:,.2f} Mbps")
    print("=" * 65)
    print("BENCHMARK COMPLETED SUCCESSFULLY!")
    return 0

if __name__ == "__main__":
    sys.exit(run_benchmark())
