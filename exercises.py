# Написати функцію, яка отримує рядок і виводить його з великої літери
# ihor -> Ihor

def capitalize(word: str): # ihor
    # word[0] -> i
    # word[1:] -> hor
    return word.capitalize()
    # return f'{word[0].upper()}{word[1:]}'

# print('ihor'[1:4]) # word[start:end]
# print(capitalize('ihor'))

# Написати функцію, яка отримає речення та виведе слова у реченні у зрототньому порядку
# 'Hello world, hello people!' -> 'People hello world hello'
def clean_extra_symbols(sentence: str) -> str:
    # return sentence.replace(',' or '!' or '.', '')
    return sentence.replace(',', '').replace('!', '').replace('.', '')

def reverse_words_in_sentence(sentence: str) -> str:
    # Прибрати знаки
    cleaned_sentence = clean_extra_symbols(sentence)
    # Розділити речення на окремі слова
    words_list = cleaned_sentence.split() # 'Hello world, hello people!' -> ['Hello', 'world,', 'hello', 'people!']
    # Змінити порядок слів
    words_list = words_list[::-1]
    # Зробити перше слово з великої, старе перше з малої
    # [1, 2, 3]
    # lst[2] = 4
    words_list[-1] = words_list[-1].lower()
    words_list[0] = capitalize(words_list[0])
    return ' '.join(words_list)

# print(reverse_words_in_sentence('Hello world, hello people!'))

def wrong_function(numbers_list):
    numbers_sum = 0
    for number in numbers_list:
        numbers_sum += number
    return numbers_sum

# print(wrong_function([1, 2, 3, 4, 5]))

# variable_one = 2
# variable_two = 3

# print(variable_one + variable_two)
# print(variable_one - variable_two)
# print(variable_one * variable_two)
# print(variable_one / variable_two)
# print(variable_one, variable_two)

# variable_one += variable_two # variable_one = variable_one + variable_two
# print(variable_one)

# += 
# -=
# *=
# /=

# result = 'a'
# Strb = 'b'
# result += Strb

# # print(result) # ab

# result *= 8
# print(result)

# * та /x = 2
# x //=2-1      # 2 x= x // (2-1)
# x = x//2-1     # 0

# def outFn():
#     count = 0
#     def inFn():
#         nonlocal count
#         count +=1
#         return count
#     return inFn
# counter = outFn()
# print(counter()) #1
# print(counter()) #2

# Замикання (closure)
def closure():
    count = 0
    def add(n):
        nonlocal count
        count += n
        return count
    return add

# my_add = closure()
# print(my_add(5))

# my_second_add = closure()
# print(my_second_add(2))

def add_numbers():
    first = 1
    second = 2
    result = first + second
    return result

print(add_numbers())
print(add_numbers())
print(add_numbers())
print(add_numbers())
print(add_numbers())
