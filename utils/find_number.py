def find_number(s: str) -> int:
    res = 0

    for c in str(s):
        if c.isdigit():
            res = res * 10 + int(c)

    return res