'''Virtual environment management.'''

import os
import subprocess
from pathlib import Path
from typing import Optional

from pyxenv.config import ENV_DIR
from pyxenv.exceptions import VenvError
from pyxenv.python_manager import PythonManager
from pyxenv.utils import run_command


class VenvManager:
    '''Manages virtual environments.'''

    @staticmethod
    def create(version: str, env_name: Optional[str] = None) -> Path:
        '''
        Create a virtual environment with specified Python version.
        
        Args:
            version: Python version
            env_name: Environment name (default: "pyxenv-{version}")
            
        Returns:
            Path to created environment
            
        Raises:
            VenvError: If creation fails
        '''
        env_name = env_name or f'pyxenv-{version}'
        env_path = ENV_DIR / env_name
        
        if env_path.exists():
            print(f'-  Ambiente "{env_name}" já existe.')
            return env_path

        try:
            python_exe = PythonManager.get_executable(version)
        except Exception as e:
            raise VenvError(f'Erro ao obter Python {version}: {e}')

        print(f'🔧 Criando ambiente virtual "{env_name}" com Python {version}...')
        
        try:
            run_command([python_exe, '-m', 'venv', str(env_path)])
            print(f'- Ambiente criado em {env_path}')
            return env_path
        except Exception as e:
            raise VenvError(f'Erro ao criar ambiente: {e}')

    @staticmethod
    def activate(env_name: str) -> None:
        '''
        Open a new terminal with activated environment.
        
        Args:
            env_name: Environment name
            
        Raises:
            VenvError: If environment not found or activation fails
        '''
        env_path = ENV_DIR / env_name
        
        if not env_path.exists():
            raise VenvError(f'Ambiente "{env_name}" não encontrado.')

        if os.name == 'nt':
            activate_script = env_path / 'Scripts' / 'activate.bat'
            if not activate_script.exists():
                raise VenvError(f'Script de ativação não encontrado: {activate_script}')
            
            print(f'- Abrindo novo terminal com ambiente "{env_name}" ativado...')
            subprocess.run(['cmd.exe', '/k', str(activate_script)])
        else:
            activate_script = env_path / 'bin' / 'activate'
            if not activate_script.exists():
                raise VenvError(f'Script de ativação não encontrado: {activate_script}')
            
            print(f'- Abrindo shell com ambiente "{env_name}" ativado...')
            subprocess.run(['bash', '--rcfile', str(activate_script)])

    @staticmethod
    def list_all() -> list[str]:
        '''
        List all available environments.
        
        Returns:
            List of environment names
        '''
        if not ENV_DIR.exists():
            return []
        
        return [env.name for env in ENV_DIR.iterdir() if env.is_dir()]
