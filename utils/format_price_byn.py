def format_price_byn(price: int):
    s = str(price)
    while len(s) < 3:
        s = '0' + s

    return f'{s[:len(s) - 2]},{s[len(s) - 2:]} BYN'