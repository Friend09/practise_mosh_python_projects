.PHONY: init sync add remove lock compile install run test clean help

help:
	@echo "Available targets:"
	@echo "  make init      - Initialize a new uv project"
	@echo "  make sync      - Sync dependencies from uv.lock"
	@echo "  make add PKG=  - Add a dependency (e.g. make add PKG=requests)"
	@echo "  make remove PKG= - Remove a dependency (e.g. make remove PKG=requests)"
	@echo "  make lock      - Update uv.lock without installing"
	@echo "  make compile   - Compile requirements.in to requirements.txt"
	@echo "  make install   - Install from requirements.txt"
	@echo "  make run CMD=   - Run a command in the uv env (e.g. make run CMD=python main.py)"
	@echo "  make test      - Run tests with uv"
	@echo "  make clean     - Remove caches and build artifacts"

init:
	uv init

sync:
	uv sync

add:
	uv add $(PKG)

remove:
	uv remove $(PKG)

lock:
	uv lock

compile:
	uv pip compile requirements.in -o requirements.txt

install:
	uv pip install --upgrade pip && \
	uv pip install -r requirements.txt

run:
	uv run $(CMD)

test:
	uv run pytest

clean:
	rm -rf .venv .pytest_cache .ruff_cache .mypy_cache __pycache__ *.egg-info dist build
