"""
Exemplos básicos de uso do Card Brand Identifier.

Este arquivo demonstra como usar a biblioteca para identificar
bandeiras de cartão de crédito e validar números.
"""

from card_brand_identifier import (
    identify_brand,
    luhn_check,
    describe_result,
    CardInfo,
    get_test_numbers,
    SUPPORTED_BRANDS_ORDER,
)


def example_1_basic_identification():
    """Exemplo 1: Identificação básica de cartão."""
    print("=" * 60)
    print("Exemplo 1: Identificação Básica")
    print("=" * 60)

    # Número de cartão Visa
    card_number = "4111 1111 1111 1111"
    info = identify_brand(card_number)

    print(f"\nNúmero: {card_number}")
    print(f"Bandeira: {info.brand}")
    print(f"Válido (Luhn): {info.valid_luhn}")
    print(f"Normalizado: {info.normalized}")
    print(f"Dígitos: {info.length}")
    print()


def example_2_multiple_cards():
    """Exemplo 2: Identificação de múltiplos cartões."""
    print("=" * 60)
    print("Exemplo 2: Identificação de Múltiplos Cartões")
    print("=" * 60)

    cards = [
        "4111111111111111",  # Visa
        "5555555555554444",  # MasterCard
        "378282246310005",  # Amex
        "30569309025904",  # Diners
        "6011111111111117",  # Discover
        "3530111333300000",  # JCB
        "6062825624254001",  # Hipercard
        "4011780000000002",  # Elo
    ]

    print("\nIdentificando cartões:\n")
    for card in cards:
        info = identify_brand(card)
        print(f"  {card} -> {describe_result(info)}")
    print()


def example_3_formatted_numbers():
    """Exemplo 3: Números com formatação."""
    print("=" * 60)
    print("Exemplo 3: Números com Formatação")
    print("=" * 60)

    # Números com espaços e hífens
    formatted_cards = [
        "4111 1111 1111 1111",  # Visa com espaços
        "5555-5555-5555-4444",  # MasterCard com hífens
        "3782 822463 10005",  # Amex com espaços
    ]

    print("\nProcessando números formatados:\n")
    for card in formatted_cards:
        info = identify_brand(card)
        print(f"  Original: {card}")
        print(f"  Normalizado: {info.normalized}")
        print(f"  Bandeira: {info.brand}")
        print(f"  Válido: {info.valid_luhn}")
        print()


def example_4_luhn_validation():
    """Exemplo 4: Validação Luhn."""
    print("=" * 60)
    print("Exemplo 4: Validação Luhn")
    print("=" * 60)

    # Números válidos e inválidos
    test_cases = [
        ("4111111111111111", True, "Visa válido"),
        ("4111111111111112", False, "Visa inválido"),
        ("5555555555554444", True, "MasterCard válido"),
        ("5555555555554445", False, "MasterCard inválido"),
    ]

    print("\nTestando validação Luhn:\n")
    for number, expected, description in test_cases:
        result = luhn_check(number)
        status = "✓" if result == expected else "✗"
        print(f"  {status} {description}: {number}")
        print(f"     Resultado: {result}, Esperado: {expected}")
    print()


def example_5_card_info_object():
    """Exemplo 5: Usando o objeto CardInfo."""
    print("=" * 60)
    print("Exemplo 5: Objeto CardInfo")
    print("=" * 60)

    # Criando um objeto CardInfo manualmente
    info = CardInfo(
        brand="visa",
        valid_luhn=True,
        normalized="4111111111111111",
        length=16
    )

    print(f"\nObjeto CardInfo:")
    print(f"  brand: {info.brand}")
    print(f"  valid_luhn: {info.valid_luhn}")
    print(f"  normalized: {info.normalized}")
    print(f"  length: {info.length}")
    print(f"\nString representation: {str(info)}")
    print(f"Repr: {repr(info)}")
    print()


def example_6_test_numbers():
    """Exemplo 6: Usando números de teste."""
    print("=" * 60)
    print("Exemplo 6: Números de Teste")
    print("=" * 60)

    # Obter todos os números de teste
    all_numbers = get_test_numbers()

    print(f"\nTotal de números de teste: {len(all_numbers)}\n")

    # Contar por bandeira
    for brand in SUPPORTED_BRANDS_ORDER:
        brand_numbers = get_test_numbers(brand)
        if brand_numbers:
            print(f"{brand.capitalize()}: {len(brand_numbers)} números")
    print()

    # Testar alguns números
    print("\nTestando números de exemplo:\n")
    for brand in SUPPORTED_BRANDS_ORDER[:4]:  # Primeiras 4 bandeiras
        numbers = get_test_numbers(brand)
        if numbers:
            info = identify_brand(numbers[0])
            print(f"  {brand.capitalize()}: {numbers[0]} -> {info.brand}")
    print()


def example_7_error_handling():
    """Exemplo 7: Tratamento de erros."""
    print("=" * 60)
    print("Exemplo 7: Tratamento de Erros")
    print("=" * 60)

    # Entradas inválidas
    invalid_inputs = [
        "",
        "   ",
        "abcd",
        "123",
        "test",
    ]

    print("\nProcessando entradas inválidas:\n")
    for input_val in invalid_inputs:
        info = identify_brand(input_val)
        print(f"  Entrada: '{input_val}'")
        print(f"  Bandeira: {info.brand}")
        print(f"  Válido: {info.valid_luhn}")
        print(f"  Normalizado: '{info.normalized}'")
        print(f"  Dígitos: {info.length}")
    print()


def example_8_without_luhn():
    """Exemplo 8: Identificação sem validação Luhn."""
    print("=" * 60)
    print("Exemplo 8: Identificação sem Validação Luhn")
    print("=" * 60)

    # Identificar sem validar Luhn
    card_number = "4111111111111112"  # Visa inválido
    info_with_luhn = identify_brand(card_number, validate_luhn=True)
    info_without_luhn = identify_brand(card_number, validate_luhn=False)

    print(f"\nNúmero: {card_number}")
    print(f"\nCom validação Luhn:")
    print(f"  Bandeira: {info_with_luhn.brand}")
    print(f"  Válido (Luhn): {info_with_luhn.valid_luhn}")

    print(f"\nSem validação Luhn:")
    print(f"  Bandeira: {info_without_luhn.brand}")
    print(f"  Válido (Luhn): {info_without_luhn.valid_luhn}")
    print()


def main():
    """Executa todos os exemplos."""
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 15 + "Card Brand Identifier" + " " * 21 + "║")
    print("║" + " " * 10 + "Exemplos de Uso Básico" + " " * 26 + "║")
    print("╚" + "═" * 58 + "╝")
    print("\n")

    examples = [
        example_1_basic_identification,
        example_2_multiple_cards,
        example_3_formatted_numbers,
        example_4_luhn_validation,
        example_5_card_info_object,
        example_6_test_numbers,
        example_7_error_handling,
        example_8_without_luhn,
    ]

    for i, example in enumerate(examples, 1):
        try:
            example()
            input("\nPressione Enter para continuar para o próximo exemplo...")
            print("\n" * 2)
        except KeyboardInterrupt:
            print("\n\nExemplos interrompidos pelo usuário.")
            break
        except Exception as e:
            print(f"\nErro ao executar exemplo {i}: {e}")
            continue

    print("\n" + "=" * 60)
    print("Exemplos concluídos!")
    print("=" * 60)


if __name__ == "__main__":
    main()
