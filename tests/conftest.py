"""
Configurações e fixtures para testes.
"""

import pytest

from card_brand_identifier.validator import (
    TEST_NUMBERS,
    BRAND_PATTERNS,
    SUPPORTED_BRANDS_ORDER,
)


@pytest.fixture
def sample_visa_numbers():
    """Retorna números de teste Visa."""
    return TEST_NUMBERS["visa"]


@pytest.fixture
def sample_mastercard_numbers():
    """Retorna números de teste MasterCard."""
    return TEST_NUMBERS["mastercard"]


@pytest.fixture
def sample_amex_numbers():
    """Retorna números de teste American Express."""
    return TEST_NUMBERS["amex"]


@pytest.fixture
def sample_diners_numbers():
    """Retorna números de teste Diners Club."""
    return TEST_NUMBERS["diners"]


@pytest.fixture
def sample_discover_numbers():
    """Retorna números de teste Discover."""
    return TEST_NUMBERS["discover"]


@pytest.fixture
def sample_jcb_numbers():
    """Retorna números de teste JCB."""
    return TEST_NUMBERS["jcb"]


@pytest.fixture
def sample_hipercard_numbers():
    """Retorna números de teste Hipercard."""
    return TEST_NUMBERS["hipercard"]


@pytest.fixture
def sample_elo_numbers():
    """Retorna números de teste Elo."""
    return TEST_NUMBERS["elo"]


@pytest.fixture
def all_test_numbers():
    """Retorna todos os números de teste."""
    return [num for numbers in TEST_NUMBERS.values() for num in numbers]


@pytest.fixture
def valid_card_numbers():
    """Retorna números de cartão válidos (passam em Luhn)."""
    return [
        "4111111111111111",  # Visa
        "4012888888881881",  # Visa
        "5555555555554444",  # MasterCard
        "5105105105105100",  # MasterCard
        "378282246310005",  # Amex
        "371449635398431",  # Amex
        "30569309025904",  # Diners
        "38520000023237",  # Diners
        "6011111111111117",  # Discover
        "6011000990139424",  # Discover
        "3530111333300000",  # JCB
        "3566002020360505",  # JCB
        "6062825624254001",  # Hipercard
        "3841000000000010",  # Hipercard
    ]


@pytest.fixture
def invalid_card_numbers():
    """Retorna números de cartão inválidos (não passam em Luhn)."""
    return [
        "4111111111111112",  # Visa inválido
        "5555555555554445",  # MasterCard inválido
        "378282246310006",  # Amex inválido
        "30569309025905",  # Diners inválido
        "6011111111111118",  # Discover inválido
    ]


@pytest.fixture
def formatted_card_numbers():
    """Retorna números de cartão com formatação."""
    return [
        "4111 1111 1111 1111",  # Visa com espaços
        "5555-5555-5555-4444",  # MasterCard com hífens
        "3782 822463 10005",  # Amex com espaços
        "3056-9309-0259-04",  # Diners com hífens
    ]


@pytest.fixture
def empty_inputs():
    """Retorna entradas vazias."""
    return [
        "",
        "   ",
        "-",
        "----",
    ]


@pytest.fixture
def invalid_inputs():
    """Retorna entradas inválidas."""
    return [
        "abcd1234",
        "test",
        "123",
        "12345678901234567890",  # Muito longo
        "abc-def-ghi-jkl",
    ]


@pytest.fixture
def brand_patterns():
    """Retorna os padrões de regex para cada bandeira."""
    return BRAND_PATTERNS


@pytest.fixture
def supported_brands():
    """Retorna a lista de bandeiras suportadas."""
    return SUPPORTED_BRANDS_ORDER
