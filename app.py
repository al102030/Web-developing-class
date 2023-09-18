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
def count_vowels(word):
    vowels = "aeiou"
    count = 0
    word = word.lower()
    for char in word:
        if char in vowels:
            count += 1
    return count


def reverse_string(sentence):
    reversed_sentence = ""
    word = ""
    i = len(sentence) - 1
    while i >= 0:
        if sentence[i] == " ":
            reversed_sentence += word[::-1] + " "
            word = ""
        else:
            word += sentence[i]
        i -= 1
    reversed_sentence += word[::-1]
    return reversed_sentence


def main():
    sentence_input = input("Enter a sentence: ")
    vowels_count = count_vowels(sentence_input)
    print(f"The number of vowels in '{sentence_input }' is: {vowels_count}")
    reversed_sentence = reverse_string(sentence_input)
    print(f"The reversed sentence is: {reversed_sentence}")


main()
