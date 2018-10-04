# FizzBuss Game using Python:
x = int(input("Enter a number for when the FizzBuss Game is reached: "))
for i in range(1, x+1):
    a = ""
    if i % 3 == 0:
        a = a + "Fizz"
    if i % 5 == 0:
        a = a + "Buzz"
    if a == "":
        a = i
    print (a)