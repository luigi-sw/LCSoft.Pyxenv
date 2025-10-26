"""Setup configuration for pypx package."""
from pathlib import Path
from setuptools import setup, find_packages

readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

version = "0.2.0"

setup(
    name="pyxenv",
    version=version,
    description="npx-like tool for Python: switch versions and manage virtual environments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Luigi C. Filho",
    author_email="lcdev@lcdesenvolvimentos.com.br",
    url="https://github.com/luigicfilho/pyxenv",
    project_urls={
        "Bug Tracker": "https://github.com/luigicfilho/pyxenv/issues",
        "Documentation": "https://github.com/luigicfilho/pyxenv#readme",
        "Source Code": "https://github.com/luigicfilho/pyxenv",
        "Changelog": "https://github.com/luigicfilho/pyxenv/blob/main/CHANGELOG.md",
    },
    keywords=[
        "python",
        "version-manager",
        "virtual-environment",
        "npx",
        "python-versions",
        "venv",
        "development-tools",
    ],
    packages=find_packages(exclude=["tests", "tests.*", "docs", "examples"]),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "pyxenv=pyxenv.cli:main",
        ],
    },
    python_requires=">=3.8",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    zip_safe=False,
)