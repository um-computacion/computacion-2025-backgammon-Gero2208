"""
Este módulo define las excepciones personalizadas para el juego de Backgammon.
"""


class BackgammonException(Exception):
    """Clase base para excepciones personalizadas en el juego de Backgammon."""


class MovimientoInvalido(BackgammonException):
    """Excepción para movimientos inválidos en Backgammon."""


class DadoInvalido(BackgammonException):
    """Excepción para un dado no válido o no disponible."""


class OrigenInvalido(BackgammonException):
    """Excepción para un origen de movimiento no válido."""
