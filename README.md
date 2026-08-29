# NetForge - Enterprise Network Simulation, Packet Analysis & Proxy Framework

[![Python Version](https://img.shields.io/badge/Python-3.9%2B-brightgreen.svg)](https://python.org)
[![Build Status](https://img.shields.io/badge/Build-Passing-success.svg)](#tests)
[![Codebase Size](https://img.shields.io/badge/Lines%20of%20Code-50k%2B-orange.svg)](#codebase-metrics)

**NetForge** is a high-performance, enterprise-grade networking engine and simulation framework written in Python. It features a complete suite of protocol encoders/decoders (Layer 2 through Layer 7), custom non-blocking I/O event multiplexers, Deep Packet Inspection (DPI), binary PCAP processing, Layer 4/7 reverse proxying and load balancing, stateful firewall/ACL filters, traffic topology generation, and real-time telemetry visualizers.

---

## Installation

### Prerequisites
- Python 3.9+ installed on your system.
- Docker (optional, for containerized deployments).

### Step-by-Step Installation
1. **Clone or Extract the Repository**:
   ```bash
   git clone https://github.com/B-Bhanu123/NetForge.git
   cd NetForge
   ```

2. **Set up Virtual Environment**:
   ```bash
   python -m venv venv
   # On Linux/macOS:
   source venv/bin/activate
   # On Windows PowerShell:
   .\venv\Scripts\Activate.ps1
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   # OR using setup.py:
   pip install -e .
   ```

---

## Dependencies

The project requirements and lockfiles are documented in:
- `requirements.txt`
- `pyproject.toml`
- `poetry.lock`
- `setup.py`

Key Python libraries used:
- `urllib3`: HTTP client connection pooling.
- `requests`: REST API data fetching.
- `prometheus-client`: Telemetry & metrics export format.
- `pytest`: Testing & verification.

---

## Build

### Local Package Build
```bash
python setup.py build
# OR using Makefile:
make build
```

### Docker Container Build
```bash
docker build -t netforge:latest .
```

---

## Run

### Option 1: Run via Main Entry Point (`main.py`)
```bash
# Launch server mode (Web Telemetry Dashboard on http://localhost:8080)
python main.py --mode server --port 8080

# Launch benchmark mode
python main.py --mode benchmark

# Verify codebase size (50k+ LOC)
python main.py --mode verify
```

### Option 2: Run via Web App Entry Point (`app.py`)
```bash
python app.py
```

### Option 3: Run via Docker
```bash
docker run -d -p 8080:8080 --name netforge-app netforge:latest
```

### Option 4: Run via Makefile
```bash
make run
```

---

## Usage

### Interactive Web Dashboard
Once running, open **[http://localhost:8080](http://localhost:8080)** in your browser to inspect live throughput graphs, active 5-tuple socket connection tables, and animated SVG network mesh topologies.

### Running Automated Test Suite
```bash
python scripts/run_tests.py
# OR using unittest:
python -m unittest discover -s tests -p "test_*.py"
# OR using Makefile:
make test
```

### Verification & Benchmarking
```bash
python scripts/verify_loc.py
python scripts/benchmark_networking.py
```

---

## Directory Structure

```
NetForge/
├── netforge/           # Core library package (Core, Protocols, Proxy, Simulator, Telemetry, UI)
├── tests/              # 8 automated test suites (500+ unit test assertions)
├── scripts/            # LOC verifier, test runner, benchmark runner
├── main.py             # CLI & application entry point
├── app.py              # Web application entry point
├── Dockerfile          # Docker container manifest
├── Makefile            # Automation makefile
├── setup.py            # Package installation script
├── requirements.txt    # Dependency manifest
├── pyproject.toml      # Standard build configuration
├── poetry.lock         # Dependency lockfile
└── README.md           # Documentation
```
