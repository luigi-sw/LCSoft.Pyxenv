# pypx 🐍 - Python Version/Environment Manager

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> **npx para Python** - Gerencie versões do Python e ambientes virtuais com facilidade

`pypx` é uma ferramenta de linha de comando inspirada no `npx` do Node.js, projetada para simplificar o gerenciamento de múltiplas versões do Python e ambientes virtuais.

## Características

- **Troca rápida de versões** - Execute scripts com diferentes versões do Python
- **Instalação automática** - Baixa e instala versões do Python automaticamente (Windows)
- **Gerenciamento de venvs** - Crie e ative ambientes virtuais facilmente
- **Detecção inteligente** - Lista todas as versões Python disponíveis
- **Multi-plataforma** - Suporte para Windows, Linux e macOS
- **Zero configuração** - Funciona imediatamente após a instalação

## Instalação

### Via pip (recomendado)

```bash
pip install pypx
```

### Via GitHub

```bash
git clone https://github.com/luigicfilho/pypx.git
cd pypx
pip install -e .
```

### Desenvolvimento

```bash
git clone https://github.com/luigicfilho/pypx.git
cd pypx
pip install -e ".[dev]"
```

## Uso Rápido

### Executar script com versão específica

```bash
# Executa script.py com Python 3.11
pypx 3.11 script.py

# Com argumentos
pypx 3.11 script.py --arg1 value1 --arg2 value2
```

### Gerenciar versões do Python

```bash
# Listar versões instaladas pelo pypx
pypx --list

# Listar todas as versões (incluindo globais)
pypx --list-all

# Instalar automaticamente (Windows)
pypx 3.12 script.py  # Instala 3.12 se não existir
```

### Gerenciar ambientes virtuais

```bash
# Criar ambiente virtual
pypx 3.11 --create-env meu-projeto

# Criar com nome padrão (pypx-3.11)
pypx 3.11 --create-env

# Ativar ambiente
pypx --activate meu-projeto

# Listar ambientes
pypx --list-envs
```

## Exemplos

### Desenvolvimento multi-versão

```bash
# Testar seu código em diferentes versões
pypx 3.8 test_script.py
pypx 3.9 test_script.py
pypx 3.11 test_script.py
pypx 3.12 test_script.py
```

### Projetos isolados

```bash
# Projeto Django com Python 3.11
pypx 3.11 --create-env django-project
pypx --activate django-project
pip install django
django-admin startproject mysite

# Projeto FastAPI com Python 3.12
pypx 3.12 --create-env fastapi-project
pypx --activate fastapi-project
pip install fastapi uvicorn
```

### CI/CD

```yaml
# .github/workflows/test.yml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: windows-latest
    strategy:
      matrix:
        python-version: ['3.8', '3.9', '3.10', '3.11', '3.12']
    
    steps:
      - uses: actions/checkout@v3
      - name: Install pypx
        run: pip install pypx
      - name: Run tests
        run: pypx ${{ matrix.python-version }} -m pytest
```

## Comandos

| Comando | Descrição |
|---------|-----------|
| `pypx <version> <script>` | Executa script com versão específica |
| `pypx --list` | Lista versões instaladas pelo pypx |
| `pypx --list-all` | Lista todas as versões detectadas |
| `pypx --create-env <name>` | Cria ambiente virtual |
| `pypx --activate <name>` | Ativa ambiente virtual |
| `pypx --list-envs` | Lista ambientes criados |
| `pypx --version` | Mostra versão do pypx |

## Estrutura de Diretórios

```
~/.pypx/
├── pythons/          # Versões Python instaladas
│   ├── 3.8.10/
│   ├── 3.11.5/
│   └── 3.12.0/
└── envs/             # Ambientes virtuais
    ├── my-project/
    ├── django-app/
    └── pypx-3.11/
```

## Configuração

pypx funciona sem configuração, mas você pode personalizar:

```python
# ~/.pypx/config.py (opcional)
PYPX_HOME = Path.home() / ".pypx"
PYTHON_DIR = PYPX_HOME / "pythons"
ENV_DIR = PYPX_HOME / "envs"
```

## Troubleshooting

### Python não encontrado

```bash
# Verificar versões disponíveis
pypx --list-all

# Instalar versão específica (Windows)
pypx 3.11 --version  # Instala automaticamente
```

### Ambiente virtual não ativa

```bash
# Verificar se existe
pypx --list-envs

# Recriar se necessário
pypx 3.11 --create-env nome-do-env
```

### Permissões no Windows

Execute o PowerShell como Administrador para instalações automáticas.

## Contribuindo

Contribuições são bem-vindas! Veja [CONTRIBUTING.md](CONTRIBUTING.md) para detalhes.

### Setup de desenvolvimento

```bash
# Clone o repositório
git clone https://github.com/luigicfilho/pypx.git
cd pypx

# Instale dependências de desenvolvimento
pip install -e ".[dev]"

# Instale pre-commit hooks
pre-commit install

# Execute os testes
pytest

# Verifique cobertura
pytest --cov=pypx --cov-report=html
```

### Executar testes

```bash
# Todos os testes
pytest

# Testes específicos
pytest tests/test_cli.py

# Com output verboso
pytest -vv

# Com cobertura
pytest --cov=pypx --cov-report=term-missing
```

### Code style

```bash
# Formatar código
black pypx tests

# Organizar imports
isort pypx tests

# Verificar estilo
flake8 pypx tests

# Type checking
mypy pypx
```

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Autor

**Luigi C. Filho**

- Email: lcdev@lcdesenvolvimentos.com.br
- GitHub: [@luigicfilho](https://github.com/luigicfilho)

## Agradecimentos

- Inspirado pelo [npx](https://github.com/npm/npx) do Node.js
- Comunidade Python pela excelente documentação

## Status do Projeto

- ✅ Detecção de versões Python
- ✅ Gerenciamento de ambientes virtuais
- ✅ Instalação automática (Windows)
- 🚧 Instalação automática (Linux/macOS) - Em desenvolvimento
- 🚧 Cache de downloads - Planejado
- 🚧 Atualização automática - Planejado

## Links Úteis

- [Documentação](https://github.com/luigicfilho/pypx#readme)
- [Issues](https://github.com/luigicfilho/pypx/issues)
- [Changelog](CHANGELOG.md)
- [Guia de Contribuição](CONTRIBUTING.md)

## Roadmap

### v0.4.0
- [ ] Suporte a pyenv
- [ ] Instalação automática no Linux/macOS
- [ ] Cache de instaladores

### v0.5.0
- [ ] Interface TUI interativa
- [ ] Configuração por projeto (.pypxrc)
- [ ] Integração com Docker

### v1.0.0
- [ ] API estável
- [ ] Documentação completa
- [ ] Pacote no PyPI verificado

## Inspiração e Alternativas

- **pyenv** - Gerenciador de versões Python completo
- **virtualenv** - Criação de ambientes virtuais
- **pipx** - Instala e executa aplicações Python
- **conda** - Gerenciador de pacotes e ambientes

`pypx` combina o melhor desses mundos com a simplicidade do `npx`!

## Star History

Se este projeto foi útil para você, considere dar uma ⭐!

[![Star History Chart](https://api.star-history.com/svg?repos=luigicfilho/pypx&type=Date)](https://star-history.com/#luigicfilho/pypx&Date)

---

<div align="center">
  
**Feito com ❤️ por [Luigi C. Filho](https://github.com/luigicfilho)**

[⬆ Voltar ao topo](#pypx-)

</div>

#
   
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   quickstart
   changelog
   api
   .. modules

.. toctree::
   :maxdepth: 2
   :caption: API Reference:

   modules


cmds
pip install build
python -m build
pip install pyinstaller
pyinstaller --onefile --name pypx pypx/cli.py
pip install cx_Freeze
python setup_cx.py bdist_msi
pip install sphinx sphinx-rtd-theme
sphinx-quickstart docs
sphinx-apidoc -o docs/source pypx
make html
make clean
