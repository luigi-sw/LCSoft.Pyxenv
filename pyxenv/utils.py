'''Utility functions for pyxenv.'''

import re
import subprocess
from typing import Optional

def run_command(cmd: list[str], check: bool = True, **kwargs) -> subprocess.CompletedProcess:
    '''
    Execute a command and print it.
    
    Args:
        cmd: Command and arguments as list
        check: Raise exception on non-zero exit
        **kwargs: Additional arguments for subprocess.run
        
    Returns:
        CompletedProcess instance
    '''
    print(f"- Executando: {' '.join(map(str, cmd))}")
    return subprocess.run(cmd, check=check, **kwargs)

def extract_version(version_string: str) -> Optional[str]:
    '''
    Extract version number from Python version string.
    
    Args:
        version_string: String like "Python 3.11.5"
        
    Returns:
        Version string like "3.11.5" or None
    '''
    match = re.search(r'(\d+\.\d+(?:\.\d+)?)', version_string)
    return match.group(1) if match else None

def is_version_prefix(version: str) -> bool:
    '''
    Check if version is a prefix (e.g., "3.11") or full version (e.g., "3.11.5").
    
    Args:
        version: Version string
        
    Returns:
        True if it's a prefix (major.minor only)
    '''
    return bool(re.match(r'^\d+\.\d+$', version))
