"""
Exemplos avançados de uso do Card Brand Identifier.

Este arquivo demonstra casos de uso mais avançados da biblioteca.
"""

from typing import List, Dict, Tuple
from card_brand_identifier import (
    identify_brand,
    luhn_check,
    get_test_numbers,
    SUPPORTED_BRANDS_ORDER,
    BRAND_PATTERNS,
)


def example_1_batch_processing():
    """Exemplo 1: Processamento em lote de cartões."""
    print("=" * 60)
    print("Exemplo 1: Processamento em Lote")
    print("=" * 60)

    # Lista de cartões para processar
    card_list = [
        "4111111111111111",
        "5555555555554444",
        "378282246310005",
        "30569309025904",
        "6011111111111117",
        "3530111333300000",
        "6062825624254001",
        "4011780000000002",
    ]

    # Processar todos os cartões
    results = []
    for card in card_list:
        info = identify_brand(card)
        results.append({
            "number": card,
            "brand": info.brand,
            "valid": info.valid_luhn,
            "length": info.length,
        })

    # Exibir resultados em formato de tabela
    print("\nResultados do processamento em lote:\n")
    print(f"{'Número':<20} {'Bandeira':<15} {'Válido':<8} {'Dígitos':<8}")
    print("-" * 60)
    for result in results:
        valid_str = "✓" if result["valid"] else "✗"
        print(f"{result['number']:<20} {result['brand'] or 'N/A':<15} {valid_str:<8} {result['length']:<8}")
    print()


def example_2_statistics():
    """Exemplo 2: Estatísticas de cartões."""
    print("=" * 60)
    print("Exemplo 2: Estatísticas de Cartões")
    print("=" * 60)

    # Obter todos os números de teste
    all_numbers = get_test_numbers()

    # Calcular estatísticas
    brand_counts = {}
    valid_counts = {}
    total_valid = 0
    total_invalid = 0

    for number in all_numbers:
        info = identify_brand(number)

        # Contar por bandeira
        if info.brand:
            brand_counts[info.brand] = brand_counts.get(info.brand, 0) + 1

        # Contar válidos/inválidos
        if info.valid_luhn:
            total_valid += 1
            if info.brand:
                valid_counts[info.brand] = valid_counts.get(info.brand, 0) + 1
        else:
            total_invalid += 1

    # Exibir estatísticas
    print(f"\nTotal de cartões: {len(all_numbers)}")
    print(f"Válidos: {total_valid}")
    print(f"Inválidos: {total_invalid}")
    print(f"\nDistribuição por bandeira:\n")

    for brand in SUPPORTED_BRANDS_ORDER:
        if brand in brand_counts:
            count = brand_counts[brand]
            valid = valid_counts.get(brand, 0)
            percentage = (count / len(all_numbers)) * 100
            print(f"  {brand.capitalize():<15} {count:>3} ({percentage:>5.1f}%) - Válidos: {valid}")
    print()


def example_3_filter_by_brand():
    """Exemplo 3: Filtrar cartões por bandeira."""
    print("=" * 60)
    print("Exemplo 3: Filtrar por Bandeira")
    print("=" * 60)

    # Lista de cartões mistos
    mixed_cards = [
        "4111111111111111",  # Visa
        "5555555555554444",  # MasterCard
        "4012888888881881",  # Visa
        "5105105105105100",  # MasterCard
        "378282246310005",  # Amex
        "4222222222222",  # Visa
    ]

    # Filtrar apenas cartões Visa
    visa_cards = [card for card in mixed_cards if identify_brand(card).brand == "visa"]

    print("\nCartões originais:")
    for card in mixed_cards:
        info = identify_brand(card)
        print(f"  {card} -> {info.brand}")

    print(f"\nCartões Visa filtrados: {len(visa_cards)}")
    for card in visa_cards:
        print(f"  {card}")
    print()


def example_4_validate_and_format():
    """Exemplo 4: Validar e formatar números."""
    print("=" * 60)
    print("Exemplo 4: Validar e Formatar")
    print("=" * 60)

    # Função para formatar número de cartão
    def format_card_number(number: str, brand: str) -> str:
        """Formata o número de cartão com espaços."""
        if brand == "amex":
            # Amex: 4-6-5
            if len(number) == 15:
                return f"{number[:4]} {number[4:10]} {number[10:]}"
        else:
            # Outras: 4-4-4-4
            if len(number) == 16:
                return f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:]}"
        return number

    # Testar formatação
    test_cases = [
        "4111111111111111",
        "5555555555554444",
        "378282246310005",
    ]

    print("\nFormatação de números:\n")
    for card in test_cases:
        info = identify_brand(card)
        formatted = format_card_number(info.normalized, info.brand)
        print(f"  Original:    {card}")
        print(f"  Normalizado: {info.normalized}")
        print(f"  Formatado:   {formatted}")
        print(f"  Bandeira:    {info.brand}")
        print(f"  Válido:      {info.valid_luhn}")
        print()


def example_5_custom_validation():
    """Exemplo 5: Validação personalizada."""
    print("=" * 60)
    print("Exemplo 5: Validação Personalizada")
    print("=" * 60)

    # Função de validação personalizada
    def validate_card(number: str) -> Dict[str, any]:
        """
        Valida um cartão com critérios personalizados.

        Returns:
            Dicionário com informações de validação
        """
        info = identify_brand(number)

        # Critérios de validação
        is_valid = True
        errors = []

        # Verificar se tem número
        if not info.normalized:
            is_valid = False
            errors.append("Número vazio")

        # Verificar comprimento
        if info.length < 13 or info.length > 19:
            is_valid = False
            errors.append(f"Comprimento inválido: {info.length}")

        # Verificar Luhn
        if not info.valid_luhn:
            is_valid = False
            errors.append("Falha na validação Luhn")

        # Verificar bandeira
        if not info.brand:
            is_valid = False
            errors.append("Bandeira não identificada")

        return {
            "number": number,
            "normalized": info.normalized,
            "brand": info.brand,
            "is_valid": is_valid,
            "errors": errors,
        }

    # Testar validação personalizada
    test_cards = [
        "4111111111111111",  # Válido
        "4111111111111112",  # Inválido (Luhn)
        "123",  # Inválido (curto)
        "",  # Inválido (vazio)
    ]

    print("\nResultados da validação personalizada:\n")
    for card in test_cards:
        result = validate_card(card)
        print(f"Número: {card if card else '(vazio)'}")
        print(f"  Normalizado: {result['normalized'] or '(vazio)'}")
        print(f"  Bandeira: {result['brand'] or 'N/A'}")
        print(f"  Válido: {'✓' if result['is_valid'] else '✗'}")
        if result['errors']:
            print(f"  Erros:")
            for error in result['errors']:
                print(f"    - {error}")
        print()


def example_6_brand_detection_performance():
    """Exemplo 6: Performance de detecção de bandeira."""
    print("=" * 60)
    print("Exemplo 6: Performance de Detecção")
    print("=" * 60)

    import time

    # Gerar muitos números de teste
    test_numbers = get_test_numbers() * 100  # Repetir 100 vezes

    # Medir tempo de processamento
    start_time = time.time()

    results = []
    for number in test_numbers:
        info = identify_brand(number)
        results.append(info)

    end_time = time.time()

    # Calcular estatísticas
    total_time = end_time - start_time
    cards_per_second = len(test_numbers) / total_time
    avg_time_per_card = total_time / len(test_numbers)

    print(f"\nPerformance de detecção:")
    print(f"  Total de cartões: {len(test_numbers)}")
    print(f"  Tempo total: {total_time:.4f} segundos")
    print(f"  Cartões por segundo: {cards_per_second:.2f}")
    print(f"  Tempo médio por cartão: {avg_time_per_card * 1000:.4f} ms")
    print()


def main():
    """Executa todos os exemplos avançados."""
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 15 + "Card Brand Identifier" + " " * 21 + "║")
    print("║" + " " * 10 + "Exemplos de Uso Avançado" + " " * 24 + "║")
    print("╚" + "═" * 58 + "╝")
    print("\n")

    examples = [
        example_1_batch_processing,
        example_2_statistics,
        example_3_filter_by_brand,
        example_4_validate_and_format,
        example_5_custom_validation,
        example_6_brand_detection_performance,
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
    print("Exemplos avançados concluídos!")
    print("=" * 60)


if __name__ == "__main__":
    main()
