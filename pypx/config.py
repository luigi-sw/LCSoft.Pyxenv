'''Configuration and constants for pypx.'''

from pathlib import Path

# Diretórios base
PYPX_HOME = Path.home() / '.pypx'
PYTHON_DIR = PYPX_HOME / 'pythons'
ENV_DIR = PYPX_HOME / 'envs'

# URLs
PYTHON_FTP_BASE = 'https://www.python.org/ftp/python/'

# Versões Python suportadas
SUPPORTED_VERSIONS = ['3.8', '3.9', '3.10', '3.11', '3.12', '3.13']

# Criar diretórios se não existirem
for directory in [PYTHON_DIR, ENV_DIR]:
    directory.mkdir(parents=True, exist_ok=True)