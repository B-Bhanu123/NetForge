.PHONY: install build run test clean verify benchmark

install:
	python -m pip install -r requirements.txt

build:
	docker build -t netforge:latest .

run:
	python main.py --mode server --port 8080

test:
	python scripts/run_tests.py

verify:
	python scripts/verify_loc.py

benchmark:
	python scripts/benchmark_networking.py

clean:
	rm -rf __pycache__ .pytest_cache *.egg-info build dist
