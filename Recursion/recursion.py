def factorial(n):
    assert 0 <= n == int(n), "The number must be positive integer only. :)"
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def fibinaci(n):
    assert 0 <= n == int(n), "The number should be positive integer only"
    if n in [0, 1]:
        return n
    else:
        return fibinaci(n-1) + fibinaci(n-2)


def power_of_number(number, power):
    assert number > 0 and 0 <= power == int(power)
    if power == 0:
        return 1
    else:
        return number * power_of_number(number, (power-1))


def sum_of_digits(number):
    assert number > 0 and isinstance(number, int), "The Number should be positive integer only."
    if len(str(number)) == 1:
        return number
    else:
        return number % 10 + sum_of_digits(int(number/10))


def gcd_of_two_numbers(num1, num2):
    assert isinstance(num1, int) and isinstance(num2, int), "The two numbers should be integers only."
    num1, num2 = abs(num1), abs(num2)
    if num1 % num2 == 0:
        return num2
    else:
        return gcd_of_two_numbers(num2, num1 % num2)


def decimal_to_binary(number):
    # assert 0 <= number == int(number)
    if number == 0:
        return 0
    else:
        return number % 2 + 10 * decimal_to_binary(int(number/2))


def reverse(strng):
    if len(strng) == 1:
        return strng
    else:
        return strng[-1] + reverse(strng[:-1])


series = []
def flatten(arr):
    if isinstance(arr, int):
        return series.append(arr)
    else:
        if isinstance(arr[0], int):
            series.append(arr[0])
        else:
            flatten(arr[0])
        if len(arr) >= 2:
            flatten(arr[1:])


print("Factorial: ", factorial(6))
print("Fibinacci: ", fibinaci(6))
print("Power of number: ", power_of_number(5, 0))
print("Sum of digits: ", sum_of_digits(11111))
print("GCD of two numbers", gcd_of_two_numbers(-4, 18))
print("Decimal to binary", decimal_to_binary(15))
# --------------------------------
flatten([1, 2, 3, [4, 5, [6, 7]]])
print(series)
# --------------------------------   
print(reverse("python"))