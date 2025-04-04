"""Expresiones Booleanas."""


def es_vocal_if(letra: str) -> bool:
    if letra.lower() == "a":
        return True
    elif letra[0].lower() == "e":
        return True
    elif letra[0].lower() == "i":
        return True
    elif letra[0].lower() == "o":
        return True
    elif letra[0].lower() == "u":
        return True
    else:
        return False


# NO MODIFICAR - INICIO
assert es_vocal_if("a")
assert not es_vocal_if("b")
assert es_vocal_if("A")
# NO MODIFICAR - FIN


###############################################################################


def es_vocal_if_in(letra: str) -> bool:
    if letra.lower() in ("a", "e", "i", "o", "u"):
        return True
    else:
        return False


# NO MODIFICAR - INICIO
assert es_vocal_if_in("a")
assert not es_vocal_if_in("b")
assert es_vocal_if_in("A")
# NO MODIFICAR - FIN


###############################################################################


def es_vocal_in(letra: str) -> bool:
    return letra.lower() in "aeiou"


# NO MODIFICAR - INICIO
assert es_vocal_in("a")
assert not es_vocal_in("b")
assert es_vocal_in("A")
# NO MODIFICAR - FIN
