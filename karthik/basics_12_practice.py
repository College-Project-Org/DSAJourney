import math


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def largest_num(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c


def age_category(age):
    if age < 0:
        return "Invalid age"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 60:
        return "Adult"
    else:
        return "Senior"


def character_type(ch):
    ch_low = ch.lower()

    if ch_low in {"a", "e", "i", "o", "u"}:
        return "Vowel"
    elif ch.isdigit():
        return "Digit"
    elif ch_low.isalpha():
        return "Consonant"
    else:
        return "Special Character"


if __name__ == "__main__":
    year = int(input("Enter a Year: "))
    print(f"{year} is {'a leap year' if is_leap_year(year) else 'not a leap year'}")

    num = int(input("Enter a number: "))
    print(f"{num} is {'prime' if is_prime(num) else 'not prime'}")

    a = int(input("1st Number: "))
    b = int(input("2nd Number: "))
    c = int(input("3rd Number: "))
    print("Largest number is:", largest_num(a, b, c))

    age = int(input("Enter age: "))
    print(age_category(age))

    ch = input("Enter a character: ")
    print(character_type(ch))
