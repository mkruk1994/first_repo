print("Podaj liczbę:")
number = int(input())
if number %3 == 0:
    if number %5 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")
if number %5 == 0:
    if number %3 == 0:
        print("FizzBuzz")
    else:
        print("Buzz")
else:
    print(number)