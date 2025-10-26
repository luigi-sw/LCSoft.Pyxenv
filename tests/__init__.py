'''Test suite for pyxenv.'''

import sys
from pathlib import Path

# Adiciona o diretório raiz ao PYTHONPATH para imports
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))