"""
Card Brand Identifier - Identificador de Bandeira de Cartão

Uma biblioteca Python para identificar a bandeira de cartões de crédito
e validar números usando o algoritmo de Luhn.

Suporta as seguintes bandeiras:
- Visa
- MasterCard
- American Express (Amex)
- Diners Club
- Discover
- JCB
- Elo
- Hipercard
"""

from .validator import (
    CardInfo,
    BRAND_PATTERNS,
    SUPPORTED_BRANDS_ORDER,
    luhn_check,
    identify_brand,
    describe_result,
)

__version__ = "1.0.0"
__all__ = [
    "CardInfo",
    "BRAND_PATTERNS",
    "SUPPORTED_BRANDS_ORDER",
    "luhn_check",
    "identify_brand",
    "describe_result",
]
