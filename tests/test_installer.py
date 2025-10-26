'''Tests for pypx.installer module.'''

import tempfile
from pathlib import Path
from unittest.mock import patch, Mock, MagicMock
import urllib.error

import pytest

from pypx.installer import PythonInstaller
from pypx.exceptions import DownloadError, InstallationError


class TestPythonInstaller:
    '''Tests for PythonInstaller class.'''

    def test_find_available_installer_success(self, mock_urllib):
        '''Test finding available installer.'''
        mock_open, _ = mock_urllib
        
        # Mock FTP listing
        mock_open.return_value.__enter__.return_value.read.return_value = b'''
            <a href="3.11.0/">3.11.0/</a>
            <a href="3.11.1/">3.11.1/</a>
            <a href="3.11.5/">3.11.5/</a>
        '''
        
        # Mock version page
        with patch('urllib.request.urlopen') as mock_version:
            mock_version.return_value.__enter__.return_value.read.return_value = b'''
                <a href="python-3.11.5-amd64.exe">python-3.11.5-amd64.exe</a>
            '''
            
            version, url = PythonInstaller.find_available_installer('3.11')
            
            assert version == '3.11.5'
            assert 'python-3.11.5-amd64.exe' in url

    def test_find_available_installer_no_versions(self, mock_urllib):
        '''Test error when no versions found.'''
        mock_open, _ = mock_urllib
        mock_open.return_value.__enter__.return_value.read.return_value = b'<html></html>'
        
        with pytest.raises(DownloadError, match='Nenhuma versão encontrada'):
            PythonInstaller.find_available_installer('3.99')

    def test_find_available_installer_no_installer(self, mock_urllib):
        '''Test error when no installer found.'''
        mock_open, _ = mock_urllib
        
        # Mock FTP listing with versions but no installers
        mock_open.return_value.__enter__.return_value.read.side_effect = [
            b'<a href="3.11.5/">3.11.5/</a>',
            b'<html>No installers here</html>'
        ]
        
        with pytest.raises(DownloadError, match='Nenhum instalador encontrado'):
            PythonInstaller.find_available_installer('3.11')

    def test_find_available_installer_network_error(self):
        '''Test handling network errors.'''
        with patch('urllib.request.urlopen', side_effect=urllib.error.URLError('Network error')):
            with pytest.raises(DownloadError, match='Falha ao acessar'):
                PythonInstaller.find_available_installer('3.11')

    def test_download_version_prefix(self, mock_urllib):
        '''Test downloading with version prefix.'''
        mock_open, mock_retrieve = mock_urllib
        
        # Mock finding installer
        with patch.object(PythonInstaller, 'find_available_installer', 
                         return_value=('3.11.5', 'https://python.org/python-3.11.5-amd64.exe')):
            
            installer_path = PythonInstaller.download('3.11')
            
            assert installer_path.name == 'python-3.11.5-amd64.exe'
            mock_retrieve.assert_called_once()

    def test_download_full_version(self, mock_urllib):
        '''Test downloading with full version.'''
        _, mock_retrieve = mock_urllib
        
        installer_path = PythonInstaller.download('3.11.5')
        
        assert installer_path.name == 'python-3.11.5-amd64.exe'
        mock_retrieve.assert_called_once()

    def test_download_http_error(self):
        '''Test handling HTTP errors during download.'''
        with patch('urllib.request.urlretrieve', 
                  side_effect=urllib.error.HTTPError('url', 404, 'Not Found', {}, None)):
            
            with pytest.raises(DownloadError, match='Erro HTTP 404'):
                PythonInstaller.download('3.11.5')

    def test_download_generic_error(self):
        '''Test handling generic download errors.'''
        with patch('urllib.request.urlretrieve', side_effect=Exception('Network error')):
            with pytest.raises(DownloadError, match='Erro ao baixar'):
                PythonInstaller.download('3.11.5')

    def test_install_already_installed(self, temp_pypx_home):
        '''Test skipping installation when already installed.'''
        version = '3.11.5'
        install_dir = temp_pypx_home / 'pythons' / version
        install_dir.mkdir(parents=True)
        
        result = PythonInstaller.install(version)
        
        assert result == install_dir

    def test_install_success(self, temp_pypx_home, mock_subprocess_run):
        '''Test successful installation.'''
        version = '3.11.5'
        installer_path = Path(tempfile.gettempdir()) / 'python-3.11.5-amd64.exe'
        
        with patch.object(PythonInstaller, 'download', return_value=installer_path):
            install_dir = temp_pypx_home / 'pythons' / version
            python_exe = install_dir / 'python.exe'
            
            # Create fake python.exe after installation
            def create_exe(*args, **kwargs):
                install_dir.mkdir(parents=True, exist_ok=True)
                python_exe.touch()
                return Mock(returncode=0)
            
            mock_subprocess_run.side_effect = create_exe
            
            result = PythonInstaller.install(version)
            
            assert result == install_dir
            assert python_exe.exists()

    def test_install_command_failure(self, temp_pypx_home):
        '''Test handling installation command failure.'''
        version = '3.11.5'
        installer_path = Path(tempfile.gettempdir()) / 'python-3.11.5-amd64.exe'
        
        with patch.object(PythonInstaller, 'download', return_value=installer_path), \
             patch('pypx.utils.run_command', side_effect=Exception('Install failed')):
            
            with pytest.raises(InstallationError, match='Falha na instalação'):
                PythonInstaller.install(version)

    def test_install_exe_not_found(self, temp_pypx_home, mock_subprocess_run):
        '''Test error when python.exe not found after installation.'''
        version = '3.11.5'
        installer_path = Path(tempfile.gettempdir()) / 'python-3.11.5-amd64.exe'
        
        with patch.object(PythonInstaller, 'download', return_value=installer_path):
            with pytest.raises(InstallationError, match='python.exe não encontrado'):
                PythonInstaller.install(version)
