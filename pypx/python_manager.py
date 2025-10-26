'''Python version detection and management.'''

import os
import shutil
import subprocess
from pathlib import Path
from typing import Optional

from pypx.config import PYTHON_DIR
from pypx.exceptions import PythonNotFoundError
from pypx.utils import extract_version


class PythonManager:
    '''Manages Python installations and version detection.'''

    @staticmethod
    def find_versions(list_all: bool = False) -> list[tuple[str, str, str]]:
        '''
        List Python versions installed globally and via pypx.
        
        Args:
            list_all: Include global Python installations
            
        Returns:
            List of tuples (version, path, source)
        '''
        versions = []
        seen = set()

        # Global versions
        if list_all:
            possible_names = [
                'python3.13', 'python3.12', 'python3.11', 'python3.10',
                'python3.9', 'python3.8', 'python3', 'python'
            ]
            for name in possible_names:
                path = shutil.which(name)
                if path and path.lower() not in seen:
                    version = PythonManager._get_version_from_executable(path)
                    if version:
                        versions.append((version, path, 'global'))
                        seen.add(path.lower())

        # pypx versions
        if PYTHON_DIR.exists():
            for directory in PYTHON_DIR.iterdir():
                if directory.is_dir():
                    py_exe = PythonManager._get_python_executable_path(directory)
                    if py_exe and py_exe.exists() and str(py_exe).lower() not in seen:
                        version = PythonManager._get_version_from_executable(str(py_exe))
                        if version:
                            versions.append((version, str(py_exe), 'pypx'))
                            seen.add(str(py_exe).lower())

        # Sort by version (descending)
        versions = sorted(
            versions,
            key=lambda x: tuple(map(int, x[0].split('.'))),
            reverse=True
        )
        return versions

    @staticmethod
    def _get_python_executable_path(directory: Path) -> Optional[Path]:
        '''Get Python executable path for a directory.'''
        if os.name == 'nt':
            return directory / 'python.exe'
        return directory / 'bin' / 'python'

    @staticmethod
    def _get_version_from_executable(executable: str) -> Optional[str]:
        '''Get Python version from executable.'''
        try:
            result = subprocess.run(
                [executable, '--version'],
                capture_output=True,
                text=True,
                timeout=5
            )
            version_string = result.stdout.strip() or result.stderr.strip()
            return extract_version(version_string)
        except Exception:
            return None

    @staticmethod
    def get_executable(version: Optional[str] = None) -> str:
        '''
        Get Python executable for specified version.
        
        Args:
            version: Python version (e.g., "3.11" or "3.11.5") or None for default
            
        Returns:
            Path to Python executable
            
        Raises:
            PythonNotFoundError: If version not found
        '''
        if version in (None, 'default'):
            exe = shutil.which('python3') or shutil.which('python')
            if not exe:
                raise PythonNotFoundError('No default Python found')
            return exe

        # Try global installation
        exe = shutil.which(f'python{version}')
        if exe:
            return exe

        # Try pypx installation
        local_exe = PYTHON_DIR / version / ('python.exe' if os.name == 'nt' else 'bin/python')
        if local_exe.exists():
            return str(local_exe)

        raise PythonNotFoundError(f'Python {version} not found')
