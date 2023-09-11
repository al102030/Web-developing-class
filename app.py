# =========================practice One==============================
# if 10 == "10":
#     print("a")
# elif "bag" > "apple" and "bag" > "cat":
#     print("b")
# else:
#     print("c")

# =========================practice Two==============================
# n = 10
# spaces = n-1
# for number in range(1, n, 2):
#     print((spaces)*" "+number*"*")
#     spaces -= 1


# =========================practice Three==============================
# command = ""
# while command.lower() != "exit":
#     command = input(">>>: ")
#     print("Echo", command)


# =========================practice Four==============================
def average():
    summery, counter = 0, 0
    while True:
        number = int(input("Enter your Number to Calculate New Average :"))
        if number != 0:
            summery += number
            counter += 1
            print(f"The Current Average is: {summery//counter}")
        else:
            print(f"The Last Average is: {summery//counter}")
            break


average()
