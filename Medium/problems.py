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

def middle_char(word: str) -> str:
    if len(word) <= 2:
        return word
    len1 = int(len(word)/2)
    if len(word)%2==0:
        return word[len1-1:len1+1]
    return word[len1-1]

def oct_to_dec(octal_number: int) -> int:
    return int(str(octal_number),8)

def oct_to_hex(octal_number: int) -> str:
    return (hex(int(str(octal_number), 8))[2:]).upper()

def sort_array(my_array: list[int], typeParam: str) -> list[int]:
    if typeParam == 'B':
        return sorted(my_array,reverse = True)
    return sorted(my_array)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes_nums(numbers: List[int]) -> List[int]:
    primes=[]
    for i in numbers:
        if is_prime(i):
            primes.append(i)
    return primes

def filp_even_odd(numbers: List[int]) -> List[int]:
    return [i+1 if i % 2 ==0 else i-1 for i in numbers]

def compare_two_words(s1: str, s2: str) -> bool:
    return s1[-2:] == s2[-2:]

def find_element(elements_array: List[int], element: int) -> bool:
    return element in elements_array

def longestZero(strParam: str) -> str:
    return (sorted(strParam.split('1'),key=len)[-1])

def find_prefix(words: List[str], text: str) -> List[str]:
    lst=[]
    for i in words:
        if i.lower().startswith(text.lower()):
            lst.append(i)
    return lst if lst else ['No matches found']

def max_element(arr: List[int]) -> int:
    return sorted(arr)[-1]

def smallest_number(arr: List[int]) -> int:
    return sorted(arr)[0]

def cumulative_sum(arr: list[int]) -> list[int]:
    cum_sum = []
    current_sum = 0
    for num in arr:
        current_sum += num
        cum_sum.append(current_sum)
    return cum_sum

def str_len_comparison(words: List[str]) -> bool:
    if len(words) <= 1:
        return False
    for i in range(len(words)-1):
        if len(words[i]) != len(words[i+1]):
            return False
    return True
    
def most_frequent_element(arr: list[int]) -> int:
    return max(set(arr), key=arr.count)