'''Command-line interface for pypx.'''

import argparse
import sys

from pypx import __version__
from pypx.exceptions import PypxError
from pypx.installer import PythonInstaller
from pypx.python_manager import PythonManager
from pypx.venv_manager import VenvManager
from pypx.utils import run_command


def main() -> None:
    '''Main CLI entry point.'''
    parser = argparse.ArgumentParser(
        description='pypx: npx para Python — gerencie versões e ambientes facilmente',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Exemplos:
  pypx 3.11 script.py          # Executa script com Python 3.11
  pypx --create-env myenv      # Cria ambiente virtual
  pypx --activate myenv        # Ativa ambiente virtual
  pypx --list                  # Lista versões pypx
  pypx --list-all              # Lista todas as versões
        '''
    )
    
    parser.add_argument('version', nargs='?', help='Versão do Python (ex: 3.11)')
    parser.add_argument('script', nargs='?', help='Script para executar')
    parser.add_argument('--create-env', metavar='NAME', help='Cria um ambiente virtual')
    parser.add_argument('--activate', metavar='NAME', help='Ativa um ambiente existente')
    parser.add_argument('--list-envs', action='store_true', help='Lista ambientes criados')
    parser.add_argument('--list', action='store_true', help='Lista versões pypx')
    parser.add_argument('--list-all', action='store_true', help='Lista todas as versões')
    parser.add_argument('--version', action='store_true', dest='show_version', help='Mostra versão do pypx')

    args, extras = parser.parse_known_args()

    try:
        # Show version
        if args.show_version and not any([args.script, args.create_env, args.activate, args.list, args.list_all, args.list_envs]):
            print(f'pypx {__version__}')
            return

        # List Python versions
        if args.list or args.list_all:
            print('✅ Versões detectadas:')
            versions = PythonManager.find_versions(list_all=args.list_all)
            for ver, path, source in versions:
                tag = '(pypx)' if source == 'pypx' else '(global)'
                print(f'  {ver} → {path} {tag}')
            return

        # List environments
        if args.list_envs:
            print('🧰 Ambientes disponíveis:')
            envs = VenvManager.list_all()
            if envs:
                for env in envs:
                    print(f'  - {env}')
            else:
                print('  (nenhum ambiente encontrado)')
            return

        # Activate environment
        if args.activate:
            VenvManager.activate(args.activate)
            return

        # Create environment
        if args.create_env:
            version = args.version or '3.11'
            VenvManager.create(version, args.create_env)
            return

        # Execute script with version
        if args.version and args.script:
            version = args.version
            try:
                python_exe = PythonManager.get_executable(version)
            except PypxError:
                print(f'⚠️  Python {version} não encontrado. Instalando...')
                PythonInstaller.install(version)
                python_exe = PythonManager.get_executable(version)
            
            run_command([python_exe, args.script] + extras)
            return

        # No valid command
        parser.print_help()

    except PypxError as e:
        print(f'❌ Erro: {e}')
        sys.exit(1)
    except KeyboardInterrupt:
        print('\n⚠️  Operação cancelada.')
        sys.exit(130)
    except Exception as e:
        print(f'❌ Erro inesperado: {e}')
        sys.exit(1)


if __name__ == '__main__':
    main()