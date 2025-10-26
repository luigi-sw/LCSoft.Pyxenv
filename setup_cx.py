"""Setup configuration for cx_Freeze to generate pypx executable and .msi ."""
from cx_Freeze import setup, Executable

# executables = [Executable("pypx/cli.py", base=None)]  

executable = [Executable(
    script="pypx/cli.py",
    base=None,                # ou "Win32GUI" para GUI
    target_name="pypx",       # <-- nome do .exe (sem .exe)
    icon="pypx/pypx.ico"    # opcional
)]

bdist_msi_options = {
    "add_to_path": True,   
    "all_users": False,       # True = para todos os usuários (requer admin)
    "upgrade_code": "{7690834c-f172-43c6-8c6e-0056fe1a8417}",  # seu GUID
    "install_icon": "pypx/pypx.ico",   # ícone no Add/Remove
}

setup(
    name="pypx",
    version="0.2.0",
    description="npx-like tool for Python: switch versions and manage virtual environments",
    executables=executable,
    options={"bdist_msi": bdist_msi_options},
)