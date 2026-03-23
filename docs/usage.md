# Guia de Uso

Este guia detalha como usar o Card Brand Identifier em diferentes cenários.

## 📋 Índice

- [Uso Básico](#uso-básico)
- [Uso Avançado](#uso-avançado)
- [Uso da CLI](#uso-da-cli)
- [Casos de Uso Comuns](#casos-de-uso-comuns)
- [Melhores Práticas](#melhores-práticas)

## 🎯 Uso Básico

### Importar e Identificar

```python
from card_brand_identifier import identify_brand

# Identificar um cartão
info = identify_brand("4111 1111 1111 1111")

print(f"Bandeira: {info.brand}")  # visa
print(f"Válido: {info.valid_luhn}")  # True
print(f"Normalizado: {info.normalized}")  # 4111111111111111
print(f"Dígitos: {info.length}")  # 16
```

### Validar com Luhn

```python
from card_brand_identifier import luhn_check

# Validar um número
is_valid = luhn_check("4111111111111111")
print(is_valid)  # True

# Validar número inválido
is_invalid = luhn_check("4111111111111112")
print(is_invalid)  # False
```

### Descrever Resultado

```python
from card_brand_identifier import identify_brand, describe_result

info = identify_brand("5555 5555 5555 4444")
description = describe_result(info)
print(description)
# Bandeira: mastercard | Luhn: válido | Dígitos: 16 | Número: 5555555555554444
```

## 🚀 Uso Avançado

### Identificação sem Validação Luhn

```python
from card_brand_identifier import identify_brand

# Identificar sem validar Luhn
info = identify_brand("4111111111111112", validate_luhn=False)
print(f"Bandeira: {info.brand}")  # visa
print(f"Válido: {info.valid_luhn}")  # False
```

### Processamento em Lote

```python
from card_brand_identifier import identify_brand

# Lista de cartões
cards = [
    "4111111111111111",
    "5555555555554444",
    "378282246310005",
    "30569309025904",
]

# Processar todos
results = []
for card in cards:
    info = identify_brand(card)
    results.append({
        "number": card,
        "brand": info.brand,
        "valid": info.valid_luhn,
    })

# Exibir resultados
for result in results:
    print(f"{result['number']}: {result['brand']} ({'✓' if result['valid'] else '✗'})")
```

### Filtrar por Bandeira

```python
from card_brand_identifier import identify_brand

# Lista mista de cartões
cards = [
    "4111111111111111",  # Visa
    "5555555555554444",  # MasterCard
    "4012888888881881",  # Visa
    "5105105105105100",  # MasterCard
]

# Filtrar apenas Visa
visa_cards = [
    card for card in cards
    if identify_brand(card).brand == "visa"
]

print(f"Cartões Visa: {visa_cards}")
# ['4111111111111111', '4012888888881881']
```

### Validação Personalizada

```python
from card_brand_identifier import identify_brand

def validate_credit_card(number: str) -> dict:
    """Valida um cartão com critérios personalizados."""
    info = identify_brand(number)

    # Critérios de validação
    if not info.normalized:
        return {"valid": False, "error": "Número vazio"}

    if info.length < 13 or info.length > 19:
        return {"valid": False, "error": "Comprimento inválido"}

    if not info.valid_luhn:
        return {"valid": False, "error": "Número inválido"}

    if not info.brand:
        return {"valid": False, "error": "Bandeira não suportada"}

    return {
        "valid": True,
        "brand": info.brand,
        "last_four": info.normalized[-4:]
    }

# Uso
result = validate_credit_card("4111 1111 1111 1111")
print(result)
# {'valid': True, 'brand': 'visa', 'last_four': '1111'}
```

## 💻 Uso da CLI

### Comandos Básicos

```bash
# Identificar um cartão
card-identify 4111111111111111

# Ver bandeiras suportadas
card-identify --brands

# Executar testes
card-identify --test

# Ver ajuda
card-identify --help
```

### Modo Verbose

```bash
# Ver informações detalhadas
card-identify 4111111111111111 --verbose
```

Saída:
```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║          🏦 Card Brand Identifier v1.0.0 🏦                  ║
║      Identificador de Bandeira de Cartão de Crédito           ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝

📊 Informações Detalhadas:
──────────────────────────────────────────────────
  Número original: 4111111111111111
  Número normalizado: 4111111111111111
  Quantidade de dígitos: 16
  Bandeira: visa
  Validação Luhn: ✅ Válido
──────────────────────────────────────────────────

💳 Bandeira: visa | Luhn: válido | Dígitos: 16 | Número: 4111111111111111
```

### Modo Interativo

```bash
# Iniciar modo interativo
card-identify --interactive
```

No modo interativo, você pode:
- Digitar números de cartão para identificar
- Digitar `testes` para executar testes
- Digitar `help` para ver a ajuda
- Digitar `sair` ou `exit` para encerrar

### Sem Banner

```bash
# Executar sem mostrar o banner
card-identify --no-banner 4111111111111111
```

## 🎯 Casos de Uso Comuns

### Validação de Formulário

```python
from card_brand_identifier import identify_brand

def validate_form_card(number: str) -> tuple[bool, str]:
    """Valida um cartão em um formulário web."""
    info = identify_brand(number)

    if not info.normalized:
        return False, "Por favor, insira um número de cartão"

    if not info.valid_luhn:
        return False, "Número de cartão inválido"

    if not info.brand:
        return False, "Bandeira de cartão não suportada"

    return True, f"Cartão {info.brand} válido"
```

### Processamento de Pagamentos

```python
from card_brand_identifier import identify_brand

def process_payment(card_number: str, amount: float) -> dict:
    """Processa um pagamento."""
    info = identify_brand(card_number)

    if not info.valid_luhn:
        return {
            "success": False,
            "error": "Número de cartão inválido"
        }

    # Processar pagamento (simulado)
    return {
        "success": True,
        "brand": info.brand,
        "amount": amount,
        "last_four": info.normalized[-4:]
    }

# Uso
result = process_payment("4111111111111111", 100.00)
print(result)
```

### Análise de Dados

```python
from card_brand_identifier import identify_brand
from collections import Counter

# Lista de transações
transactions = [
    {"card": "4111111111111111", "amount": 100.00},
    {"card": "5555555555554444", "amount": 200.00},
    {"card": "4111111111111111", "amount": 150.00},
]

# Analisar por bandeira
brands = []
for tx in transactions:
    info = identify_brand(tx["card"])
    brands.append(info.brand)

# Contar por bandeira
brand_counts = Counter(brands)
print(brand_counts)
# Counter({'visa': 2, 'mastercard': 1})
```

### Integração com API

```python
from fastapi import FastAPI
from card_brand_identifier import identify_brand
from pydantic import BaseModel

app = FastAPI()

class CardRequest(BaseModel):
    card_number: str

@app.post("/validate")
def validate_card(request: CardRequest):
    """Endpoint para validar cartão."""
    info = identify_brand(request.card_number)

    return {
        "brand": info.brand,
        "valid": info.valid_luhn,
        "normalized": info.normalized,
        "length": info.length
    }
```

## 💡 Melhores Práticas

### 1. Sempre Normalize o Número

```python
from card_brand_identifier import identify_brand

# ❌ Ruim - usa o número original
info = identify_brand("4111 1111 1111 1111")
user_input = "4111 1111 1111 1111"

# ✅ Bom - usa o número normalizado
info = identify_brand(user_input)
normalized_number = info.normalized
```

### 2. Valide Antes de Processar

```python
from card_brand_identifier import identify_brand

def process_card(number: str):
    """Processa um cartão com validação."""
    info = identify_brand(number)

    # Valide antes de processar
    if not info.valid_luhn:
        raise ValueError("Número de cartão inválido")

    if not info.brand:
        raise ValueError("Bandeira não suportada")

    # Processar o cartão
    # ...
```

### 3. Trate Erros Adequadamente

```python
from card_brand_identifier import identify_brand

def safe_identify(number: str) -> dict:
    """Identifica com tratamento de erros."""
    try:
        info = identify_brand(number)
        return {
            "success": True,
            "brand": info.brand,
            "valid": info.valid_luhn
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
```

### 4. Use Números de Teste

```python
from card_brand_identifier import get_test_numbers, identify_brand

# Obter números de teste para uma bandeira específica
visa_tests = get_test_numbers("visa")

# Testar todos
for number in visa_tests:
    info = identify_brand(number)
    assert info.brand == "visa"
    assert info.valid_luhn
```

### 5. Documente Seu Código

```python
from card_brand_identifier import identify_brand

def validate_payment_card(card_number: str) -> dict:
    """
    Valida um cartão de pagamento.

    Args:
        card_number: Número do cartão (pode conter espaços ou hífens)

    Returns:
        Dicionário com informações de validação:
        - valid (bool): Se o cartão é válido
        - brand (str): Bandeira identificada
        - last_four (str): Últimos 4 dígitos

    Raises:
        ValueError: Se o número for inválido

    Example:
        >>> validate_payment_card("4111 1111 1111 1111")
        {'valid': True, 'brand': 'visa', 'last_four': '1111'}
    """
    info = identify_brand(card_number)

    if not info.valid_luhn:
        raise ValueError("Número de cartão inválido")

    return {
        "valid": True,
        "brand": info.brand,
        "last_four": info.normalized[-4:]
    }
```

## 📚 Recursos Adicionais

- [Exemplos Básicos](../examples/basic_usage.py)
- [Exemplos Avançados](../examples/advanced_usage.py)
- [API Reference](./index.md#api-reference)
- [Troubleshooting](./troubleshooting.md)
