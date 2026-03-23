# Troubleshooting

Este guia ajuda a resolver problemas comuns ao usar o Card Brand Identifier.

## 📋 Índice

- [Problemas de Instalação](#problemas-de-instalação)
- [Problemas de Execução](#problemas-de-execução)
- [Problemas de Validação](#problemas-de-validação)
- [Problemas de Performance](#problemas-de-performance)
- [Outros Problemas](#outros-problemas)

## 🔧 Problemas de Instalação

### Erro: "No module named 'card_brand_identifier'"

**Sintoma:**
```python
ImportError: No module named 'card_brand_identifier'
```

**Causa:** O pacote não foi instalado corretamente.

**Solução:**
```bash
# Verifique se o pacote está instalado
pip list | grep card-brand-identifier

# Reinstale o pacote
pip uninstall card-brand-identifier
pip install card-brand-identifier

# Se estiver em modo de desenvolvimento
cd /caminho/do/projeto
pip install -e .
```

### Erro: "Permission denied"

**Sintoma:**
```
PermissionError: [Errno 13] Permission denied
```

**Causa:** Permissões insuficientes para instalar pacotes.

**Solução:**
```bash
# Opção 1: Use --user
pip install --user card-brand-identifier

# Opção 2: Use um ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate  # Windows
pip install card-brand-identifier

# Opção 3: Use sudo (não recomendado)
sudo pip install card-brand-identifier
```

### Erro: "Python version not supported"

**Sintoma:**
```
Package requires a different Python version
```

**Causa:** Versão do Python incompatível.

**Solução:**
```bash
# Verifique sua versão do Python
python --version

# O Card Brand Identifier requer Python 3.8+
# Instale uma versão compatível se necessário

# Windows: https://www.python.org/downloads/
# macOS: brew install python3
# Linux: sudo apt-get install python3.8
```

### Erro: "pip not found"

**Sintoma:**
```
Command 'pip' not found
```

**Causa:** pip não está instalado.

**Solução:**
```bash
# Instale o pip
python -m ensurepip --upgrade

# Ou use o instalador oficial
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

## 🏃 Problemas de Execução

### Erro: "ModuleNotFoundError: No module named 'pytest'"

**Sintoma:**
```python
ModuleNotFoundError: No module named 'pytest'
```

**Causa:** Dependências de desenvolvimento não instaladas.

**Solução:**
```bash
# Instale dependências de desenvolvimento
pip install -e ".[dev]"

# Ou instale pytest separadamente
pip install pytest pytest-cov
```

### Erro: "AttributeError: module 'card_brand_identifier' has no attribute"

**Sintoma:**
```python
AttributeError: module 'card_brand_identifier' has no attribute 'identify_brand'
```

**Causa:** Importação incorreta ou versão antiga.

**Solução:**
```python
# ❌ Incorreto
from card_brand_identifier import validator
validator.identify_brand("4111111111111111")

# ✅ Correto
from card_brand_identifier import identify_brand
identify_brand("4111111111111111")

# Ou
from card_brand_identifier.validator import identify_brand
identify_brand("4111111111111111")
```

### Erro: "Command not found: card-identify"

**Sintoma:**
```
bash: card-identify: command not found
```

**Causa:** CLI não instalada ou PATH não configurado.

**Solução:**
```bash
# Reinstale o pacote
pip install --force-reinstall card-brand-identifier

# Verifique onde o CLI está instalado
python -m card_brand_identifier.cli --help

# Ou use python -m
python -m card_brand_identifier.cli 4111111111111111
```

## ✅ Problemas de Validação

### Cartão Válido Mas Bandeira Não Identificada

**Sintoma:**
```python
info = identify_brand("1234567890123456")
# brand=None, valid_luhn=True
```

**Causa:** Número válido pelo Luhn mas não corresponde a nenhuma bandeira suportada.

**Solução:**
```python
# Verifique se a bandeira é suportada
from card_brand_identifier import SUPPORTED_BRANDS_ORDER
print(SUPPORTED_BRANDS_ORDER)

# Verifique o número normalizado
info = identify_brand("1234567890123456")
print(info.normalized)

# Considere adicionar suporte para novas bandeiras
```

### Cartão Inválido Mas Bandeira Identificada

**Sintoma:**
```python
info = identify_brand("4111111111111112")
# brand='visa', valid_luhn=False
```

**Causa:** Padrão de bandeira correto mas falha na validação Luhn.

**Solução:**
```python
# Identifique sem validar Luhn
info = identify_brand("4111111111111112", validate_luhn=False)
# brand='visa', valid_luhn=False

# Valide separadamente
from card_brand_identifier import luhn_check
is_valid = luhn_check("4111111111111112")
print(is_valid)  # False
```

### Números Formulados Não São Reconhecidos

**Sintoma:**
```python
info = identify_brand("4111-1111-1111-1111")
# brand=None
```

**Causa:** Formatação não suportada.

**Solução:**
```python
# O Card Brand Identifier remove espaços e hífens automaticamente
# Se não funcionar, normalize manualmente
import re
normalized = re.sub(r"\D", "", "4111-1111-1111-1111")
info = identify_brand(normalized)
```

## ⚡ Problemas de Performance

### Processamento Lento de Muitos Cartões

**Sintoma:** Processar milhares de cartões demora muito.

**Solução:**
```python
from card_brand_identifier import identify_brand
from concurrent.futures import ThreadPoolExecutor

def process_card(card_number):
    """Processa um único cartão."""
    return identify_brand(card_number)

# Use processamento paralelo
cards = ["4111111111111111"] * 10000

with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(process_card, cards))
```

### Alto Uso de Memória

**Sintoma:** Processar muitos cartões consome muita memória.

**Solução:**
```python
from card_brand_identifier import identify_brand

# Use geradores em vez de listas
def process_cards(card_numbers):
    """Processa cartões em lote."""
    for card in card_numbers:
        yield identify_brand(card)

# Processar em chunks
def process_in_chunks(cards, chunk_size=1000):
    """Processa em chunks para economizar memória."""
    for i in range(0, len(cards), chunk_size):
        chunk = cards[i:i + chunk_size]
        yield from process_cards(chunk)
```

## 🌐 Outros Problemas

### Problemas com Codificação

**Sintoma:** Caracteres especiais não são processados corretamente.

**Solução:**
```python
# Use UTF-8 ao ler/escrever arquivos
with open('cards.txt', 'r', encoding='utf-8') as f:
    cards = f.readlines()

# Normalize antes de processar
import re
normalized = re.sub(r"\D", "", card_number)
```

### Problemas com Docker

**Sintoma:** Container Docker não funciona.

**Solução:**
```bash
# Reconstrua a imagem
docker build --no-cache -t card-brand-identifier .

# Verifique os logs
docker logs card-identifier-app

# Execute em modo interativo
docker run -it card-brand-identifier bash

# Verifique se o Python está instalado
docker run card-brand-identifier python --version
```

### Problemas com Testes

**Sintoma:** Testes falham aleatoriamente.

**Solução:**
```bash
# Execute testes com verbose
pytest tests/ -v

# Execute testes específicos
pytest tests/test_validator.py::TestLuhnCheck::test_valid_visa_numbers -v

# Execute com coverage
pytest tests/ --cov=src --cov-report=html

# Limpe o cache
pytest --cache-clear
```

### Problemas com Pre-commit

**Sintoma:** Hooks de pre-commit falham.

**Solução:**
```bash
# Reinstale os hooks
pre-commit uninstall
pre-commit install

# Execute manualmente
pre-commit run --all-files

# Pule hooks (não recomendado)
git commit --no-verify
```

## 📞 Obter Ajuda

Se você não conseguir resolver seu problema:

1. **Verifique a Documentação**
   - [Guia de Instalação](./installation.md)
   - [Guia de Uso](./usage.md)
   - [API Reference](./index.md#api-reference)

2. **Pesquise Issues**
   - [GitHub Issues](https://github.com/Ronbragaglia/identificador_bandeira_cartao/issues)

3. **Abra uma Issue**
   - Descreva o problema detalhadamente
   - Inclua código de exemplo
   - Informe sua versão do Python e do pacote
   - Inclua o traceback completo

4. **Contato**
   - Email: ronbragaglia@gmail.com
   - GitHub: [@Ronbragaglia](https://github.com/Ronbragaglia)

## 🔍 Debugging

### Ativar Logging

```python
import logging
logging.basicConfig(level=logging.DEBUG)

from card_brand_identifier import identify_brand
info = identify_brand("4111111111111111")
```

### Verificar Versão

```python
import card_brand_identifier
print(card_brand_identifier.__version__)

# Ou via CLI
card-identify --version
```

### Testar Isoladamente

```python
# Teste em um script isolado
from card_brand_identifier import identify_brand, luhn_check

# Teste Luhn
print(luhn_check("4111111111111111"))  # True

# Teste identificação
info = identify_brand("4111111111111111")
print(info.brand)  # visa
```

## 📚 Recursos Adicionais

- [Documentação Principal](./index.md)
- [Exemplos de Código](../examples/)
- [Contribuindo](https://github.com/Ronbragaglia/identificador_bandeira_cartao/blob/main/CONTRIBUTING.md)
- [Licença](../LICENSE)
