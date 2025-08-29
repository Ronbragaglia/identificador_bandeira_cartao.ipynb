Objetivo:
Identificar a bandeira do cartão (Visa, MasterCard, Amex, Diners, Discover, JCB, Elo, Hipercard) usando faixas IIN/BIN e expressões regulares, e verificar a validade do número com Luhn para reduzir falsos positivos.

Por que este projeto?
Reúne em um só lugar padrões de bandeiras globais e brasileiras (Elo/Hipercard), úteis para protótipos, validações de formulários e estudos.

Demonstra boas práticas: funções puras, testes, README e automação de CI com GitHub Actions.

Principais recursos
Detecção de bandeiras: Visa, MasterCard, American Express, Diners, Discover, JCB, Elo e Hipercard.

Validação por Luhn com implementação clara e performática.

Pronto para Colab e também para uso como módulo Python (src/validator.py).

Demo rápida (Colab)
Abra o notebook do Colab, cole o código fornecido e execute a célula para ver os testes de exemplo e usar a função identify_brand.

Exemplo de uso no Colab:

info = identify_brand("4111 1111 1111 1111")
print(info)
# CardInfo(brand='visa', valid_luhn=True, normalized='4111111111111111', length=16)

Uso como biblioteca
Importar e chamar a função para obter a bandeira e o status de Luhn.

from src.validator import identify_brand

print(identify_brand("5555 5555 5555 4444"))
# CardInfo(brand='mastercard', valid_luhn=True, normalized='5555555555554444', length=16)
****

Exemplos práticos
Visa: 4111111111111111 → bandeira visa e Luhn válido.

MasterCard: 5555555555554444 → bandeira mastercard e Luhn válido.

Amex: 378282246310005 → bandeira amex e Luhn válido.

Hipercard: 6062825624254001 → bandeira hipercard e Luhn válido.

Elo: 4011780000000002 → bandeira elo e Luhn válido.

.
├── src/
│   └── validator.py         # Luhn + regex + identify_brand
├── tests/
│   └── test_validator.py    # Testes unitários (unittest)
├── notebook/
│   └── identificador_bandeira_cartao.ipynb  # Opcional: versão Colab
├── images/                  # Screenshots do notebook (opcional)
├── .github/workflows/
│   └── python-ci.yml        # CI básico com GitHub Actions
├── .gitignore
└── README.md


Decisões técnicas
Luhn: algoritmo padrão para verificação do dígito, implementado com soma alternada após inversão da string numérica.

Regex/IIN: padrões consolidados para Visa/MC/Amex/Diners/Discover/JCB e conjuntos práticos para Elo/Hipercard; essas faixas podem evoluir, então mantenha atualizações.

Separação de responsabilidades: identificação de bandeira independe da validação Luhn, permitindo mensagens precisas.

Contribuição
Fork, branch, commit e PR são bem-vindos; manter testes verdes e descrição clara das mudanças no PR.


Licença
Este projeto está sob a licença MIT; ver LICENSE no repositório.

Observações importantes
Números de cartões reais não devem ser utilizados; use apenas dados de teste públicos.

Padrões de Elo/Hipercard podem mudar com o tempo; revise regex periodicamente para manter a precisão.
