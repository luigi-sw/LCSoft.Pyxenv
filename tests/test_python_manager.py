'''Tests for pyxenv.python_manager module.'''

import shutil
from pathlib import Path
from unittest.mock import patch, Mock

import pytest

from pyxenv.python_manager import PythonManager
from pyxenv.exceptions import PythonNotFoundError


class TestPythonManager:
    '''Tests for PythonManager class.'''

    def test_find_versions_empty(self, temp_pyxenv_home):
        '''Test finding versions with no installations.'''
        versions = PythonManager.find_versions(list_all=False)
        assert versions == []

    def test_find_versions_with_pyxenv_installations(self, temp_pyxenv_home, mock_subprocess_run):
        '''Test finding pyxenv-installed versions.'''
        # Create fake Python installation
        python_dir = temp_pyxenv_home / 'pythons' / '3.11.5'
        python_dir.mkdir(parents=True)
        
        if shutil.which('python'):  # Windows
            (python_dir / 'python.exe').touch()
        else:  # Unix
            bin_dir = python_dir / 'bin'
            bin_dir.mkdir()
            (bin_dir / 'python').touch()

        with patch.object(PythonManager, '_get_version_from_executable', return_value='3.11.5'):
            versions = PythonManager.find_versions(list_all=False)
            
            assert len(versions) == 1
            assert versions[0][0] == '3.11.5'
            assert versions[0][2] == 'pyxenv'

    def test_find_versions_with_global_installations(self, temp_pyxenv_home):
        '''Test finding global Python installations.'''
        with patch('shutil.which', return_value='/usr/bin/python3.11'), \
             patch.object(PythonManager, '_get_version_from_executable', return_value='3.11.5'):
            
            versions = PythonManager.find_versions(list_all=True)
            
            assert len(versions) >= 1
            assert any(v[2] == 'global' for v in versions)

    def test_find_versions_sorted(self, temp_pyxenv_home):
        '''Test that versions are sorted correctly.'''
        # Create multiple fake installations
        for version in ['3.9.0', '3.11.5', '3.10.2']:
            python_dir = temp_pyxenv_home / 'pythons' / version
            python_dir.mkdir(parents=True)
            (python_dir / 'python.exe').touch()

        with patch.object(PythonManager, '_get_version_from_executable', 
                         side_effect=['3.9.0', '3.11.5', '3.10.2']):
            versions = PythonManager.find_versions(list_all=False)
            
            version_numbers = [v[0] for v in versions]
            assert version_numbers == ['3.11.5', '3.10.2', '3.9.0']

    def test_get_executable_default(self):
        '''Test getting default Python executable.'''
        with patch('shutil.which', return_value='/usr/bin/python3'):
            exe = PythonManager.get_executable(None)
            assert exe == '/usr/bin/python3'

    def test_get_executable_specific_version(self):
        '''Test getting specific Python version.'''
        with patch('shutil.which', return_value='/usr/bin/python3.11'):
            exe = PythonManager.get_executable('3.11')
            assert exe == '/usr/bin/python3.11'

    def test_get_executable_pyxenv_version(self, temp_pyxenv_home):
        '''Test getting pyxenv-installed Python version.'''
        python_dir = temp_pyxenv_home / 'pythons' / '3.11.5'
        python_dir.mkdir(parents=True)
        python_exe = python_dir / 'python.exe'
        python_exe.touch()

        with patch('shutil.which', return_value=None):
            exe = PythonManager.get_executable('3.11.5')
            assert Path(exe) == python_exe

    def test_get_executable_not_found(self):
        '''Test error when Python version not found.'''
        with patch('shutil.which', return_value=None):
            with pytest.raises(PythonNotFoundError):
                PythonManager.get_executable('3.99')

    def test_get_version_from_executable_success(self):
        '''Test extracting version from executable.'''
        with patch('subprocess.run') as mock:
            mock.return_value = Mock(
                stdout='Python 3.11.5',
                stderr=''
            )
            
            version = PythonManager._get_version_from_executable('/usr/bin/python3')
            assert version == '3.11.5'

    def test_get_version_from_executable_failure(self):
        '''Test handling failure when getting version.'''
        with patch('subprocess.run', side_effect=Exception('Command failed')):
            version = PythonManager._get_version_from_executable('/invalid/path')
            assert version is None
