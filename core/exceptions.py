class BackgammonException(Exception):
    """Clase base para excepciones personalizadas en el juego de Backgammon."""
    pass

class MovimientoInvalido(BackgammonException):
    """Excepción para movimientos inválidos en Backgammon."""
    pass

class DadoInvalido(BackgammonException):
    """Excepción para un dado no válido o no disponible."""
    pass

class OrigenInvalido(BackgammonException):
    """Excepción para un origen de movimiento no válido."""
    pass
