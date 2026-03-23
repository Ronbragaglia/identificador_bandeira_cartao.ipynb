# Guia de Instalação

Este guia detalha como instalar e configurar o Card Brand Identifier em diferentes ambientes.

## 📋 Requisitos do Sistema

### Python
- Python 3.8 ou superior
- pip (geralmente incluído com Python)

### Sistema Operacional
- Windows 10 ou superior
- macOS 10.14 ou superior
- Linux (qualquer distribuição moderna)

## 🚀 Métodos de Instalação

### Método 1: pip (Recomendado)

A forma mais simples de instalar o Card Brand Identifier é usando pip:

```bash
pip install card-brand-identifier
```

#### Instalação com versão específica

```bash
pip install card-brand-identifier==1.0.0
```

#### Atualização

```bash
pip install --upgrade card-brand-identifier
```

### Método 2: Poetry

Se você usa Poetry para gerenciamento de dependências:

```bash
poetry add card-brand-identifier
```

#### Instalar com dependências de desenvolvimento

```bash
poetry add card-brand-identifier --dev
```

### Método 3: pipenv

Se você usa pipenv:

```bash
pipenv install card-brand-identifier
```

#### Instalar com dependências de desenvolvimento

```bash
pipenv install card-brand-identifier --dev
```

### Método 4: Do Código Fonte

Para instalar a versão mais recente do código fonte:

```bash
# Clone o repositório
git clone https://github.com/Ronbragaglia/identificador_bandeira_cartao.git
cd identificador_bandeira_cartao

# Instale em modo de desenvolvimento
pip install -e .

# Ou instale com todas as dependências
pip install -e ".[all]"
```

### Método 5: Docker

Para usar o Card Brand Identifier em um container Docker:

```bash
# Construa a imagem
docker build -t card-brand-identifier .

# Execute o container
docker run --rm card-brand-identifier

# Execute com argumentos
docker run --rm card-brand-identify 4111111111111111
```

#### Usando Docker Compose

```bash
# Inicie o serviço
docker-compose up -d

# Execute testes
docker-compose --profile tests up

# Execute exemplos
docker-compose --profile examples up
```

## 🔧 Configuração do Ambiente de Desenvolvimento

### Passo 1: Clone o Repositório

```bash
git clone https://github.com/Ronbragaglia/identificador_bandeira_cartao.git
cd identificador_bandeira_cartao
```

### Passo 2: Crie um Ambiente Virtual

#### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows

```cmd
python -m venv .venv
.venv\Scripts\activate
```

#### PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### Passo 3: Instale as Dependências

```bash
# Instale apenas o pacote
pip install -e .

# Instale com dependências de desenvolvimento
pip install -e ".[dev]"

# Instale com todas as dependências
pip install -e ".[all]"
```

### Passo 4: Verifique a Instalação

```bash
# Verifique se o pacote está instalado
python -c "import card_brand_identifier; print(card_brand_identifier.__version__)"

# Execute a CLI
card-identify --help

# Execute os testes
pytest
```

## 📦 Dependências

### Dependências Principais

O Card Brand Identifier não tem dependências externas. Ele usa apenas bibliotecas padrão do Python:
- `re` - Para expressões regulares
- `dataclasses` - Para a classe CardInfo
- `typing` - Para type hints

### Dependências de Desenvolvimento

- `pytest` - Framework de testes
- `pytest-cov` - Cobertura de código
- `black` - Formatação de código
- `flake8` - Linting
- `isort` - Ordenação de imports
- `mypy` - Verificação de tipos
- `pre-commit` - Hooks de pre-commit

## 🐛 Solução de Problemas

### Erro: "No module named 'card_brand_identifier'"

**Solução:**
```bash
# Verifique se o pacote está instalado
pip list | grep card-brand-identifier

# Reinstale se necessário
pip install --force-reinstall card-brand-identifier
```

### Erro: "Permission denied" ao instalar

**Solução:**
```bash
# Use --user para instalar no diretório do usuário
pip install --user card-brand-identifier

# Ou use um ambiente virtual
python -m venv .venv
source .venv/bin/activate
pip install card-brand-identifier
```

### Erro: "Python not found"

**Solução:**
```bash
# Verifique se o Python está instalado
python --version

# Se não estiver, instale o Python 3.8+
# Windows: https://www.python.org/downloads/
# macOS: brew install python3
# Linux: sudo apt-get install python3
```

### Erro: "pip not found"

**Solução:**
```bash
# Verifique se o pip está instalado
python -m pip --version

# Se não estiver, instale o pip
python -m ensurepip --upgrade
```

## ✅ Verificação da Instalação

Após a instalação, você pode verificar se tudo está funcionando corretamente:

```bash
# Teste a importação
python -c "from card_brand_identifier import identify_brand; print(identify_brand('4111111111111111'))"

# Teste a CLI
card-identify 4111111111111111

# Execute os testes
pytest tests/ -v

# Execute os exemplos
python examples/basic_usage.py
```

## 🔄 Atualização

Para atualizar para a versão mais recente:

```bash
pip install --upgrade card-brand-identifier
```

Para atualizar do código fonte:

```bash
cd identificador_bandeira_cartao
git pull origin main
pip install -e ".[all]"
```

## 🗑️ Desinstalação

Para remover o Card Brand Identifier:

```bash
pip uninstall card-brand-identifier
```

## 📚 Próximos Passos

Após a instalação, você pode:

- Ler o [Guia de Uso](./usage.md)
- Ver os [Exemplos](../examples/)
- Consultar a [Documentação da API](./index.md#api-reference)
- Contribuir com o projeto no [GitHub](https://github.com/Ronbragaglia/identificador_bandeira_cartao)
