'''Tests for pypx.cli module.'''

import sys
from io import StringIO
from unittest.mock import patch, Mock

import pytest

from pypx.cli import main


class TestCLI:
    '''Tests for CLI commands.'''

    def test_show_version(self, capsys):
        '''Test --version flag.'''
        with patch('sys.argv', ['pypx', '--version']):
            main()
            
        captured = capsys.readouterr()
        assert 'pypx' in captured.out
        assert '0.3.0' in captured.out

    def test_list_versions(self, capsys):
        '''Test --list flag.'''
        with patch('sys.argv', ['pypx', '--list']), \
             patch('pypx.python_manager.PythonManager.find_versions', 
                   return_value=[('3.11.5', '/usr/bin/python3.11', 'pypx')]):
            
            main()
            
        captured = capsys.readouterr()
        assert '3.11.5' in captured.out
        assert 'pypx' in captured.out

    def test_list_envs(self, capsys):
        '''Test --list-envs flag.'''
        with patch('sys.argv', ['pypx', '--list-envs']), \
             patch('pypx.venv_manager.VenvManager.list_all', 
                   return_value=['env1', 'env2']):
            
            main()
            
        captured = capsys.readouterr()
        assert 'env1' in captured.out
        assert 'env2' in captured.out

    def test_create_env(self):
        '''Test --create-env command.'''
        with patch('sys.argv', ['pypx', '3.11', '--create-env', 'myenv']), \
             patch('pypx.venv_manager.VenvManager.create') as mock_create:
            
            main()
            
            mock_create.assert_called_once_with('3.11', 'myenv')

    def test_activate_env(self):
        '''Test --activate command.'''
        with patch('sys.argv', ['pypx', '--activate', 'myenv']), \
             patch('pypx.venv_manager.VenvManager.activate') as mock_activate:
            
            main()
            
            mock_activate.assert_called_once_with('myenv')

    def test_execute_script(self):
        '''Test executing script with version.'''
        with patch('sys.argv', ['pypx', '3.11', 'script.py']), \
             patch('pypx.python_manager.PythonManager.get_executable', 
                   return_value='/usr/bin/python3.11'), \
             patch('pypx.utils.run_command') as mock_run:
            
            main()
            
            mock_run.assert_called_once()
            args = mock_run.call_args[0][0]
            assert '/usr/bin/python3.11' in args
            assert 'script.py' in args

    def test_execute_script_auto_install(self):
        '''Test auto-installing Python when not found.'''
        with patch('sys.argv', ['pypx', '3.11', 'script.py']), \
             patch('pypx.python_manager.PythonManager.get_executable', 
                   side_effect=[Exception('Not found'), '/path/to/python']), \
             patch('pypx.installer.PythonInstaller.install') as mock_install, \
             patch('pypx.utils.run_command'):
            
            main()
            
            mock_install.assert_called_once_with('3.11')

    def test_error_handling(self, capsys):
        '''Test error handling.'''
        with patch('sys.argv', ['pypx', '--activate', 'nonexistent']), \
             patch('pypx.venv_manager.VenvManager.activate', 
                   side_effect=Exception('Env not found')):
            
            with pytest.raises(SystemExit):
                main()
            
            captured = capsys.readouterr()
            assert 'Erro' in captured.out

    def test_keyboard_interrupt(self, capsys):
        '''Test handling Ctrl+C.'''
        with patch('sys.argv', ['pypx', '--list']), \
             patch('pypx.python_manager.PythonManager.find_versions', 
                   side_effect=KeyboardInterrupt):
            
            with pytest.raises(SystemExit) as exc:
                main()
            
            assert exc.value.code == 130
            captured = capsys.readouterr()
            assert 'cancelada' in captured.out
