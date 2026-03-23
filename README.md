# 🏦 Card Brand Identifier

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Type checking: mypy](https://img.shields.io/badge/type%20checking-mypy-blue.svg)](https://github.com/python/mypy)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](tests/)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](tests/)

> Biblioteca Python profissional para identificação de bandeiras de cartão de crédito e validação usando o algoritmo de Luhn.

## ✨ Características

- 🎯 **Identificação Precisa**: Suporta 8 bandeiras principais (Visa, MasterCard, Amex, Diners, Discover, JCB, Hipercard, Elo)
- ✅ **Validação Luhn**: Algoritmo de validação padrão da indústria
- 🚀 **Fácil de Usar**: API simples e intuitiva
- 💻 **CLI Completa**: Interface de linha de comando poderosa
- 📦 **Zero Dependências**: Usa apenas bibliotecas padrão do Python
- 🧪 **Bem Testado**: Cobertura de testes abrangente
- 🐳 **Docker Ready**: Imagem Docker otimizada incluída
- 📚 **Documentação Completa**: Guias de instalação, uso e troubleshooting
- 🔧 **Ferramentas de Desenvolvimento**: Pre-commit hooks, CI/CD, Makefile

## 🚀 Instalação Rápida

### Via pip

```bash
pip install card-brand-identifier
```

### Do Código Fonte

```bash
git clone https://github.com/Ronbragaglia/identificador_bandeira_cartao.git
cd identificador_bandeira_cartao
pip install -e .
```

### Via Docker

```bash
docker build -t card-brand-identifier .
docker run --rm card-brand-identify 4111111111111111
```

## 📖 Uso Básico

### Python API

```python
from card_brand_identifier import identify_brand

# Identificar um cartão
info = identify_brand("4111 1111 1111 1111")

print(f"Bandeira: {info.brand}")        # visa
print(f"Válido: {info.valid_luhn}")      # True
print(f"Normalizado: {info.normalized}")  # 4111111111111111
```

### CLI

```bash
# Identificar um cartão
card-identify 4111111111111111

# Ver bandeiras suportadas
card-identify --brands

# Modo interativo
card-identify --interactive

# Executar testes
card-identify --test
```

## 💳 Bandeiras Suportadas

| Bandeira | Prefixos | Comprimento | Exemplo |
|----------|-----------|-------------|----------|
| 💳 Visa | 4 | 13, 16, 19 | `4111111111111111` |
| 💳 MasterCard | 51-55, 2221-2720 | 16 | `5555555555554444` |
| 💳 American Express | 34, 37 | 15 | `378282246310005` |
| 💳 Diners Club | 300-305, 36, 38 | 14 | `30569309025904` |
| 💳 Discover | 6011, 65, 644-649 | 16 | `6011111111111117` |
| 💳 JCB | 2131, 1800, 35 | 16 | `3530111333300000` |
| 💳 Hipercard | 3841, 606282 | 16 | `6062825624254001` |
| 💳 Elo | Múltiplos prefixos | 16 | `4011780000000002` |

## 🎯 Exemplos de Uso

### Validação de Formulário

```python
from card_brand_identifier import identify_brand

def validate_credit_card(number: str) -> dict:
    """Valida um cartão em um formulário web."""
    info = identify_brand(number)

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

### Processamento em Lote

```python
from card_brand_identifier import identify_brand

cards = [
    "4111111111111111",
    "5555555555554444",
    "378282246310005",
]

results = [identify_brand(card) for card in cards]

for info in results:
    print(f"{info.normalized}: {info.brand} ({'✓' if info.valid_luhn else '✗'})")
```

### Filtrar por Bandeira

```python
from card_brand_identifier import identify_brand

cards = [
    "4111111111111111",  # Visa
    "5555555555554444",  # MasterCard
    "4012888888881881",  # Visa
]

# Filtrar apenas Visa
visa_cards = [
    card for card in cards
    if identify_brand(card).brand == "visa"
]

print(visa_cards)
# ['4111111111111111', '4012888888881881']
```

## 🧪 Testes

```bash
# Executar todos os testes
pytest

# Executar com coverage
pytest --cov=src --cov-report=html

# Executar testes específicos
pytest tests/test_validator.py::TestLuhnCheck -v
```

## 🛠️ Desenvolvimento

### Configurar Ambiente

```bash
# Clone o repositório
git clone https://github.com/Ronbragaglia/identificador_bandeira_cartao.git
cd identificador_bandeira_cartao

# Crie um ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate  # Windows

# Instale as dependências
pip install -e ".[dev]"

# Instale os hooks do pre-commit
pre-commit install
```

### Comandos Disponíveis

```bash
# Ver ajuda do Makefile
make help

# Executar testes
make test

# Executar testes com coverage
make test-cov

# Formatar código
make format

# Verificar código
make check-all

# Construir pacote
make build

# Executar exemplos
make run-examples
```

## 📚 Documentação

- 📖 [Documentação Principal](docs/index.md)
- 🔧 [Guia de Instalação](docs/installation.md)
- 💡 [Guia de Uso](docs/usage.md)
- 🐛 [Troubleshooting](docs/troubleshooting.md)
- 📝 [Exemplos Básicos](examples/basic_usage.py)
- 🚀 [Exemplos Avançados](examples/advanced_usage.md)

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Fork o repositório
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

Para mais detalhes, veja [CONTRIBUTING.md](CONTRIBUTING.md).

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🔗 Links Úteis

- 📦 [PyPI Package](https://pypi.org/project/card-brand-identifier/)
- 🐛 [Reportar Bug](https://github.com/Ronbragaglia/identificador_bandeira_cartao/issues)
- 💡 [Solicitar Feature](https://github.com/Ronbragaglia/identificador_bandeira_cartao/issues)
- 📧 [Pull Requests](https://github.com/Ronbragaglia/identificador_bandeira_cartao/pulls)
- 📧 [Email](mailto:ronbragaglia@gmail.com)

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Ronbragaglia/identificador_bandeira_cartao&type=Date)](https://star-history.com/#Ronbragaglia/identificador_bandeira_cartao&Date)

## 🙏 Agradecimentos

- Agradecimentos a todos os contribuidores que ajudaram a melhorar este projeto
- Inspirado pelas melhores práticas da indústria de pagamentos
- Agradecimentos à comunidade Python pelos excelentes ferramentas de desenvolvimento

## 📞 Contato

- **Autor**: Rone Bragaglia
- **Email**: ronbragaglia@gmail.com
- **GitHub**: [@Ronbragaglia](https://github.com/Ronbragaglia)

---

⚠️ **Nota de Segurança**: Esta biblioteca deve ser usada apenas para fins educacionais e de desenvolvimento. Nunca use números de cartão reais em produção sem seguir as melhores práticas de segurança da PCI-DSS.

⚠️ **Nota Legal**: Os números de cartão fornecidos nos exemplos são números de teste públicos e não representam cartões reais. Use apenas números de teste fornecidos pelas operadoras de cartão.
