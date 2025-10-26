"""Setup configuration for pypx package."""
from pathlib import Path
from setuptools import setup, find_packages

readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

version = "0.2.0"

setup(
    name="pypx",
    version=version,
    description="npx-like tool for Python: switch versions and manage virtual environments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Luigi C. Filho",
    author_email="lcdev@lcdesenvolvimentos.com.br",
    url="https://github.com/luigicfilho/pypx",
    project_urls={
        "Bug Tracker": "https://github.com/luigicfilho/pypx/issues",
        "Documentation": "https://github.com/luigicfilho/pypx#readme",
        "Source Code": "https://github.com/luigicfilho/pypx",
        "Changelog": "https://github.com/luigicfilho/pypx/blob/main/CHANGELOG.md",
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
            "pypx=pypx.cli:main",
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
    # # Dependencies
    # python_requires=">=3.8",
    # install_requires=[
    #     # Adicione suas dependências aqui
    #     # Exemplo: "requests>=2.28.0",
    # ],
    # extras_require={
    #     "dev": [
    #         "pytest>=7.0.0",
    #         "pytest-cov>=4.0.0",
    #         "black>=23.0.0",
    #         "flake8>=6.0.0",
    #         "mypy>=1.0.0",
    #         "isort>=5.12.0",
    #     ],
    #     "docs": [
    #         "sphinx>=5.0.0",
    #         "sphinx-rtd-theme>=1.2.0",
    #     ],
    # },
    # classifiers=[
    #     # Development Status
    #     "Development Status :: 3 - Alpha",
        
    #     # Intended Audience
    #     "Intended Audience :: Developers",
    #     "Intended Audience :: System Administrators",
        
    #     # Topic
    #     "Topic :: Software Development :: Build Tools",
    #     "Topic :: Software Development :: Libraries :: Python Modules",
    #     "Topic :: System :: Installation/Setup",
        
    #     # License
    #     "License :: OSI Approved :: MIT License",
        
    #     # Python versions
    #     "Programming Language :: Python :: 3",
    #     "Programming Language :: Python :: 3.8",
    #     "Programming Language :: Python :: 3.9",
    #     "Programming Language :: Python :: 3.10",
    #     "Programming Language :: Python :: 3.11",
    #     "Programming Language :: Python :: 3.12",
    #     "Programming Language :: Python :: 3.13",
        
    #     # OS
    #     "Operating System :: OS Independent",
    #     "Operating System :: POSIX :: Linux",
    #     "Operating System :: MacOS",
    #     "Operating System :: Microsoft :: Windows",
        
    #     # Other
    #     "Environment :: Console",
    #     "Natural Language :: English",
    #     "Typing :: Typed",
    # ],
)