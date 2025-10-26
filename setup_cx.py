"""Setup configuration for cx_Freeze to generate pyxenv executable and .msi ."""
from cx_Freeze import setup, Executable

executable = [Executable(
    script="pyxenv/cli.py",
    base=None, 
    target_name="pyxenv",  
    icon="pyxenv/pyxenv.ico" 
)]

bdist_msi_options = {
    "add_to_path": True,   
    "all_users": False,       # True = para todos os usuários (requer admin)
    "upgrade_code": "{7690834c-f172-43c6-8c6e-0056fe1a8417}", 
    "install_icon": "pyxenv/pyxenv.ico", 
}

setup(
    name="pyxenv",
    version="0.2.0",
    description="npx-like tool for Python: switch versions and manage virtual environments",
    executables=executable,
    options={"bdist_msi": bdist_msi_options},
)