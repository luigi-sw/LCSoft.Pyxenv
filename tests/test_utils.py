'''Tests for pypx.utils module.'''

import subprocess
from unittest.mock import patch, Mock

import pytest

from pypx.utils import run_command, extract_version, is_version_prefix


class TestRunCommand:
    '''Tests for run_command function.'''

    def test_run_command_success(self, mock_subprocess_run):
        '''Test successful command execution.'''
        result = run_command(['python', '--version'])
        
        mock_subprocess_run.assert_called_once_with(
            ['python', '--version'],
            check=True
        )
        assert result.returncode == 0

    def test_run_command_with_kwargs(self, mock_subprocess_run):
        '''Test command execution with additional kwargs.'''
        run_command(['python', '--version'], capture_output=True, text=True)
        
        mock_subprocess_run.assert_called_once_with(
            ['python', '--version'],
            check=True,
            capture_output=True,
            text=True
        )

    def test_run_command_failure(self):
        '''Test command execution failure.'''
        with patch('subprocess.run') as mock:
            mock.side_effect = subprocess.CalledProcessError(1, 'cmd')
            
            with pytest.raises(subprocess.CalledProcessError):
                run_command(['invalid-command'])


class TestExtractVersion:
    '''Tests for extract_version function.'''

    @pytest.mark.parametrize('input_str,expected', [
        ('Python 3.11.5', '3.11.5'),
        ('Python 3.11.5rc1', '3.11.5'),
        ('3.10.2', '3.10.2'),
        ('Python 3.9', '3.9'),
        ('invalid', None),
        ('', None),
    ])
    def test_extract_version(self, input_str, expected):
        '''Test version extraction from various strings.'''
        assert extract_version(input_str) == expected


class TestIsVersionPrefix:
    '''Tests for is_version_prefix function.'''

    @pytest.mark.parametrize('version,expected', [
        ('3.11', True),
        ('3.9', True),
        ('3.11.5', False),
        ('3.11.5rc1', False),
        ('3', False),
        ('invalid', False),
    ])
    def test_is_version_prefix(self, version, expected):
        '''Test version prefix detection.'''
        assert is_version_prefix(version) == expected
