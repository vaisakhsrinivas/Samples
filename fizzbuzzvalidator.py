def is_fizzbuzz(arr) -> bool:

    if not arr:
        return True

    start = None
    for i, val in enumerate(arr):
        if isinstance(val, int):
            start = val - i
            break

    if start is None:
        return False

    for i, val in enumerate(arr):
        number = start + i
        if number % 15 == 0:
            expected = "FizzBuzz"
        elif number % 3 == 0:
            expected = "Fizz"
        elif number % 5 == 0:
            expected = "Buzz"
        else:
            expected = number
        if val != expected:
            return False
    return True


print(is_fizzbuzz([1, 2, "Fizz", 4, "Buzz"]))
print(is_fizzbuzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz"]))
print(is_fizzbuzz((["FizzBuzz", 16, 17, "Fizz", 19, "Buzz"])))
print(is_fizzbuzz((["FizzBuzz", 22, 23, "Fizz", 25, "Buzz", "FizzBuzz", 28, 29, "Fizz", "Buzz"])))