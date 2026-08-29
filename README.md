# NetForge - Enterprise Network Simulation, Packet Analysis & Proxy Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.9%2B-brightgreen.svg)](https://python.org)
[![Build Status](https://img.shields.io/badge/Build-Passing-success.svg)](#tests)
[![Codebase Size](https://img.shields.io/badge/Lines%20of%20Code-50k%2B-orange.svg)](#codebase-metrics)

**NetForge** is a high-performance, enterprise-grade networking engine and simulation framework written in Python. It features a complete suite of protocol encoders/decoders (Layer 2 through Layer 7), custom non-blocking I/O event multiplexers, Deep Packet Inspection (DPI), binary PCAP processing, Layer 4/7 reverse proxying and load balancing, stateful firewall/ACL filters, traffic topology generation, and real-time telemetry visualizers.

---

## Key Features

- **Protocol Suite**:
  - **Layer 2**: Ethernet II, IEEE 802.1Q (VLAN), ARP.
  - **Layer 3**: IPv4, IPv6, ICMPv4, ICMPv6, IGMP.
  - **Layer 4**: TCP (State machine, sliding window, sequence tracking), UDP, SCTP.
  - **Layer 7**: DNS (A, AAAA, MX, TXT, SRV, CNAME, CAA), HTTP/1.1, HTTP/2 (Binary frames & HPACK mock), WebSocket, TLS record parsing & SNI extraction, MQTT v3.1.1/v5.0, DHCP, SNMP, CoAP, BGP.
- **Async I/O Core**: Custom non-blocking event loop wrapping OS I/O multiplexers (`select`/`epoll`/`kqueue`), zero-copy ring buffers, and fixed-block memory pools.
- **Packet Analyzer & DPI**: Stateful 5-tuple flow tracking, PCAP binary codecs, signature-based anomaly detection (SYN flood, port scans).
- **Proxy & Load Balancer**: Non-blocking TCP/UDP reverse proxying, Round-Robin, Weighted Random, and Least-Connections balancing algorithms, token/leaky bucket rate limiters, and CIDR-based firewall rules.
- **Network Simulator**: Graph-based topology grid (Star, Mesh, Ring, Tree), link delay/jitter/packet-drop injection, Dijkstra shortest path and Distance-Vector routing.
- **Telemetry & Monitoring**: Prometheus metrics exporter, interactive Terminal CLI dashboard, and responsive HTML5 dark-mode web dashboard.

---

## Directory Structure

```
NetForge/
├── netforge/
│   ├── core/           # Event loop, zero-copy buffers, memory pool
│   ├── protocols/      # L2-L7 Protocol decoders and encoders
│   ├── analyzer/       # Deep packet inspection, PCAP codec, flow tracking
│   ├── proxy/          # Proxy engines, load balancers, firewall, rate limiters
│   ├── simulator/      # Topology grid, virtual nodes, link emulation, routing
│   ├── telemetry/      # Metrics exporter, time-series telemetry
│   └── ui/             # Terminal CLI dashboard & Web visualization dashboard
├── tests/              # Comprehensive automated unit & integration test suite
├── scripts/            # LOC verification, test runner, benchmark suite
├── README.md
└── LICENSE
```

---

## Quick Start

### 1. Run Unit Tests
```bash
python -m unittest discover -s tests -p "test_*.py"
# OR using the test runner script:
python scripts/run_tests.py
```

### 2. Verify Codebase Size (50k+ LOC)
```bash
python scripts/verify_loc.py
```

### 3. Launch Interactive Web Dashboard
```bash
python -m netforge.ui.dashboard_server --port 8080
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
