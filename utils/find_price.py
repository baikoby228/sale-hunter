from .find_number import find_number

def find_price(s: str) -> int:
    res = find_number(s)

    if not ',' in s and not '.' in s:
        res *= 100

    return res