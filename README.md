# README: Project practise_programming_python_projects

## Prerequisites

- Python 3.x
- `pip` (Python package installer)

## Installation

The project uses `uv` for fast Python package management. The Makefile will automatically install `uv` if it's not already available on your system.

### Quick Start

1. Install dependencies:
   ```bash
   make install
   ```

2. Compile requirements (if you modify `requirements.in`):
   ```bash
   make compile
   ```

### Manual Installation

If you prefer to install `uv` manually:

```bash
pip install uv
```

Then proceed with `make install` or `make compile` as needed.

## Available Make Targets

- `make bootstrap` - Install `uv` if not already available
- `make compile` - Compile `requirements.in` to `requirements.txt`
- `make install` - Install all project dependencies
