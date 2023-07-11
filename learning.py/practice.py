first = input("Enter first numbar :")
second = input("Enter second number :")
operator = input("choose your opretor : +, -, *, /, %, // ,** :")

first = int(first)
second = int(second)

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
elif operator == "//":
    print(first // second)
elif operator == "**":
    print(first ** second)
else :
    print("invalid operation")

print("thank you")
print("this calculator created :alok")
