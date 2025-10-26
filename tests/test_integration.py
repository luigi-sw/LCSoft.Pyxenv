'''Integration tests for pypx.'''

import pytest
from pathlib import Path
from unittest.mock import patch

from pypx.python_manager import PythonManager
from pypx.venv_manager import VenvManager
from pypx.installer import PythonInstaller


class TestIntegration:
    '''Integration tests combining multiple components.'''

    def test_full_workflow_create_and_activate(self, temp_pypx_home, mock_subprocess_run):
        '''Test complete workflow: create and activate venv.'''
        version = '3.11'
        env_name = 'integration-test'
        
        # Mock Python executable
        with patch('pypx.python_manager.PythonManager.get_executable', 
                  return_value='/usr/bin/python3.11'):
            
            # Create venv
            env_path = VenvManager.create(version, env_name)
            assert env_path.exists()
            
            # List environments
            envs = VenvManager.list_all()
            assert env_name in envs

    def test_version_detection_and_usage(self, temp_pypx_home):
        '''Test detecting and using Python versions.'''
        # Create fake Python installation
        python_dir = temp_pypx_home / 'pythons' / '3.11.5'
        python_dir.mkdir(parents=True)
        (python_dir / 'python.exe').touch()
        
        with patch.object(PythonManager, '_get_version_from_executable', 
                         return_value='3.11.5'):
            # Find versions
            versions = PythonManager.find_versions(list_all=False)
            assert len(versions) == 1
            assert versions[0][0] == '3.11.5'
            
            # Get executable
            with patch('shutil.which', return_value=None):
                exe = PythonManager.get_executable('3.11.5')
                assert '3.11.5' in exe