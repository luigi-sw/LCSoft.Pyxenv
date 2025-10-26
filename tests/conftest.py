'''Pytest configuration and fixtures.'''

import tempfile
from pathlib import Path
from unittest.mock import Mock, patch

import pytest


@pytest.fixture
def temp_pyxenv_home(tmp_path):
    '''Create a temporary pyxenv home directory.'''
    pyxenv_home = tmp_path / '.pyxenv'
    pythons_dir = pyxenv_home / 'pythons'
    envs_dir = pyxenv_home / 'envs'
    
    pythons_dir.mkdir(parents=True)
    envs_dir.mkdir(parents=True)
    
    with patch('pyxenv.config.pyxenv_HOME', pyxenv_home), \
         patch('pyxenv.config.PYTHON_DIR', pythons_dir), \
         patch('pyxenv.config.ENV_DIR', envs_dir):
        yield pyxenv_home


@pytest.fixture
def mock_subprocess_run():
    '''Mock subprocess.run to avoid actual command execution.'''
    with patch('subprocess.run') as mock:
        mock.return_value = Mock(
            returncode=0,
            stdout='Python 3.11.5',
            stderr=''
        )
        yield mock


@pytest.fixture
def mock_urllib():
    '''Mock urllib for download tests.'''
    with patch('urllib.request.urlopen') as mock_open, \
         patch('urllib.request.urlretrieve') as mock_retrieve:
        yield mock_open, mock_retrieve

