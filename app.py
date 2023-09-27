# from timeit import timeit
# =========================Question One==============================
# if 10 == "10":
#     print("a")
# elif "bag" > "apple" and "bag" > "cat":
#     print("b")
# else:
#     print("c")

# =========================Question Two==============================
# n = 10
# spaces = n-1
# for number in range(1, n, 2):
#     print((spaces)*" "+number*"*")
#     spaces -= 1


# =========================Question Three==============================
# command = ""
# while command.lower() != "exit":
#     command = input(">>>: ")
#     print("Echo", command)


# =========================Question Four==============================
# def average():
#     summery, counter = 0, 0
#     while True:
#         number = int(input("Enter your Number to Calculate New Average :"))
#         if number != 0:
#             summery += number
#             counter += 1
#             print(f"The Current Average is: {summery//counter}")
#         else:
#             print(f"The Last Average is: {summery//counter}")
#             break


# average()


# =========================Question Five==============================
# def greeting():
#     while True:
#         name = input("Please enter your name:")
#         if name != "" and name.strip() != "" and name.lower() != "exit":
#             print(f"Hi {name}. Nice to meet you!")
#         elif name.lower() == "exit":
#             print("Goodbye!")
#             break
#         else:
#             print("Please Enter a Correct Name!")


# greeting()


# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print("Start")
# print(multiply(1, 2, 3))


# =========================Question six================================
# def fizz_buzz(number):
#     if number % 3 == 0 and number % 5 == 0:
#         print("Fizz_Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)


# fizz_buzz(29)


# =========================Question Seven==============================
# def count_vowels(word):
#     vowels = "aeiou"
#     count = 0
#     word = word.lower()
#     for char in word:
#         if char in vowels:
#             count += 1
#     return count


# def reverse_string(sentence):
#     reversed_sentence = ""
#     word = ""
#     i = len(sentence) - 1
#     while i >= 0:
#         if sentence[i] == " ":
#             reversed_sentence += word[::-1] + " "
#             word = ""
#         else:
#             word += sentence[i]
#         i -= 1
#     reversed_sentence += word[::-1]
#     return reversed_sentence


# def main():
#     sentence_input = input("Enter a sentence: ")
#     vowels_count = count_vowels(sentence_input)
#     print(f"The number of vowels in '{sentence_input }' is: {vowels_count}")
#     reversed_sentence = reverse_string(sentence_input)
#     print(f"The reversed sentence is: {reversed_sentence}")


# main()


# =========================Question Eight==============================

# def remove_duplicates(strings):
#     unique_strings = []
#     for string in strings:
#         if string not in unique_strings:
#             unique_strings.append(string)
#     return unique_strings


# def find_longest_word(words):
#     longest_word = ""
#     for word in words:
#         if len(word) > len(longest_word):
#             longest_word = word
#     return longest_word


# def main():

#     strings = ["apple", "banana", "cherry", "apple", "kiwi", "banana"]
#     unique_strings = remove_duplicates(strings)
#     print("Unique strings:", unique_strings)

#     words = ["cat", "elephant", "tiger", "lion", "giraffe"]
#     longest_word = find_longest_word(words)
#     print("Longest word:", longest_word)


# main()

# ===============================Data structures=====================
# lst = [
#     ("p1", 10),
#     ("p2", 9),
#     ("p3", 12)
# ]


# def sort_item(item):
#     return item[1]


# lst.sort(key=sort_item)
# print(lst)

# prices = []
# for item in lst:
#     prices.append(item[1])

# prices = map(lambda item: item[1], lst)
# prices = [item[1] for item in lst]
# print(prices)


# filtered = filter(lambda item: item[1] >= 10, lst)
# filtered = [item for item in lst if item[1] >= 10]
# print(filtered)

# lst1 = ["a", "b", "c"]
# lst2 = [1, 2, 3]

# x = zip("@#$", lst1, lst2)
# print(list(x))


# =========================Question Nine==============================
# dict1 = {"a": -12, "b": 10, "c": 5, "d": -2, "e": 6, "f": 22, "g": 0}
# print([item if item >= 0 else 0 for item in dict1.values()])


# =========================Question Ten==============================

# sentence = "This is a common interview question"

# char_frequency = {}
# for char in sentence:
#     if char not in char_frequency:
#         char_frequency[char] = 1
#     else:
#         char_frequency[char] += 1

# char_frequency_sorted = sorted(char_frequency.items(),
#                                key=lambda kv: kv[1],
#                                reverse=True)
# print(char_frequency_sorted[0])


# ================================Exceptions Examples==========================

# while True:
#     try:
#         x = int(input("Enter a number: "))
#         print(x)
#     except ValueError:
#         print("Please Enter a Number!")


# code1 = """
# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be zero or less!")
#     return 10 / age


# try:
#     calculate_xfactor(-1)
# except ValueError as error:
#     #print(error)
#     pass
# """

# code2 = """
# def calculate_xfactor(age):
#     if age <= 0:
#         return None
#     return 10 / age


# xfactor = calculate_xfactor(-1)
# if xfactor == None:
#     pass
# """

# print("First code time: ", timeit(code1, number=10000))
# print("Second code time: ", timeit(code2, number=10000))


# ======================================classes==========================
