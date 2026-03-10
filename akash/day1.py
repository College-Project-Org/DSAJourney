a: float = 3.5


def add(x: int, y: float) -> float:
    """Return the sum of x and y."""
    return x + y


result = add(a, 5)
print(f"The result of addition is: {result}")


# Input a number
b = input("enter a number: ")
print("The number you entered is: ", b)

# datatypes
# int, float, str, bool, list, tuple, set, dict

# string formatting
str1 = "Hello, World! {a}".format(a=a)  # string formatting
str2 = f"""
This is a multi-line string.
It can span multiple lines {a}.
aaaa"""

str3 = """
This is to demonstrate formatting in multi-line strings.
The value of a is: {a}
and the value of result is: {result}
""".format(a=a, result=result)

print(str1)
print(str2)
print(str3)

# boolean values
while True:
    num1 = input("Enter a number: ")
    if num1.isdigit():
        print(f"You entered a valid number: {num1}")
    else:
        print("Invalid input. Please enter a valid number.")
        break

# list
my_list = [5, 4, 3, 2, 1]
print(f"Original list: {my_list}")
sorted_list = sorted(my_list)  # sorted function returns a new sorted list
# sort method sorts the list in place
print("New sorted list variable", sorted_list)  # sorted list
my_list.sort()
print("Original list after inplace sort", my_list)  # original list remains unchanged
my_list2 = ["apple", "banana", "cherry", 1, 2, 3]
print(my_list)
print(my_list2)
for i in my_list2:
    if isinstance(i, int):
        print(f"{i} is a digit")
    else:
        print(f"{i} is not a digit")

# append
# my_list = [5, 4, 3, 2, 1]
my_list = my_list + [7, 8, 9]
print(my_list[1])
for i in my_list:
    print(i)

for i in range(len(my_list)):
    print(i, my_list[i])

my_list.append(22)
print(my_list)
