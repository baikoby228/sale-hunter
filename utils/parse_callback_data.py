def parse_callback_data(data: str) -> list[str]:
    res = []
    cur = ''
    for x in data:
        if x == '_':
            res.append(cur)
            cur = ''
        else:
            cur += x
    res.append(cur)

    return res