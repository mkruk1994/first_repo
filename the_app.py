def fizzbuzz(i):
    if i %3 == 0:
        if i%5 == 0:
            return "FizzBuzz"
        else:
            return "Fizz"
    if i %5 == 0:
        if i%3 == 0:
            return "FizzBuzz"
        else:
            return "Buzz"
    return i