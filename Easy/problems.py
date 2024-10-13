from typing import Counter, List
def Decimal_places(num: str) -> int:
    if "." not in num:
        return 0
    return len(num.split(".")[1])

def say_hi_bye(name: str, num: int) -> str:
    if num == 1:
        return f"Hi {name}"
    return f"Bye {name}"

def input_type(value: str) -> str:
    try:
        int_value = int(value)
        return 'integer'
    except ValueError:
        try:
            float_value = float(value)
            return 'double'
        except ValueError:
            return 'string'

def sum_two_smallest_nums(arr: List[int]) -> int:
    arr.sort()
    return arr[0] + arr[1]

def number_sum(num: int) -> int:
    i = 0
    sum=0
    for i in range(num):
        i=i+1
        sum+=i
        print(f"i = {i}")
        print(f"sum = {sum}")
    return sum

def stringCheck(value: List[str]) -> bool:
    for _ in range(len(value)-1):
        if not (value[_] == value[_+1]):
            return False
    return True

def canForm(source: str, target: str) -> str:
    if len(target) > len(source):
        return "no"
    target = target.lower()
    source = source.lower()
    for i in range(len(target)):
        if target[i] not in source:
            return "no"
    return "yes"

def is_same(name1: str, name2: str) -> str:
    return "متشابهتين" if name1 == name2 else "غير متشابهتين"

def repetitions(s: str) -> int:
    max_count = 0  
    current_count = 1  
 
    if not s:
        return 0

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_count += 1 
        else:
            max_count = max(max_count, current_count)  
            current_count = 1  

    max_count = max(max_count, current_count)
    return max_count

def search(word: str, character: str) -> int:
    # find the index of the character in the word and -1 if there is no character
    if character not in word:
        return -1
    return word.index(character)

def string_builder(expression: str) -> str:
    num = 0  
    for i in expression:
        if i.isdecimal():
            num = int(i)
        elif i.isalpha():
            return i*num
        
    return

def sumOdd(arr: List[int]) -> int:
    sum=0
    for number in arr:
        if number % 2 == 1:
            sum += number
    return sum

def concat_names(name1: str, name2: str) -> str:
    return name1 + " " + name2

def word_repeat(word: str, n: int) -> str:
    word = word+" "
    word = word*n
    return word[0:len(word)-1]


def calculate_sum(lst: List[int]) -> int:
    sum=0
    for number in lst:
        if number == 7:
            return sum
        else:
            sum+=number
    return sum

def cumulative_addition(elements_array: List[int]) -> List[int]:
    return [sum(elements_array),len(elements_array)]

def average(values: List[int]) -> float:
    return sum(values)/len(values)

import math
def calculate_circumference(radius: float) -> float:
    return radius*2*3.14159

def cubicRoot(num: int) -> float:
    return num**(1/3)

def mergeAndOrder(array1: List[int], array2: List[int]) -> List[int]:
    res_arr = array1+array2
    res_arr.sort()
    return res_arr

def find_circle_area(radius: float) -> float:
    return math.pi*radius**2

def cone_volume(radius: float, height: float) -> float:
    return math.pi*radius**2*height/3

def countdown(num: int) -> List[int]:
    countdown_list = []
    
    for i in range(num - 3, -1, -3):
        if i % 2 == 0 and i != 0:
            countdown_list.append(i)
    
    if not countdown_list:
        return [0]
    
    return sorted(countdown_list)

def root_check(sqr: float, num: int) -> int:
    return sqr if num ** 0.5 == sqr else 0

def reverse_case(strParam: str) -> str:
    return strParam.swapcase()

def factorial(number: int) -> int:
    if number == 0:
        return 1
    return number * factorial(number - 1)

def isMirrored(num: int) -> bool:
    return str(num) == str(num)[::-1]

def remove_duplicate(arr: List[int]) -> List[int]:
    #remove duplicates from the list and keep it in the same order
    return list(dict.fromkeys(arr))

def count_char(sentence: str, ch: str) -> int:
    return sentence.count(ch)

def hashtag_it(my_array: List[str]) -> str:
    sen = ""
    my_array = ["#"+item for item in my_array]
    
    sen = " ".join(my_array)

    return sen

def left_digit(strParam: str) -> int:
    for char in strParam:
        if char.isdigit():
            return int(char)

# check if the all strings in the array are the same even if the order is different
def match_arrays(array1: List[str], array2: List[str]) -> bool:
    return sorted(array1) == sorted(array2)

def replaceThe(txt: str) -> str:
    txt = txt.split()
    for i in range(len(txt)):
        if txt[i] == "the":
            if txt[i+1][0] in "aeiou":
                txt[i] = "an"
            else:
                txt[i] = "a"
    return " ".join(txt)

def getPrimesBetween(a: int, b: int) -> List[int]:
    primes = []
    for num in range(a,b+1):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes

def countDown(number: int) -> str:
    return " ".join([str(i) for i in range(number,-1,-1)])

def allSameCase(word: str) -> bool:
    return word.islower() or word.isupper()

def operation(num1: int, num2: int) -> str:
    if num1 + num2 == 24:
        return "added"
    elif num1 - num2 == 24:
        return "subtracted"
    elif num1 / num2 == 24:
        return "divided"
    elif num1 * num2 == 24:
        return "multiplied"
    return "None"

def numbers_range(number: int) -> str:
    return " ".join([str(i) for i in range(0,number+1)])

def getBiggestShared(a: List[int], b: List[int]) -> int:
    return max(set(a).intersection(b))

def less_or_more_than_zero(number: int) -> str:
    return "Greater than zero" if number > 0 else "Less than zero" if number < 0 else "Equal to zero"

def reverse_words(str1: str, str2: str) -> str:
    return str2+", "+str1

def get_duplicate_elements(arr: List[int]) -> List[int]:
    counts = Counter(arr)
    return [element for element, count in counts.items() if count > 1]

def gravity_flip(columns: List[int]) -> List[int]:
    return sorted(columns)

# input: 3[a]2[bc]
def string_builder(expression: str) -> str:
    stack = []
    current_string = ""
    current_number = 0

    for char in expression:
        if char == "[":
            stack.append(current_string)
            stack.append(current_number)
            current_string = ""
            current_number = 0
        elif char == "]":
            number = stack.pop()
            prev_string = stack.pop()
            current_string = prev_string + number * current_string
        elif char.isdigit():
            current_number = current_number * 10 + int(char)
        else:
            current_string += char

    return current_string

def increasing_array(arr: List[int]) -> int:
    count = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            count += 1
            arr[i] = arr[i-1]
    return count

arr = [3, 2, 5, 1, 7]
print(increasing_array(arr)) # 5