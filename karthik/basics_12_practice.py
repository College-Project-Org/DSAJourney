# Conditional statements.
# 1st Question - Write a program to check **leap year**.


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


year = int(input("Enter a Year:"))

if is_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


# 2nd Question -Check if a number is **prime**.
import math


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


num = int(input("Enter a number:"))
if is_prime(num):
    print(f"{num} is prime")
else:
    print(f"{num} is not a prime")


# 3rd Question - Given three numbers, **find the largest without using `max()`**.
def largest_num(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c


a = int(input("1st Number:"))
b = int(input("2nd Number:"))
c = int(input("3rd Number:"))

print("the largest number is ", largest_num(a, b, c))


# 4th Question- Write a program that categorizes age:
# * child
# * teenager
# * adult
# * senior


def age_category(age):
    if age < 0:
        print("give correct age")
    elif age > 0 and age <= 12:
        print("child")
    elif age > 12 and age <= 19:
        print("Teenager")
    elif age > 19 and age <= 60:
        print("Adult")
    elif age > 60:
        print("Senior")


age = int(input("Enter age of a person:"))

age_category(age)

# 5th Question -5. Given a character, check if it is:

# * vowel
# * consonant
# * digit


def character_type(ch):

    ch_low = ch.lower()

    if ch_low in {"a", "e", "i", "o", "u"}:
        print(f"{ch} is Vowel")
    elif ch.isdigit():
        print(f"{ch} is digit")
    elif ch_low.isalpha():
        print(f"{ch} is a consonant")
    else:
        print(f"{ch} is a special character")


ch = input("Enter a character:")

character_type(ch)
