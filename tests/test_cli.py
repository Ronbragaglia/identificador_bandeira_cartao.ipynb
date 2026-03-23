"""
Testes para o módulo CLI.
"""

import pytest
from io import StringIO
import sys
from unittest.mock import patch

from card_brand_identifier.cli import (
    print_banner,
    print_supported_brands,
    get_brand_icon,
    identify_card,
    main,
)


class TestPrintBanner:
    """Testes para a função print_banner."""

    def test_print_banner(self, capsys):
        """Testa impressão do banner."""
        print_banner()
        captured = capsys.readouterr()
        assert "Card Brand Identifier" in captured.out
        assert "Identificador de Bandeira de Cartão" in captured.out


class TestPrintSupportedBrands:
    """Testes para a função print_supported_brands."""

    def test_print_supported_brands(self, capsys):
        """Testa impressão das bandeiras suportadas."""
        print_supported_brands()
        captured = capsys.readouterr()
        assert "Bandeiras Suportadas" in captured.out
        assert "visa" in captured.out.lower()
        assert "mastercard" in captured.out.lower()
        assert "amex" in captured.out.lower()


class TestGetBrandIcon:
    """Testes para a função get_brand_icon."""

    def test_get_visa_icon(self):
        """Testa ícone Visa."""
        assert get_brand_icon("visa") == "💳"

    def test_get_mastercard_icon(self):
        """Testa ícone MasterCard."""
        assert get_brand_icon("mastercard") == "💳"

    def test_get_amex_icon(self):
        """Testa ícone Amex."""
        assert get_brand_icon("amex") == "💳"

    def test_get_diners_icon(self):
        """Testa ícone Diners."""
        assert get_brand_icon("diners") == "💳"

    def test_get_discover_icon(self):
        """Testa ícone Discover."""
        assert get_brand_icon("discover") == "💳"

    def test_get_jcb_icon(self):
        """Testa ícone JCB."""
        assert get_brand_icon("jcb") == "💳"

    def test_get_hipercard_icon(self):
        """Testa ícone Hipercard."""
        assert get_brand_icon("hipercard") == "💳"

    def test_get_elo_icon(self):
        """Testa ícone Elo."""
        assert get_brand_icon("elo") == "💳"

    def test_get_unknown_icon(self):
        """Testa ícone para bandeira desconhecida."""
        assert get_brand_icon("unknown") == "❓"

    def test_get_none_icon(self):
        """Testa ícone para None."""
        assert get_brand_icon(None) == "❓"


class TestIdentifyCard:
    """Testes para a função identify_card."""

    def test_identify_visa(self, capsys):
        """Testa identificação de Visa."""
        identify_card("4111111111111111", verbose=False)
        captured = capsys.readouterr()
        assert "visa" in captured.out
        assert "Luhn: válido" in captured.out

    def test_identify_mastercard(self, capsys):
        """Testa identificação de MasterCard."""
        identify_card("5555555555554444", verbose=False)
        captured = capsys.readouterr()
        assert "mastercard" in captured.out
        assert "Luhn: válido" in captured.out

    def test_identify_verbose(self, capsys):
        """Testa identificação em modo verbose."""
        identify_card("4111111111111111", verbose=True)
        captured = capsys.readouterr()
        assert "Informações Detalhadas" in captured.out
        assert "Número original" in captured.out
        assert "Número normalizado" in captured.out
        assert "Quantidade de dígitos" in captured.out


class TestMain:
    """Testes para a função main."""

    @patch("sys.argv", ["card-identify", "--brands"])
    def test_main_brands(self, capsys):
        """Testa main com flag --brands."""
        result = main()
        captured = capsys.readouterr()
        assert result == 0
        assert "Bandeiras Suportadas" in captured.out

    @patch("sys.argv", ["card-identify", "--test"])
    def test_main_test(self, capsys):
        """Testa main com flag --test."""
        result = main()
        captured = capsys.readouterr()
        assert result == 0
        assert "Executando Testes" in captured.out

    @patch("sys.argv", ["card-identify", "4111111111111111"])
    def test_main_with_number(self, capsys):
        """Testa main com número de cartão."""
        result = main()
        captured = capsys.readouterr()
        assert result == 0
        assert "visa" in captured.out

    @patch("sys.argv", ["card-identify", "4111111111111111", "--verbose"])
    def test_main_with_number_verbose(self, capsys):
        """Testa main com número e flag --verbose."""
        result = main()
        captured = capsys.readouterr()
        assert result == 0
        assert "Informações Detalhadas" in captured.out

    @patch("sys.argv", ["card-identify", "--no-banner", "4111111111111111"])
    def test_main_no_banner(self, capsys):
        """Testa main com flag --no-banner."""
        result = main()
        captured = capsys.readouterr()
        assert result == 0
        assert "Card Brand Identifier" not in captured.out

    @patch("sys.argv", ["card-identify"])
    def test_main_no_args(self, capsys):
        """Testa main sem argumentos."""
        result = main()
        captured = capsys.readouterr()
        assert result == 0
        assert "Identificador de Bandeira de Cartão de Crédito" in captured.out

    @patch("sys.argv", ["card-identify", "--help"])
    def test_main_help(self, capsys):
        """Testa main com flag --help."""
        with pytest.raises(SystemExit):
            main()

    @patch("sys.argv", ["card-identify", "invalid"])
    def test_main_invalid_number(self, capsys):
        """Testa main com número inválido."""
        result = main()
        captured = capsys.readouterr()
        assert result == 0
        assert "indeterminada" in captured.out
