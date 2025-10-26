'''Configuration and constants for pyxenv.'''

from pathlib import Path

# Diretórios base
pyxenv_HOME = Path.home() / '.pyxenv'
PYTHON_DIR = pyxenv_HOME / 'pythons'
ENV_DIR = pyxenv_HOME / 'envs'

# URLs
PYTHON_FTP_BASE = 'https://www.python.org/ftp/python/'

# Versões Python suportadas
SUPPORTED_VERSIONS = ['3.8', '3.9', '3.10', '3.11', '3.12', '3.13']

# Criar diretórios se não existirem
for directory in [PYTHON_DIR, ENV_DIR]:
    directory.mkdir(parents=True, exist_ok=True)