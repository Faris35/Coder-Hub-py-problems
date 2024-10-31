from typing import List

def cap_space(txt: str) -> str:
    return ''.join([' ' + i.lower() if i.isupper() else i for i in txt])

