# Pyxenv 🐍 - Python Version/Environment Manager

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)


> **npx para Python** - Gerencie versões do Python e ambientes virtuais com facilidade

`Pyxenv` é uma ferramenta de linha de comando inspirada no `npx` do Node.js, projetada para simplificar o gerenciamento de múltiplas versões do Python e ambientes virtuais.

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
pip install pyxenv
```

### Via GitHub

```bash
git clone https://github.com/luigicfilho/pyxenv.git
cd pyxenv
pip install -e .
```

## Uso Rápido

### Executar script com versão específica

```bash
# Executa script.py com Python 3.11
pyxenv 3.11 script.py

# Com argumentos
pyxenv 3.11 script.py --arg1 value1 --arg2 value2
```

### Gerenciar versões do Python

```bash
# Listar versões instaladas pelo pyxenv
pyxenv --list

# Listar todas as versões (incluindo globais)
pyxenv --list-all

# Instalar automaticamente (Windows)
pyxenv 3.12 script.py  # Instala 3.12 se não existir
```

### Gerenciar ambientes virtuais

```bash
# Criar ambiente virtual
pyxenv 3.11 --create-env meu-projeto

# Criar com nome padrão (pyxenv-3.11)
pyxenv 3.11 --create-env

# Ativar ambiente
pyxenv --activate meu-projeto

# Listar ambientes
pyxenv --list-envs
```

## Exemplos

### Desenvolvimento multi-versão

```bash
# Testar seu código em diferentes versões
pyxenv 3.8 test_script.py
pyxenv 3.9 test_script.py
pyxenv 3.11 test_script.py
pyxenv 3.12 test_script.py
```

### Projetos isolados

```bash
# Projeto Django com Python 3.11
pyxenv 3.11 --create-env django-project
pyxenv --activate django-project
pip install django
django-admin startproject mysite

# Projeto FastAPI com Python 3.12
pyxenv 3.12 --create-env fastapi-project
pyxenv --activate fastapi-project
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
      - name: Install pyxenv
        run: pip install pyxenv
      - name: Run tests
        run: pyxenv ${{ matrix.python-version }} -m pytest
```

## Comandos

| Comando | Descrição |
|---------|-----------|
| `pyxenv <version> <script>` | Executa script com versão específica |
| `pyxenv --list` | Lista versões instaladas pelo pyxenv |
| `pyxenv --list-all` | Lista todas as versões detectadas |
| `pyxenv --create-env <name>` | Cria ambiente virtual |
| `pyxenv --activate <name>` | Ativa ambiente virtual |
| `pyxenv --list-envs` | Lista ambientes criados |
| `pyxenv --version` | Mostra versão do pyxenv |

## Estrutura de Diretórios

```
~/.pyxenv/
├── pythons/          # Versões Python instaladas
│   ├── 3.8.10/
│   ├── 3.11.5/
│   └── 3.12.0/
└── envs/             # Ambientes virtuais
    ├── my-project/
    ├── django-app/
    └── pyxenv-3.11/
```

## Configuração

pyxenv funciona sem configuração, mas você pode personalizar:

```python
# ~/.pyxenv/config.py (opcional)
pyxenv_HOME = Path.home() / ".pyxenv"
PYTHON_DIR = pyxenv_HOME / "pythons"
ENV_DIR = pyxenv_HOME / "envs"
```

## Troubleshooting

### Python não encontrado

```bash
# Verificar versões disponíveis
pyxenv --list-all

# Instalar versão específica (Windows)
pyxenv 3.11 --version  # Instala automaticamente
```

### Ambiente virtual não ativa

```bash
# Verificar se existe
pyxenv --list-envs

# Recriar se necessário
pyxenv 3.11 --create-env nome-do-env
```

## Contribuindo

Contribuições são bem-vindas! Veja [CONTRIBUTING.md](CONTRIBUTING.md) para detalhes.

### Setup de desenvolvimento

```bash
# Clone o repositório
git clone https://github.com/luigicfilho/pyxenv.git
cd pyxenv

# Instale dependências de desenvolvimento
pip install -e .

# Execute os testes
pytest

# Verifique cobertura
pytest --cov=pyxenv --cov-report=html
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
pytest --cov=pyxenv --cov-report=term-missing
```

### Code style

```bash
# Formatar código
black pyxenv tests

# Organizar imports
isort pyxenv tests

# Verificar estilo
flake8 pyxenv tests

# Type checking
mypy pyxenv
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

- [x] Detecção de versões Python
- [x] Gerenciamento de ambientes virtuais
- [x] Instalação automática (Windows)
- [ ] Instalação automática (Linux/macOS) - Em desenvolvimento
- [ ] Cache de downloads - Planejado
- [ ] Atualização automática - Planejado

## Links Úteis

- [Documentação](https://github.com/luigicfilho/pyxenv#readme)
- [Issues](https://github.com/luigicfilho/pyxenv/issues)
- [Changelog](CHANGELOG.md)
- [Guia de Contribuição](CONTRIBUTING.md)

## Roadmap

### v0.2.0
- [ ] Suporte a pyenv
- [ ] Instalação automática no Linux/macOS
- [ ] Cache de instaladores

### v0.3.0
- [ ] Interface TUI interativa
- [ ] Configuração por projeto (.pyxenvrc)
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

`pyxenv` combina o melhor desses mundos com a simplicidade do `npx`!

## Star History

Se este projeto foi útil para você, considere dar uma ⭐!

---

<div align="center">
  
**Feito com ❤️ por [Luigi C. Filho](https://github.com/luigicfilho)**

[⬆ Voltar ao topo](#pyxenv)

</div>
