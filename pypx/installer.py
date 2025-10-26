'''Python download and installation for Windows.'''

import re
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

from pypx.config import PYTHON_DIR, PYTHON_FTP_BASE
from pypx.exceptions import DownloadError, InstallationError
from pypx.utils import is_version_prefix, run_command


class PythonInstaller:
    '''Handles Python download and installation on Windows.'''

    @staticmethod
    def find_available_installer(version_prefix: str) -> tuple[str, str]:
        '''
        Find the latest installer for a Python version series.
        
        Args:
            version_prefix: Version prefix like "3.11"
            
        Returns:
            Tuple of (full_version, installer_url)
            
        Raises:
            DownloadError: If no installer found
        '''
        print(f'- Procurando versões disponíveis para {version_prefix}...')
        
        try:
            html = urllib.request.urlopen(PYTHON_FTP_BASE).read().decode('utf-8')
        except Exception as e:
            raise DownloadError(f'Falha ao acessar {PYTHON_FTP_BASE}: {e}')

        # Find all versions in the series
        pattern = rf'href="({re.escape(version_prefix)}\.\d+)/"'
        versions = sorted(
            re.findall(pattern, html),
            key=lambda v: list(map(int, v.split('.'))),
            reverse=True,
        )
        
        if not versions:
            raise DownloadError(f'Nenhuma versão encontrada para {version_prefix}')

        # Find a version with available installer
        for ver in versions:
            ver_url = f'{PYTHON_FTP_BASE}{ver}/'
            try:
                sub_html = urllib.request.urlopen(ver_url).read().decode('utf-8')
                exe_match = re.search(r'href="(python-[\w\.-]*amd64\.exe)"', sub_html)
                
                if exe_match:
                    filename = exe_match.group(1)
                    full_url = ver_url + filename
                    print(f'- Encontrado instalador: {full_url}')
                    return ver, full_url
            except Exception:
                continue

        raise DownloadError(f'Nenhum instalador encontrado para {version_prefix}')

    @staticmethod
    def download(version: str) -> Path:
        '''
        Download Python installer for Windows.
        
        Args:
            version: Python version (e.g., "3.11" or "3.11.5")
            
        Returns:
            Path to downloaded installer
            
        Raises:
            DownloadError: If download fails
        '''
        if is_version_prefix(version):
            version, installer_url = PythonInstaller.find_available_installer(version)
        else:
            installer_url = f'{PYTHON_FTP_BASE}{version}/python-{version}-amd64.exe'

        installer_path = Path(tempfile.gettempdir()) / Path(installer_url).name
        print(f'-  Baixando instalador de {installer_url}')
        
        try:
            urllib.request.urlretrieve(installer_url, installer_path)
            print(f'- Instalador salvo em: {installer_path}')
            return installer_path
        except urllib.error.HTTPError as e:
            raise DownloadError(f'Erro HTTP {e.code} ao baixar {installer_url}')
        except Exception as e:
            raise DownloadError(f'Erro ao baixar Python {version}: {e}')

    @staticmethod
    def install(version: str) -> Path:
        '''
        Install Python silently to pypx directory.
        
        Args:
            version: Python version to install
            
        Returns:
            Path to installation directory
            
        Raises:
            InstallationError: If installation fails
        '''
        install_dir = PYTHON_DIR / version
        
        if install_dir.exists():
            print(f'- Python {version} já instalado em {install_dir}')
            return install_dir

        installer = PythonInstaller.download(version)
        print(f'- Instalando Python {version} em {install_dir}')
        
        cmd = [
            str(installer),
            '/quiet',
            'InstallAllUsers=0',
            'PrependPath=0',
            f'TargetDir={install_dir}',
            'Include_launcher=0',
            'Include_test=0',
            'SimpleInstall=1',
        ]
        
        try:
            run_command(cmd)
        except Exception as e:
            raise InstallationError(f'Falha na instalação: {e}')

        python_exe = install_dir / 'python.exe'
        if not python_exe.exists():
            raise InstallationError(f'python.exe não encontrado em {install_dir}')

        print(f'- Python {version} instalado com sucesso.')
        return install_dir
