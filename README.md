# Pyxenv 🐍 - Python Version/Environment Manager

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)


> **npx for Python** - Manage Python versions and virtual environments with ease

`Pyxenv` is a command-line tool inspired by Node.js's `npx`, designed to simplify managing multiple Python versions and virtual environments.

## Features

- **Quick version switching** - Run scripts with different Python versions
- **Automatic installation** - Downloads and installs Python versions automatically (Windows)
- **Virtual environment management** - Create and activate virtual environments easily
- **Smart detection** - Lists all available Python versions
- **Cross-platform** - Support for Windows, Linux and macOS
- **Zero configuration** - Works immediately after installation

## Installation

### Via pip (recommended)

```bash
pip install pyxenv
```

### Via GitHub

```bash
git clone https://github.com/luigicfilho/pyxenv.git
cd pyxenv
pip install -e .
```

## Quick Usage

### Run script with specific version

```bash
# Run script.py with Python 3.11
pyxenv 3.11 script.py

# With arguments
pyxenv 3.11 script.py --arg1 value1 --arg2 value2
```

### Manage Python versions

```bash
# List versions installed by pyxenv
pyxenv --list

# List all versions (including globals)
pyxenv --list-all

# Auto-install (Windows)
pyxenv 3.12 script.py  # Installs 3.12 if not exists
```

### Manage virtual environments

```bash
# Create virtual environment
pyxenv 3.11 --create-env my-project

# Create with default name (pyxenv-3.11)
pyxenv 3.11 --create-env

# Activate environment
pyxenv --activate my-project

# List environments
pyxenv --list-envs
```

## Examples

### Multi-version development

```bash
# Test your code in different versions
pyxenv 3.8 test_script.py
pyxenv 3.9 test_script.py
pyxenv 3.11 test_script.py
pyxenv 3.12 test_script.py
```

### Isolated projects

```bash
# Django project with Python 3.11
pyxenv 3.11 --create-env django-project
pyxenv --activate django-project
pip install django
django-admin startproject mysite

# FastAPI project with Python 3.12
pyxenv 3.12 --create-env fastapi-project
pyxenv --activate fastapi-project
pip install fastapi uvicorn
```

### CI/CD

```yaml
# .github/workflows/test.yml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: windows-latest
    strategy:
      matrix:
        python-version: ['3.8', '3.9', '3.10', '3.11', '3.12']
    
    steps:
      - uses: actions/checkout@v3
      - name: Install pyxenv
        run: pip install pyxenv
      - name: Run tests
        run: pyxenv ${{ matrix.python-version }} -m pytest
```

## Commands

| Command | Description |
|---------|-------------|
| `pyxenv <version> <script>` | Run script with specific version |
| `pyxenv --list` | List versions installed by pyxenv |
| `pyxenv --list-all` | List all detected versions |
| `pyxenv --create-env <name>` | Create virtual environment |
| `pyxenv --activate <name>` | Activate virtual environment |
| `pyxenv --list-envs` | List created environments |
| `pyxenv --version` | Show pyxenv version |

## Directory Structure

```
~/.pyxenv/
├── pythons/          # Installed Python versions
│   ├── 3.8.10/
│   ├── 3.11.5/
│   └── 3.12.0/
└── envs/             # Virtual environments
    ├── my-project/
    ├── django-app/
    └── pyxenv-3.11/
```

## Configuration

pyxenv works without configuration, but you can customize:

```python
# ~/.pyxenv/config.py (optional)
pyxenv_HOME = Path.home() / ".pyxenv"
PYTHON_DIR = pyxenv_HOME / "pythons"
ENV_DIR = pyxenv_HOME / "envs"
```

## Troubleshooting

### Python not found

```bash
# Check available versions
pyxenv --list-all

# Install specific version (Windows)
pyxenv 3.11 --version  # Auto-installs
```

### Virtual environment not activating

```bash
# Check if it exists
pyxenv --list-envs

# Recreate if necessary
pyxenv 3.11 --create-env env-name
```

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### Development setup

```bash
# Clone repository
git clone https://github.com/luigicfilho/pyxenv.git
cd pyxenv

# Install development dependencies
pip install -e .

# Run tests
pytest

# Check coverage
pytest --cov=pyxenv --cov-report=html
```

### Run tests

```bash
# All tests
pytest

# Specific tests
pytest tests/test_cli.py

# With verbose output
pytest -vv

# With coverage
pytest --cov=pyxenv --cov-report=term-missing
```

### Code style

```bash
# Format code
black pyxenv tests

# Sort imports
isort pyxenv tests

# Check style
flake8 pyxenv tests

# Type checking
mypy pyxenv
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Luigi C. Filho**

- Email: lcdev@lcdesenvolvimentos.com.br
- GitHub: [@luigicfilho](https://github.com/luigicfilho)

## Acknowledgments

- Inspired by Node.js's [npx](https://github.com/npm/npx)
- Python community for excellent documentation

## Project Status

- [x] Python version detection
- [x] Virtual environment management
- [x] Automatic installation (Windows)
- [ ] Automatic installation (Linux/macOS) - In development
- [ ] Download cache - Planned
- [ ] Auto-update - Planned

## Useful Links

- [Documentation](https://github.com/luigicfilho/pyxenv#readme)
- [Issues](https://github.com/luigicfilho/pyxenv/issues)
- [Changelog](CHANGELOG.md)
- [Contribution Guide](CONTRIBUTING.md)

## Roadmap

### v0.3.0
- [ ] pyenv support
- [ ] Auto-install on Linux/macOS
- [ ] Installer cache

### v0.4.0
- [ ] Interactive TUI interface
- [ ] Project configuration (.pyxenvrc)
- [ ] Docker integration

### v1.0.0
- [ ] Stable API
- [ ] Complete documentation
- [ ] Verified PyPI package

## Inspiration and Alternatives

- **pyenv** - Complete Python version manager
- **virtualenv** - Virtual environment creation
- **pipx** - Install and run Python applications
- **conda** - Package and environment manager

`pyxenv` combines the best of these worlds with the simplicity of `npx`!

## Star History

If this project has been useful to you, consider giving it a ⭐!

---

<div align="center">
  
**Made with ❤️ by [Luigi C. Filho](https://github.com/luigicfilho)**

</div>