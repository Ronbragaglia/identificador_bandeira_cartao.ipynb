"""
Módulo de validação e identificação de bandeiras de cartão de crédito.

Este módulo fornece funções para:
- Validar números de cartão usando o algoritmo de Luhn
- Identificar a bandeira do cartão baseado em padrões IIN/BIN
- Retornar informações detalhadas sobre o cartão
"""

import re
from dataclasses import dataclass
from typing import Optional, Dict, List


def luhn_check(number: str) -> bool:
    """
    Valida um número de cartão usando o algoritmo de Luhn.

    Args:
        number: Número do cartão (pode conter espaços ou hífens)

    Returns:
        True se o número for válido, False caso contrário

    Example:
        >>> luhn_check("4111111111111111")
        True
        >>> luhn_check("4111111111111112")
        False
    """
    # Remove caracteres não numéricos
    num = re.sub(r"\D", "", number)
    if not num:
        return False

    # Inverte a string e converte para lista de inteiros
    digits = list(map(int, num[::-1]))

    # Aplica o algoritmo de Luhn
    total = 0
    for i, d in enumerate(digits):
        if i % 2 == 1:
            # Dobra os dígitos em posições ímpares (após inversão)
            dbl = d * 2
            # Se o resultado for maior que 9, subtrai 9
            total += dbl - 9 if dbl > 9 else dbl
        else:
            total += d

    # O número é válido se a soma for múltipla de 10
    return total % 10 == 0


# Padrões de regex para cada bandeira (baseados em IIN/BIN ranges)
BRAND_PATTERNS: Dict[str, re.Pattern] = {
    "visa": re.compile(r"^4\d{12}(\d{3})?(\d{3})?$"),
    "mastercard": re.compile(
        r"^(?:5[1-5]\d{14}|2(?:22[1-9]\d{12}|2[3-9]\d{13}|[3-6]\d{14}|7[11]\d{13}|720\d{12}))$"
    ),
    "amex": re.compile(r"^3\d{13}$"),
    "diners": re.compile(r"^3(?:0[0-5]|\d)\d{11}$"),
    "discover": re.compile(r"^(?:6011\d{12}|65\d{14}|64[4-9]\d{13})$"),
    "jcb": re.compile(r"^(?:2131|1800)\d{11}$|^(?:35\d{3})\d{11}$"),
    "hipercard": re.compile(r"^(?:606282\d{10}(\d{3})?|3841(?:0|4|6)0\d{13})$"),
    "elo": re.compile(
        r"^(?:4011(78|79)|431274|438935|451416|457393|4576(?:3[12]|\d)|504175|627780|636297|636368|636369|"
        r"6503[1-3]|6500(?:3[5-9]|4\d|5[0-1])|6504(?:0[5-9]|[1-3]\d)|650(?:48[5-9]|49\d|50\d|51[1-9]|52\d|53[0-7])|"
        r"6505(?:[4-9]\d)|6507(?:0\d|1[0-8]|2[0-7])|650(?:90[1-9]|91\d|920)|6516(?:5[2-9]|[6-7]\d)|6550(?:0\d|1[1-9]|2[1-9]|[3-4]\d|5[0-8]))\d+$"
    ),
}

# Ordem de verificação das bandeiras (importante para evitar falsos positivos)
SUPPORTED_BRANDS_ORDER: List[str] = [
    "visa",
    "mastercard",
    "amex",
    "diners",
    "discover",
    "jcb",
    "hipercard",
    "elo",
]


@dataclass
class CardInfo:
    """
    Informações sobre um cartão de crédito.

    Attributes:
        brand: Nome da bandeira identificada (None se não identificada)
        valid_luhn: True se o número passar na validação de Luhn
        normalized: Número normalizado (apenas dígitos)
        length: Quantidade de dígitos no número
    """

    brand: Optional[str]
    valid_luhn: bool
    normalized: str
    length: int

    def __str__(self) -> str:
        """Representação em string das informações do cartão."""
        return describe_result(self)

    def __repr__(self) -> str:
        """Representação em string para debugging."""
        return f"CardInfo(brand={self.brand!r}, valid_luhn={self.valid_luhn}, normalized={self.normalized!r}, length={self.length})"


def identify_brand(number: str, validate_luhn: bool = True) -> CardInfo:
    """
    Identifica a bandeira de um cartão de crédito.

    Args:
        number: Número do cartão (pode conter espaços ou hífens)
        validate_luhn: Se True, valida o número usando Luhn

    Returns:
        Objeto CardInfo com informações sobre o cartão

    Example:
        >>> info = identify_brand("4111 1111 1111 1111")
        >>> info.brand
        'visa'
        >>> info.valid_luhn
        True
    """
    # Normaliza o número (remove caracteres não numéricos)
    num = re.sub(r"\D", "", number or "")

    # Tenta identificar a bandeira
    brand = None
    for b in SUPPORTED_BRANDS_ORDER:
        if BRAND_PATTERNS[b].match(num):
            brand = b
            break

    # Valida usando Luhn se solicitado
    valid = luhn_check(num) if validate_luhn and num else False

    return CardInfo(brand=brand, valid_luhn=valid, normalized=num, length=len(num))


def describe_result(info: CardInfo) -> str:
    """
    Gera uma descrição legível das informações do cartão.

    Args:
        info: Objeto CardInfo com informações do cartão

    Returns:
        String com descrição formatada

    Example:
        >>> info = identify_brand("4111 1111 1111 1111")
        >>> describe_result(info)
        'Bandeira: visa | Luhn: válido | Dígitos: 16 | Número: 4111111111111111'
    """
    if not info.normalized:
        return "Entrada vazia/sem dígitos."

    if info.brand and info.valid_luhn:
        return f"Bandeira: {info.brand} | Luhn: válido | Dígitos: {info.length} | Número: {info.normalized}"
    if info.brand and not info.valid_luhn:
        return f"Bandeira: {info.brand} | Luhn: inválido | Dígitos: {info.length} | Número: {info.normalized}"
    if not info.brand and info.valid_luhn:
        return f"Bandeira: indeterminada | Luhn: válido | Dígitos: {info.length} | Número: {info.normalized}"
    return f"Bandeira: indeterminada | Luhn: inválido | Dígitos: {info.length} | Número: {info.normalized}"


def identify_and_print(number: str) -> None:
    """
    Identifica e imprime informações sobre um cartão.

    Args:
        number: Número do cartão (pode conter espaços ou hífens)
    """
    info = identify_brand(number, validate_luhn=True)
    print(describe_result(info))


# Números de teste para cada bandeira
TEST_NUMBERS: Dict[str, List[str]] = {
    "visa": [
        "4111111111111111",
        "4012888888881881",
        "4222222222222",
    ],
    "mastercard": [
        "5555555555554444",
        "5105105105105100",
        "2223000048400011",
    ],
    "amex": [
        "378282246310005",
        "371449635398431",
        "378734493671000",
    ],
    "diners": [
        "30569309025904",
        "38520000023237",
    ],
    "discover": [
        "6011111111111117",
        "6011000990139424",
        "6511111111111112",
    ],
    "jcb": [
        "3530111333300000",
        "3566002020360505",
        "213111111111111",
    ],
    "hipercard": [
        "6062825624254001",
        "3841000000000010",
    ],
    "elo": [
        "4011780000000002",
        "4389350000000000",
        "5066991111111118",
    ],
}


def get_test_numbers(brand: Optional[str] = None) -> List[str]:
    """
    Retorna números de teste para validação.

    Args:
        brand: Nome da bandeira específica (None para todas)

    Returns:
        Lista de números de teste
    """
    if brand:
        return TEST_NUMBERS.get(brand.lower(), [])
    return [num for numbers in TEST_NUMBERS.values() for num in numbers]


def run_quick_tests() -> None:
    """Executa testes rápidos com números de exemplo."""
    print("== Testes rápidos ==")
    for num in get_test_numbers():
        identify_and_print(num)
