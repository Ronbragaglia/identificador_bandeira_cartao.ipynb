# Contribuindo para o Card Brand Identifier

Obrigado por considerar contribuir para o Card Brand Identifier! Este documento fornece diretrizes e instruções para contribuir com o projeto.

## 📋 Índice

- [Como Contribuir](#como-contribuir)
- [Processo de Desenvolvimento](#processo-de-desenvolvimento)
- [Diretrizes de Código](#diretrizes-de-código)
- [Processo de Pull Request](#processo-de-pull-request)
- [Reportando Bugs](#reportando-bugs)
- [Sugerindo Features](#sugerindo-features)

## 🚀 Como Contribuir

### Maneiras de Contribuir

Existem várias maneiras de contribuir:

1. **Reportar bugs** - Encontre e reporte bugs
2. **Sugerir novas features** - Ideias para melhorar o projeto
3. **Enviar Pull Requests** - Corrigir bugs ou adicionar features
4. **Melhorar a documentação** - Ajudar a tornar a documentação mais clara
5. **Escrever testes** - Melhorar a cobertura de testes
6. **Revisar Pull Requests** - Ajudar a revisar contribuições de outros

## 🔧 Processo de Desenvolvimento

### 1. Setup do Ambiente

```bash
# Fork o repositório
git clone https://github.com/SEU_USUARIO/identificador_bandeira_cartao.git
cd identificador_bandeira_cartao

# Adicione o repositório upstream
git remote add upstream https://github.com/Ronbragaglia/identificador_bandeira_cartao.git

# Crie um ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate  # Windows

# Instale as dependências
pip install -e ".[dev]"

# Instale os hooks do pre-commit
pre-commit install
```

### 2. Crie uma Branch

```bash
# Crie uma branch para sua feature
git checkout -b feature/sua-feature

# Ou para correção de bug
git checkout -b fix/seu-bug
```

### 3. Faça Suas Mudanças

```bash
# Faça suas mudanças
git add .
git commit -m "feat: adicione suporte para nova bandeira"
```

### 4. Teste Suas Mudanças

```bash
# Execute os testes
make test

# Execute os testes com coverage
make test-cov

# Verifique o código
make check-all
```

### 5. Push e Abra um PR

```bash
# Push para o seu fork
git push origin feature/sua-feature

# Abra um Pull Request no GitHub
```

## 📝 Diretrizes de Código

### Estilo de Código

Nós seguimos as seguintes convenções:

- **Formatação**: Use Black com line-length de 100
- **Imports**: Use isort com perfil black
- **Type Hints**: Use type hints em todas as funções públicas
- **Docstrings**: Use Google-style docstrings

### Exemplo de Código

```python
"""
Módulo de exemplo para contribuição.

Este módulo demonstra o estilo de código esperado.
"""

from typing import Optional


def example_function(param: str, optional_param: Optional[int] = None) -> bool:
    """
    Faz algo interessante.

    Args:
        param: Descrição do parâmetro.
        optional_param: Descrição do parâmetro opcional.

    Returns:
        True se sucesso, False caso contrário.

    Example:
        >>> example_function("test")
        True
    """
    if optional_param is None:
        optional_param = 0

    return len(param) > optional_param
```

### Testes

- Escreva testes para novas features
- Mantenha a cobertura de código acima de 90%
- Use fixtures para dados de teste
- Use descritivos nomes de teste

### Commits

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: adicione suporte para nova bandeira
fix: corrija validação Luhn para números longos
docs: atualize guia de instalação
test: adicione testes para nova feature
refactor: melhore performance de identificação
style: formate código com black
chore: atualize dependências
```

## 🔄 Processo de Pull Request

### Checklist Antes de Abrir um PR

- [ ] Código segue as diretrizes de estilo
- [ ] Testes foram adicionados/atualizados
- [ ] Todos os testes passam
- [ ] Coverage está acima de 90%
- [ ] Docstrings foram adicionadas
- [ ] CHANGELOG.md foi atualizado
- [ ] README.md foi atualizado (se necessário)
- [ ] Commits seguem Conventional Commits

### Título do PR

Use um título claro e descritivo:

```
feat: adicione suporte para bandeira Aura
fix: corrija detecção de MasterCard com prefixo 2221
docs: melhore documentação da CLI
```

### Descrição do PR

Inclua:

- Descrição clara das mudanças
- Motivação para a mudança
- Screenshots (se aplicável)
- Links para issues relacionadas
- Passos para testar

## 🐛 Reportando Bugs

### Antes de Reportar

1. **Pesquise issues existentes** - Verifique se o bug já foi reportado
2. **Verifique a documentação** - Certifique-se de que não é um erro de uso
3. **Teste com a versão mais recente** - O bug pode já ter sido corrigido

### Como Reportar

Crie uma issue com:

- **Título**: Descrição curta do bug
- **Descrição Detalhada**:
  - Passos para reproduzir
  - Comportamento esperado
  - Comportamento atual
  - Ambiente (Python, OS, versão do pacote)
- **Exemplo de Código**:
  ```python
  from card_brand_identifier import identify_brand
  info = identify_brand("4111111111111111")
  print(info.brand)  # Deveria ser 'visa'
  ```
- **Logs/Traceback**: Se houver erro, inclua o traceback completo

## 💡 Sugerindo Features

### Antes de Sugerir

1. **Pesquise issues existentes** - Verifique se a feature já foi sugerida
2. **Considere o escopo** - A feature se encaixa no projeto?
3. **Pense na implementação** - Como seria implementada?

### Como Sugerir

Crie uma issue com:

- **Título**: Descrição curta da feature
- **Descrição Detalhada**:
  - Motivação para a feature
  - Casos de uso
  - Benefícios esperados
  - Possíveis implementações
- **Exemplos de Uso**:
  ```python
  from card_brand_identifier import identify_brand
  info = identify_brand("4111111111111111")
  # Nova feature aqui
  ```

## 📚 Melhorando a Documentação

### Como Contribuir

1. **Correções**: Corrija erros de gramática, ortografia ou formatação
2. **Melhorias**: Adicione exemplos, esclareça conceitos
3. **Traduções**: Adicione traduções para outros idiomas

### Onde Contribuir

- README.md - Documentação principal
- docs/ - Documentação detalhada
- examples/ - Exemplos de código
- Docstrings - Documentação inline

## 🧪 Escrevendo Testes

### Boas Práticas

```python
import pytest
from card_brand_identifier import identify_brand

class TestNewFeature:
    """Testes para nova feature."""

    def test_basic_usage(self):
        """Testa uso básico da nova feature."""
        result = identify_brand("4111111111111111")
        assert result.brand == "visa"
        assert result.valid_luhn is True

    @pytest.mark.parametrize("card_number,expected_brand", [
        ("4111111111111111", "visa"),
        ("5555555555554444", "mastercard"),
    ])
    def test_multiple_cards(self, card_number, expected_brand):
        """Testa múltiplos números de cartão."""
        result = identify_brand(card_number)
        assert result.brand == expected_brand

    def test_error_handling(self):
        """Testa tratamento de erros."""
        with pytest.raises(ValueError):
            identify_brand(None)
```

## 🎨 Design e UX

### Para CLI

- Mantenha mensagens claras e concisas
- Use cores e ícones apropriadamente
- Forneça ajuda detalhada

### Para API

- Mantenha a API consistente
- Use type hints
- Forneça exemplos na docstring

## 📦 Publicando

### Quando Publicar

- Atualize a versão em pyproject.toml
- Atualize CHANGELOG.md
- Crie um git tag
- Push para o GitHub
- GitHub Actions irá publicar automaticamente

### Versionamento

Seguimos [Semantic Versioning](https://semver.org/):

- **MAJOR**: Mudanças incompatíveis com versões anteriores
- **MINOR**: Funcionalidades adicionadas de forma compatível
- **PATCH**: Correções de bugs compatíveis

## 🤝 Código de Conduta

Seja respeitoso e profissional. Nós valorizamos:

- Respeito mútuo
- Inclusão e diversidade
- Colaboração construtiva
- Foco no que é melhor para a comunidade

## 📞 Contato

Se você tiver dúvidas:

- Abra uma issue no GitHub
- Envie um email para ronbragaglia@gmail.com
- Entre em contato via GitHub [@Ronbragaglia](https://github.com/Ronbragaglia)

## 🙏 Agradecimentos

Agradecimentos a todos os contribuidores que ajudaram a tornar este projeto melhor!

---

**Lembre-se**: Qualquer contribuição é valiosa, não importa o tamanho. Obrigado por contribuir! 🎉
