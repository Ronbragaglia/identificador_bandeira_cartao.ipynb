# Card Brand Identifier

Biblioteca Python para identificação de bandeiras de cartão de crédito e validação usando o algoritmo de Luhn.

## 📋 Índice

- [Instalação](#instalação)
- [Uso Básico](#uso-básico)
- [API Reference](#api-reference)
- [Bandeiras Suportadas](#bandeiras-suportadas)
- [Exemplos](#exemplos)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

## 🚀 Instalação

### Via pip

```bash
pip install card-brand-identifier
```

### Via Poetry

```bash
poetry add card-brand-identifier
```

### Via pipenv

```bash
pipenv install card-brand-identifier
```

### Do código fonte

```bash
git clone https://github.com/Ronbragaglia/identificador_bandeira_cartao.git
cd identificador_bandeira_cartao
pip install -e .
```

## 📖 Uso Básico

### Identificar um cartão

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
```

### Usar a CLI

```bash
# Identificar um cartão
card-identify 4111111111111111

# Ver bandeiras suportadas
card-identify --brands

# Executar testes
card-identify --test

# Modo interativo
card-identify --interactive

# Ver informações detalhadas
card-identify 4111111111111111 --verbose
```

## 📚 API Reference

### `identify_brand(number: str, validate_luhn: bool = True) -> CardInfo`

Identifica a bandeira de um cartão de crédito.

**Parâmetros:**
- `number` (str): Número do cartão (pode conter espaços ou hífens)
- `validate_luhn` (bool): Se True, valida o número usando Luhn

**Retorna:**
- `CardInfo`: Objeto com informações do cartão

**Exemplo:**
```python
info = identify_brand("5555 5555 5555 4444")
# CardInfo(brand='mastercard', valid_luhn=True, normalized='5555555555554444', length=16)
```

### `luhn_check(number: str) -> bool`

Valida um número de cartão usando o algoritmo de Luhn.

**Parâmetros:**
- `number` (str): Número do cartão

**Retorna:**
- `bool`: True se válido, False caso contrário

**Exemplo:**
```python
is_valid = luhn_check("4111111111111111")
# True
```

### `CardInfo`

Classe que representa informações de um cartão.

**Atributos:**
- `brand` (Optional[str]): Nome da bandeira identificada
- `valid_luhn` (bool): True se passar na validação Luhn
- `normalized` (str): Número normalizado (apenas dígitos)
- `length` (int): Quantidade de dígitos

## 💳 Bandeiras Suportadas

| Bandeira | Prefixos | Comprimento |
|----------|-----------|-------------|
| Visa | 4 | 13, 16, 19 |
| MasterCard | 51-55, 2221-2720 | 16 |
| American Express | 34, 37 | 15 |
| Diners Club | 300-305, 36, 38 | 14 |
| Discover | 6011, 65, 644-649 | 16 |
| JCB | 2131, 1800, 35 | 16 |
| Hipercard | 3841, 606282 | 16 |
| Elo | Múltiplos prefixos | 16 |

## 🎯 Exemplos

### Exemplo 1: Validação de formulário

```python
from card_brand_identifier import identify_brand

def validate_credit_card(number: str) -> dict:
    """Valida um cartão de crédito em um formulário."""
    info = identify_brand(number)

    if not info.normalized:
        return {"valid": False, "error": "Número vazio"}

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

### Exemplo 2: Processamento em lote

```python
from card_brand_identifier import identify_brand

cards = [
    "4111111111111111",
    "5555555555554444",
    "378282246310005",
]

results = [identify_brand(card) for card in cards]

for info in results:
    print(f"{info.normalized}: {info.brand}")
```

### Exemplo 3: Filtrar por bandeira

```python
from card_brand_identifier import identify_brand

cards = [
    "4111111111111111",  # Visa
    "5555555555554444",  # MasterCard
    "4012888888881881",  # Visa
]

# Filtrar apenas cartões Visa
visa_cards = [
    card for card in cards
    if identify_brand(card).brand == "visa"
]

print(visa_cards)  # ['4111111111111111', '4012888888881881']
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Fork o repositório
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Desenvolvimento

```bash
# Clone o repositório
git clone https://github.com/Ronbragaglia/identificador_bandeira_cartao.git
cd identificador_bandeira_cartao

# Crie um ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate  # Windows

# Instale as dependências de desenvolvimento
pip install -e ".[dev]"

# Execute os testes
pytest

# Execute os exemplos
python examples/basic_usage.py
```

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](../LICENSE) para detalhes.

## 🔗 Links Úteis

- [Documentação Completa](./installation.md)
- [Guia de Instalação](./installation.md)
- [Guia de Uso](./usage.md)
- [Troubleshooting](./troubleshooting.md)
- [GitHub Repository](https://github.com/Ronbragaglia/identificador_bandeira_cartao)
- [Reportar Bug](https://github.com/Ronbragaglia/identificador_bandeira_cartao/issues)
- [Solicitar Feature](https://github.com/Ronbragaglia/identificador_bandeira_cartao/issues)
