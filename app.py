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


# ======================================Question Eleven==========================

# phone_book = {
#     "John Doe": "09111234562",
#     "Jane Smith": "09359876543",
#     "Alice Johnson": "09114567894",
#     "Bob Thompson": "09357891233",
#     "Emily Davis": "09112461358",
#     "Michael Wilson": "09351352496",
#     "Sarah Anderson": "09115793507",
#     "David Clark": "09353575789",
#     "Olivia Baker": "09118246850",
#     "Daniel Green": "09356808244",
#     "Sophia King": "09114682436",
#     "William Lee": "09352464681",
#     "Mia Miller": "09113575799",
#     "Joseph Hill": "09355793576",
#     "Grace Adams": "09112461357",
#     "Andrew Parker": "09351352465",
#     "Elizabeth Stewart": "09115793570",
#     "Matthew Turner": "09353575749",
#     "Ava Bennett": "09116808234",
#     "Anthony Morgan": "09358246820",
#     "Chloe Cook": "09112464628",
#     "Christopher Reed": "09354682426",
#     "Victoria Scott": "09115793574",
#     "Ryan Phillips": "09353575795",
#     "Ella Young": "09111352466",
#     "Benjamin Hall": "09352461359",
# }

# while True:
#     option = input(
#         "Please Choose an option (add to add a new number / src to search a number) :").lower()
#     if option == "add":
#         while True:
#             name_to_add = input("Please enter a name: ")
#             number_to_add = input("Please enter a number: ")
#             if name_to_add != "" and number_to_add.isnumeric():
#                 phone_book[name_to_add] = number_to_add
#                 print("Your Contact number successfully Saved!")
#                 break
#             else:
#                 print("Wrong name or phone number. Please retry!")
#                 retry = input("Type 'c' to continue or 'e' to exit: ")
#                 if retry == "e":
#                     break
#                 else:
#                     pass
#     elif option == "src":
#         while True:
#             print("You can 'exit' by typing exit")
#             name_to_search = input("Please enter a Name to search: ")
#             if name_to_search != "" and name_to_search.lower() != "exit":
#                 result = [f"{key} :  {value}" for key,
#                           value in phone_book.items() if name_to_search in key]
#                 for num in result:
#                     print(num)
#             elif name_to_search.lower() == "exit":
#                 break
#             else:
#                 print("Not Found! Try again.")
#     else:
#         print("Firstly, select an option (add or src)")

# class Point:

#     default_color = "red"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x}, {self.y})"

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)

#     @classmethod
#     def zero(cls):
#         return cls(0, 0)

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# point = Point(1, 2)
# point = Point.zero()
# point.draw()


# point = Point(2, 3)
# other = Point(1, 2)

# print(point + other)

# print(point.__dict__)

# class Product:
#     def __init__(self, price):
#         # self.__price = price
#         self.set_price(price)

#     def get_price(self):
#         return self.__price

#     def set_price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative.")
#         self.__price = value
#     price = property(get_price, set_price)


# product = Product(-50)
# product.


# class Product:
#     def __init__(self, price):
#         self.price = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative.")
#         self.__price = value


# product = Product(-50)


# ======================================Question Twelve==========================

# Class name = bank account
# attributes = account_number, balance, currency
# Methods = deposit, withdraw, get_balance

class BankAccount:
    def __init__(self, account_number, balance, currency):
        self.account_number = account_number
        self.balance = balance
        self.currency = currency

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.balance


# Create an instance of the BankAccount class
account = BankAccount("12345", 1000, "USD")

# Perform a deposit of 500
account.deposit(500)

# Perform a withdrawal of 200
account.withdraw(200)

# Print the final balance
print("Final balance:", account.get_balance())
