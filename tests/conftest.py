'''Pytest configuration and fixtures.'''

import tempfile
from pathlib import Path
from unittest.mock import Mock, patch

import pytest


@pytest.fixture
def temp_pypx_home(tmp_path):
    '''Create a temporary pypx home directory.'''
    pypx_home = tmp_path / '.pypx'
    pythons_dir = pypx_home / 'pythons'
    envs_dir = pypx_home / 'envs'
    
    pythons_dir.mkdir(parents=True)
    envs_dir.mkdir(parents=True)
    
    with patch('pypx.config.PYPX_HOME', pypx_home), \
         patch('pypx.config.PYTHON_DIR', pythons_dir), \
         patch('pypx.config.ENV_DIR', envs_dir):
        yield pypx_home


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

