'''pypx - npx-like tool for Python.'''

__version__ = '0.2.0'
__author__ = 'Luigi C. Filho'
__email__ = 'lcdev@lcdesenvolvimentos.com.br'

from pypx.python_manager import PythonManager
from pypx.venv_manager import VenvManager

__all__ = ['PythonManager', 'VenvManager', '__version__']