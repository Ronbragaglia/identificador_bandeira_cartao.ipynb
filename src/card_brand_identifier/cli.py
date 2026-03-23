"""
CLI para identificação de bandeiras de cartão de crédito.

Este módulo fornece uma interface de linha de comando para
identificar bandeiras e validar números de cartão.
"""

import argparse
import sys
from typing import Optional

from .validator import identify_brand, describe_result, get_test_numbers, SUPPORTED_BRANDS_ORDER


def print_banner() -> None:
    """Imprime o banner da aplicação."""
    banner = """
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║          🏦 Card Brand Identifier v1.0.0 🏦                  ║
║      Identificador de Bandeira de Cartão de Crédito           ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
"""
    print(banner)


def print_supported_brands() -> None:
    """Imprime a lista de bandeiras suportadas."""
    print("\n📋 Bandeiras Suportadas:")
    print("─" * 50)
    for i, brand in enumerate(SUPPORTED_BRANDS_ORDER, 1):
        icon = get_brand_icon(brand)
        print(f"  {i:2d}. {icon} {brand.capitalize()}")
    print("─" * 50)


def get_brand_icon(brand: Optional[str]) -> str:
    """Retorna um ícone emoji para a bandeira."""
    icons = {
        "visa": "💳",
        "mastercard": "💳",
        "amex": "💳",
        "diners": "💳",
        "discover": "💳",
        "jcb": "💳",
        "hipercard": "💳",
        "elo": "💳",
    }
    return icons.get(brand, "❓")


def identify_card(number: str, verbose: bool = False) -> None:
    """
    Identifica e imprime informações sobre um cartão.

    Args:
        number: Número do cartão
        verbose: Se True, imprime informações detalhadas
    """
    info = identify_brand(number, validate_luhn=True)

    if verbose:
        print("\n📊 Informações Detalhadas:")
        print("─" * 50)
        print(f"  Número original: {number}")
        print(f"  Número normalizado: {info.normalized}")
        print(f"  Quantidade de dígitos: {info.length}")
        print(f"  Bandeira: {info.brand if info.brand else 'Indeterminada'}")
        print(f"  Validação Luhn: {'✅ Válido' if info.valid_luhn else '❌ Inválido'}")
        print("─" * 50)
    else:
        icon = get_brand_icon(info.brand)
        luhn_icon = "✅" if info.valid_luhn else "❌"
        print(f"\n{icon} {describe_result(info)}")


def run_tests() -> None:
    """Executa testes com números de exemplo."""
    print("\n🧪 Executando Testes:")
    print("─" * 50)

    test_count = 0
    passed = 0

    for brand in SUPPORTED_BRANDS_ORDER:
        numbers = get_test_numbers(brand)
        if numbers:
            print(f"\n{brand.capitalize()}:")
            for num in numbers:
                info = identify_brand(num, validate_luhn=True)
                test_count += 1
                if info.brand == brand and info.valid_luhn:
                    passed += 1
                    print(f"  ✅ {num} - {info.brand}")
                else:
                    print(f"  ❌ {num} - Esperado: {brand}, Obtido: {info.brand}")

    print("\n" + "─" * 50)
    print(f"📊 Resultado: {passed}/{test_count} testes passaram")
    print("─" * 50)


def interactive_mode() -> None:
    """Modo interativo para identificar múltiplos cartões."""
    print("\n🎮 Modo Interativo")
    print("─" * 50)
    print("Digite um número de cartão para identificar")
    print("Digite 'sair' ou 'exit' para encerrar")
    print("Digite 'testes' para executar testes")
    print("Digite 'help' para ver a ajuda")
    print("─" * 50)

    while True:
        try:
            number = input("\n💳 Número do cartão: ").strip()

            if not number:
                continue

            if number.lower() in ["sair", "exit", "quit"]:
                print("\n👋 Até logo!")
                break

            if number.lower() == "testes":
                run_tests()
                continue

            if number.lower() == "help":
                print_supported_brands()
                continue

            identify_card(number, verbose=True)

        except KeyboardInterrupt:
            print("\n\n👋 Encerrando...")
            break
        except Exception as e:
            print(f"\n❌ Erro: {e}")


def main() -> int:
    """
    Função principal da CLI.

    Returns:
        0 em caso de sucesso, 1 em caso de erro
    """
    parser = argparse.ArgumentParser(
        description="Identificador de Bandeira de Cartão de Crédito",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  %(prog)s 4111111111111111
  %(prog)s "5555 5555 5555 4444"
  %(prog)s 378282246310005 --verbose
  %(prog)s --test
  %(prog)s --interactive
  %(prog)s --brands
        """,
    )

    parser.add_argument(
        "number",
        nargs="?",
        help="Número do cartão para identificar",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Mostrar informações detalhadas",
    )

    parser.add_argument(
        "-t",
        "--test",
        action="store_true",
        help="Executar testes com números de exemplo",
    )

    parser.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        help="Modo interativo",
    )

    parser.add_argument(
        "-b",
        "--brands",
        action="store_true",
        help="Listar bandeiras suportadas",
    )

    parser.add_argument(
        "--no-banner",
        action="store_true",
        help="Não mostrar o banner",
    )

    args = parser.parse_args()

    # Mostra o banner a menos que seja desativado
    if not args.no_banner:
        print_banner()

    # Lista bandeiras
    if args.brands:
        print_supported_brands()
        return 0

    # Modo interativo
    if args.interactive:
        interactive_mode()
        return 0

    # Executa testes
    if args.test:
        run_tests()
        return 0

    # Identifica um cartão
    if args.number:
        identify_card(args.number, verbose=args.verbose)
        return 0

    # Se nenhum argumento foi fornecido, mostra ajuda
    if not args.number and not args.test and not args.interactive and not args.brands:
        parser.print_help()
        print_supported_brands()
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
