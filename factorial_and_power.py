def power(number, pow):
    """
    docstring
    """
    if pow == 0:
        return 1

    else:
        return number * power(number,pow-1)


def factorial(number):
    """
    docstring
    """
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)


print("{} to the power of {} is {}".format(5,3, power(5,3)))
print("{} to the power of {} is {}".format(1,5, power(1,5)))
print("{}! is {}".format(4, factorial(4)))
print("{}! is {}".format(0, factorial(0)))