# Zinnai Baby Mind AI - Makefile
# Usage: make <command>

.PHONY: help install run demo dashboard test clean

help:
	@echo "Zinnai Baby Mind AI - Available commands:"
	@echo "  make install   - Install dependencies"
	@echo "  make run       - Run main baby mind loop"
	@echo "  make demo      - Run interactive console chat"
	@echo "  make telemetry - Run live telemetry simulator (Azure Kronos)"
	@echo "  make dashboard - Start web dashboard (Flask)"
	@echo "  make test      - Run unit tests with pytest"
	@echo "  make clean     - Remove cache and temporary files"

install:
	pip install -r requirements.txt

run:
	python zinnai_baby_mind.py

demo:
	python examples/demo_console.py

telemetry:
	python examples/live_telemetry_sim.py

dashboard:
	python web/app.py

test:
	pytest tests/ -v

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .coverage htmlcov
