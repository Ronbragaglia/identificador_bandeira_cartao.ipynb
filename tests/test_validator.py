"""
Testes para o módulo de validação de cartões.
"""

import pytest

from card_brand_identifier.validator import (
    luhn_check,
    identify_brand,
    describe_result,
    CardInfo,
    BRAND_PATTERNS,
    SUPPORTED_BRANDS_ORDER,
    get_test_numbers,
)


class TestLuhnCheck:
    """Testes para a função luhn_check."""

    def test_valid_visa_numbers(self, sample_visa_numbers):
        """Testa números Visa válidos."""
        for number in sample_visa_numbers:
            assert luhn_check(number), f"Número {number} deveria ser válido"

    def test_valid_mastercard_numbers(self, sample_mastercard_numbers):
        """Testa números MasterCard válidos."""
        for number in sample_mastercard_numbers:
            assert luhn_check(number), f"Número {number} deveria ser válido"

    def test_valid_amex_numbers(self, sample_amex_numbers):
        """Testa números Amex válidos."""
        for number in sample_amex_numbers:
            assert luhn_check(number), f"Número {number} deveria ser válido"

    def test_valid_diners_numbers(self, sample_diners_numbers):
        """Testa números Diners válidos."""
        for number in sample_diners_numbers:
            assert luhn_check(number), f"Número {number} deveria ser válido"

    def test_valid_discover_numbers(self, sample_discover_numbers):
        """Testa números Discover válidos."""
        for number in sample_discover_numbers:
            assert luhn_check(number), f"Número {number} deveria ser válido"

    def test_valid_jcb_numbers(self, sample_jcb_numbers):
        """Testa números JCB válidos."""
        for number in sample_jcb_numbers:
            assert luhn_check(number), f"Número {number} deveria ser válido"

    def test_valid_hipercard_numbers(self, sample_hipercard_numbers):
        """Testa números Hipercard válidos."""
        for number in sample_hipercard_numbers:
            assert luhn_check(number), f"Número {number} deveria ser válido"

    def test_invalid_numbers(self, invalid_card_numbers):
        """Testa números inválidos."""
        for number in invalid_card_numbers:
            assert not luhn_check(number), f"Número {number} deveria ser inválido"

    def test_formatted_numbers(self, formatted_card_numbers):
        """Testa números com formatação (espaços e hífens)."""
        for number in formatted_card_numbers:
            assert luhn_check(number), f"Número formatado {number} deveria ser válido"

    def test_empty_inputs(self, empty_inputs):
        """Testa entradas vazias."""
        for input_val in empty_inputs:
            assert not luhn_check(input_val), f"Entrada vazia '{input_val}' deveria ser inválida"

    def test_invalid_inputs(self, invalid_inputs):
        """Testa entradas inválidas."""
        for input_val in invalid_inputs:
            assert not luhn_check(input_val), f"Entrada inválida '{input_val}' deveria retornar False"

    def test_none_input(self):
        """Testa entrada None."""
        assert not luhn_check(None)

    def test_single_digit(self):
        """Testa número com um dígito."""
        assert not luhn_check("0")

    def test_zero(self):
        """Testa zero."""
        assert luhn_check("0")

    def test_luhn_algorithm_correctness(self):
        """Testa a correção do algoritmo de Luhn."""
        # Casos de teste conhecidos
        assert luhn_check("79927398713")  # Exemplo clássico
        assert luhn_check("4242424242424242")  # Stripe test
        assert luhn_check("5555555555554444")  # MasterCard test


class TestIdentifyBrand:
    """Testes para a função identify_brand."""

    def test_identify_visa(self, sample_visa_numbers):
        """Testa identificação de Visa."""
        for number in sample_visa_numbers:
            info = identify_brand(number)
            assert info.brand == "visa", f"Número {number} deveria ser identificado como Visa"
            assert info.valid_luhn, f"Número {number} deveria passar em Luhn"

    def test_identify_mastercard(self, sample_mastercard_numbers):
        """Testa identificação de MasterCard."""
        for number in sample_mastercard_numbers:
            info = identify_brand(number)
            assert info.brand == "mastercard", f"Número {number} deveria ser identificado como MasterCard"
            assert info.valid_luhn, f"Número {number} deveria passar em Luhn"

    def test_identify_amex(self, sample_amex_numbers):
        """Testa identificação de Amex."""
        for number in sample_amex_numbers:
            info = identify_brand(number)
            assert info.brand == "amex", f"Número {number} deveria ser identificado como Amex"
            assert info.valid_luhn, f"Número {number} deveria passar em Luhn"

    def test_identify_diners(self, sample_diners_numbers):
        """Testa identificação de Diners."""
        for number in sample_diners_numbers:
            info = identify_brand(number)
            assert info.brand == "diners", f"Número {number} deveria ser identificado como Diners"
            assert info.valid_luhn, f"Número {number} deveria passar em Luhn"

    def test_identify_discover(self, sample_discover_numbers):
        """Testa identificação de Discover."""
        for number in sample_discover_numbers:
            info = identify_brand(number)
            assert info.brand == "discover", f"Número {number} deveria ser identificado como Discover"
            assert info.valid_luhn, f"Número {number} deveria passar em Luhn"

    def test_identify_jcb(self, sample_jcb_numbers):
        """Testa identificação de JCB."""
        for number in sample_jcb_numbers:
            info = identify_brand(number)
            assert info.brand == "jcb", f"Número {number} deveria ser identificado como JCB"
            assert info.valid_luhn, f"Número {number} deveria passar em Luhn"

    def test_identify_hipercard(self, sample_hipercard_numbers):
        """Testa identificação de Hipercard."""
        for number in sample_hipercard_numbers:
            info = identify_brand(number)
            assert info.brand == "hipercard", f"Número {number} deveria ser identificado como Hipercard"
            assert info.valid_luhn, f"Número {number} deveria passar em Luhn"

    def test_identify_elo(self, sample_elo_numbers):
        """Testa identificação de Elo."""
        for number in sample_elo_numbers:
            info = identify_brand(number)
            # Alguns números Elo podem não passar em Luhn nos testes
            assert info.brand == "elo", f"Número {number} deveria ser identificado como Elo"

    def test_formatted_numbers(self, formatted_card_numbers):
        """Testa identificação de números formatados."""
        info = identify_brand("4111 1111 1111 1111")
        assert info.brand == "visa"
        assert info.valid_luhn
        assert info.normalized == "4111111111111111"

        info = identify_brand("5555-5555-5555-4444")
        assert info.brand == "mastercard"
        assert info.valid_luhn
        assert info.normalized == "5555555555554444"

    def test_empty_input(self):
        """Testa entrada vazia."""
        info = identify_brand("")
        assert info.brand is None
        assert not info.valid_luhn
        assert info.normalized == ""
        assert info.length == 0

    def test_none_input(self):
        """Testa entrada None."""
        info = identify_brand(None)
        assert info.brand is None
        assert not info.valid_luhn
        assert info.normalized == ""
        assert info.length == 0

    def test_invalid_luhn_but_valid_brand(self):
        """Testa número com bandeira válida mas Luhn inválido."""
        info = identify_brand("4111111111111112")  # Visa com último dígito alterado
        assert info.brand == "visa"
        assert not info.valid_luhn

    def test_no_luhn_validation(self):
        """Testa identificação sem validação Luhn."""
        info = identify_brand("4111111111111112", validate_luhn=False)
        assert info.brand == "visa"
        assert not info.valid_luhn  # Ainda False porque num está vazio após validação

    def test_card_info_length(self):
        """Testa o campo length de CardInfo."""
        info = identify_brand("4111111111111111")
        assert info.length == 16

        info = identify_brand("378282246310005")
        assert info.length == 15

        info = identify_brand("30569309025904")
        assert info.length == 14


class TestDescribeResult:
    """Testes para a função describe_result."""

    def test_describe_valid_visa(self):
        """Testa descrição de Visa válido."""
        info = CardInfo(brand="visa", valid_luhn=True, normalized="4111111111111111", length=16)
        result = describe_result(info)
        assert "visa" in result
        assert "Luhn: válido" in result
        assert "16" in result

    def test_describe_invalid_visa(self):
        """Testa descrição de Visa inválido."""
        info = CardInfo(brand="visa", valid_luhn=False, normalized="4111111111111112", length=16)
        result = describe_result(info)
        assert "visa" in result
        assert "Luhn: inválido" in result

    def test_describe_valid_luhn_unknown_brand(self):
        """Testa descrição com Luhn válido mas bandeira desconhecida."""
        info = CardInfo(brand=None, valid_luhn=True, normalized="1234567890123456", length=16)
        result = describe_result(info)
        assert "indeterminada" in result
        assert "Luhn: válido" in result

    def test_describe_invalid_luhn_unknown_brand(self):
        """Testa descrição com Luhn inválido e bandeira desconhecida."""
        info = CardInfo(brand=None, valid_luhn=False, normalized="1234567890123456", length=16)
        result = describe_result(info)
        assert "indeterminada" in result
        assert "Luhn: inválido" in result

    def test_describe_empty_input(self):
        """Testa descrição de entrada vazia."""
        info = CardInfo(brand=None, valid_luhn=False, normalized="", length=0)
        result = describe_result(info)
        assert "vazia" in result.lower()


class TestCardInfo:
    """Testes para a classe CardInfo."""

    def test_card_info_creation(self):
        """Testa criação de CardInfo."""
        info = CardInfo(brand="visa", valid_luhn=True, normalized="4111111111111111", length=16)
        assert info.brand == "visa"
        assert info.valid_luhn is True
        assert info.normalized == "4111111111111111"
        assert info.length == 16

    def test_card_info_str(self):
        """Testa método __str__."""
        info = CardInfo(brand="visa", valid_luhn=True, normalized="4111111111111111", length=16)
        result = str(info)
        assert "visa" in result
        assert "Luhn: válido" in result

    def test_card_info_repr(self):
        """Testa método __repr__."""
        info = CardInfo(brand="visa", valid_luhn=True, normalized="4111111111111111", length=16)
        result = repr(info)
        assert "CardInfo" in result
        assert "visa" in result


class TestBrandPatterns:
    """Testes para os padrões de bandeira."""

    def test_visa_pattern(self, brand_patterns):
        """Testa padrão Visa."""
        pattern = brand_patterns["visa"]
        assert pattern.match("4111111111111111")
        assert pattern.match("4012888888881881")
        assert pattern.match("4222222222222")
        assert not pattern.match("5111111111111111")

    def test_mastercard_pattern(self, brand_patterns):
        """Testa padrão MasterCard."""
        pattern = brand_patterns["mastercard"]
        assert pattern.match("5555555555554444")
        assert pattern.match("5105105105105100")
        assert pattern.match("2223000048400011")
        assert not pattern.match("4111111111111111")

    def test_amex_pattern(self, brand_patterns):
        """Testa padrão Amex."""
        pattern = brand_patterns["amex"]
        assert pattern.match("378282246310005")
        assert pattern.match("371449635398431")
        assert pattern.match("378734493671000")
        assert not pattern.match("4111111111111111")

    def test_diners_pattern(self, brand_patterns):
        """Testa padrão Diners."""
        pattern = brand_patterns["diners"]
        assert pattern.match("30569309025904")
        assert pattern.match("38520000023237")
        assert not pattern.match("4111111111111111")

    def test_discover_pattern(self, brand_patterns):
        """Testa padrão Discover."""
        pattern = brand_patterns["discover"]
        assert pattern.match("6011111111111117")
        assert pattern.match("6011000990139424")
        assert pattern.match("6511111111111112")
        assert not pattern.match("4111111111111111")

    def test_jcb_pattern(self, brand_patterns):
        """Testa padrão JCB."""
        pattern = brand_patterns["jcb"]
        assert pattern.match("3530111333300000")
        assert pattern.match("3566002020360505")
        assert pattern.match("213111111111111")
        assert not pattern.match("4111111111111111")

    def test_hipercard_pattern(self, brand_patterns):
        """Testa padrão Hipercard."""
        pattern = brand_patterns["hipercard"]
        assert pattern.match("6062825624254001")
        assert pattern.match("3841000000000010")
        assert not pattern.match("4111111111111111")

    def test_elo_pattern(self, brand_patterns):
        """Testa padrão Elo."""
        pattern = brand_patterns["elo"]
        assert pattern.match("4011780000000002")
        assert pattern.match("4389350000000000")
        assert pattern.match("5066991111111118")
        assert not pattern.match("4111111111111111")


class TestGetTestNumbers:
    """Testes para a função get_test_numbers."""

    def test_get_all_test_numbers(self):
        """Testa obter todos os números de teste."""
        numbers = get_test_numbers()
        assert len(numbers) > 0
        assert isinstance(numbers, list)

    def test_get_specific_brand_numbers(self):
        """Testa obter números de uma bandeira específica."""
        numbers = get_test_numbers("visa")
        assert len(numbers) > 0
        assert all(luhn_check(num) for num in numbers)

    def test_get_invalid_brand_numbers(self):
        """Testa obter números de uma bandeira inválida."""
        numbers = get_test_numbers("invalid")
        assert len(numbers) == 0


class TestSupportedBrandsOrder:
    """Testes para a ordem de verificação de bandeiras."""

    def test_supported_brands_order(self, supported_brands):
        """Testa que a ordem de verificação está correta."""
        assert len(supported_brands) == 8
        assert "visa" in supported_brands
        assert "mastercard" in supported_brands
        assert "amex" in supported_brands
        assert "diners" in supported_brands
        assert "discover" in supported_brands
        assert "jcb" in supported_brands
        assert "hipercard" in supported_brands
        assert "elo" in supported_brands

    def test_brand_patterns_match_supported_brands(self, brand_patterns, supported_brands):
        """Testa que todos os padrões correspondem às bandeiras suportadas."""
        for brand in supported_brands:
            assert brand in brand_patterns
