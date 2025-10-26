'''Tests for pypx.venv_manager module.'''

import os
from pathlib import Path
from unittest.mock import patch, Mock

import pytest

from pypx.venv_manager import VenvManager
from pypx.exceptions import VenvError


class TestVenvManager:
    '''Tests for VenvManager class.'''

    def test_create_venv_success(self, temp_pypx_home, mock_subprocess_run):
        '''Test successful venv creation.'''
        version = '3.11'
        env_name = 'test-env'
        
        with patch('pypx.python_manager.PythonManager.get_executable', 
                  return_value='/usr/bin/python3.11'):
            
            env_path = VenvManager.create(version, env_name)
            
            assert env_path == temp_pypx_home / 'envs' / env_name
            mock_subprocess_run.assert_called_once()

    def test_create_venv_default_name(self, temp_pypx_home, mock_subprocess_run):
        '''Test venv creation with default name.'''
        version = '3.11'
        
        with patch('pypx.python_manager.PythonManager.get_executable', 
                  return_value='/usr/bin/python3.11'):
            
            env_path = VenvManager.create(version)
            
            assert env_path.name == f'pypx-{version}'

    def test_create_venv_already_exists(self, temp_pypx_home):
        '''Test handling existing venv.'''
        version = '3.11'
        env_name = 'existing-env'
        env_path = temp_pypx_home / 'envs' / env_name
        env_path.mkdir(parents=True)
        
        result = VenvManager.create(version, env_name)
        
        assert result == env_path

    def test_create_venv_python_not_found(self, temp_pypx_home):
        '''Test error when Python version not found.'''
        with patch('pypx.python_manager.PythonManager.get_executable', 
                  side_effect=Exception('Python not found')):
            
            with pytest.raises(VenvError, match='Erro ao obter Python'):
                VenvManager.create('3.99', 'test-env')

    def test_create_venv_creation_failure(self, temp_pypx_home):
        '''Test handling venv creation failure.'''
        with patch('pypx.python_manager.PythonManager.get_executable', 
                  return_value='/usr/bin/python3.11'), \
             patch('pypx.utils.run_command', side_effect=Exception('Venv creation failed')):
            
            with pytest.raises(VenvError, match='Erro ao criar ambiente'):
                VenvManager.create('3.11', 'test-env')

    def test_activate_venv_windows(self, temp_pypx_home):
        '''Test venv activation on Windows.'''
        env_name = 'test-env'
        env_path = temp_pypx_home / 'envs' / env_name
        scripts_dir = env_path / 'Scripts'
        scripts_dir.mkdir(parents=True)
        (scripts_dir / 'activate.bat').touch()
        
        with patch('os.name', 'nt'), \
             patch('subprocess.run') as mock_run:
            
            VenvManager.activate(env_name)
            
            mock_run.assert_called_once()
            args = mock_run.call_args[0][0]
            assert 'cmd.exe' in args
            assert 'activate.bat' in str(args)

    def test_activate_venv_unix(self, temp_pypx_home):
        '''Test venv activation on Unix.'''
        env_name = 'test-env'
        env_path = temp_pypx_home / 'envs' / env_name
        bin_dir = env_path / 'bin'
        bin_dir.mkdir(parents=True)
        (bin_dir / 'activate').touch()
        
        with patch('os.name', 'posix'), \
             patch('subprocess.run') as mock_run:
            
            VenvManager.activate(env_name)
            
            mock_run.assert_called_once()
            args = mock_run.call_args[0][0]
            assert 'bash' in args
            assert 'activate' in str(args)

    def test_activate_venv_not_found(self, temp_pypx_home):
        '''Test error when venv not found.'''
        with pytest.raises(VenvError, match='não encontrado'):
            VenvManager.activate('nonexistent-env')

    def test_activate_venv_script_not_found(self, temp_pypx_home):
        '''Test error when activation script not found.'''
        env_name = 'test-env'
        env_path = temp_pypx_home / 'envs' / env_name
        env_path.mkdir(parents=True)
        
        with patch('os.name', 'nt'):
            with pytest.raises(VenvError, match='Script de ativação não encontrado'):
                VenvManager.activate(env_name)

    def test_list_all_empty(self, temp_pypx_home):
        '''Test listing with no environments.'''
        envs = VenvManager.list_all()
        assert envs == []

    def test_list_all_with_envs(self, temp_pypx_home):
        '''Test listing existing environments.'''
        env_names = ['env1', 'env2', 'env3']
        envs_dir = temp_pypx_home / 'envs'
        
        for name in env_names:
            (envs_dir / name).mkdir()
        
        envs = VenvManager.list_all()
        
        assert sorted(envs) == sorted(env_names)

    def test_list_all_no_envs_dir(self):
        '''Test listing when envs directory doesn't exist.'''
        with patch('pypx.config.ENV_DIR', Path('/nonexistent/path')):
            envs = VenvManager.list_all()
            assert envs == []
