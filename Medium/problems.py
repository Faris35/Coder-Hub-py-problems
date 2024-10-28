from typing import List
def word_length(arr: List[str]) -> List[int]:
    return [len(item) for item in arr]

def countWords(txt: str) -> int:
    return len(txt.split())

def sub_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    if len(arr1) != len(arr2):
        return []
    return [item2 - item1 for item1, item2 in zip(arr1, arr2)]

def add_five(arr: List[str]) -> List[str]:
    return [] if len(arr) == 0 else [item + "5" for item in arr]

def stringContains(firstName: str, contains: str) -> bool:
    return contains in firstName

def largest_smallest(array_values: List[int]) -> List[int]:
    return [max(array_values), min(array_values)]

def array_root(arr: List[float]) -> List[float]:
    return [round(item ** 0.5, 2) for item in arr]

def sortByLength(txt: str) -> str:
    lst = txt.split()
    lst.sort(key=len)
    return ' '.join(lst)

def count_ones(num: int) -> int:
    return bin(num).count('1')

# NOTE: This function is not correct 
def removeSpecialCharacters(strParam: str) -> str:
    return ''.join(e for e in strParam if e.isalnum() or e == 'ـ' or e == '-')
