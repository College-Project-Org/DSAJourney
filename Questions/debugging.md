# Debugging Practice (10 Questions)

Students must answer:

1. **What is wrong?**
2. **Why is it wrong?**
3. **Fix the code**

---

# Debugging 1 — String + Integer

```python
a = input("Enter a number: ")
b = input("Enter another number: ")

print(a + b)
```

Expected:

```python
Input:
2
3

Output:
5
```

Actual output:

```python
23
```

Students must identify:

* `input()` returns **string**
* need type conversion

---

# Debugging 2 — Wrong Indentation

```python
for i in range(5):
print(i)
```

Error:

```python
IndentationError
```

Students must fix indentation.

---

# Debugging 3 — Off-by-One Error

```python
numbers = [10,20,30,40]

for i in range(len(numbers)):
    print(numbers[i+1])
```

Error:

```python
IndexError
```

Students must reason about:

* index bounds
* loop range

---

# Debugging 4 — Mutable Reference Trap

```python
a = [1,2,3]
b = a

b.append(4)

print(a)
```

Students often expect:

```python
[1,2,3]
```

Actual:

```python
[1,2,3,4]
```

Concept:

* **list reference vs copy**

---

# Debugging 5 — Function Returning None

```python
def add(a,b):
    print(a+b)

result = add(2,3)
print(result)
```

Output:

```python
5
None
```

Concept:

* `print()` vs `return`

---

# Debugging 6 — Incorrect Condition

```python
num = 10

if num > 5 and < 20:
    print("Valid")
```

Error:

```python
SyntaxError
```

Students must fix logical expression.

Correct form:

```python
if num > 5 and num < 20
```

---

# Debugging 7 — Dictionary Key Error

```python
student = {
    "name": "Akash",
    "age": 22
}

print(student["marks"])
```

Error:

```python
KeyError
```

Students must handle:

* missing key
* `.get()` method

---

# Debugging 8 — Modifying List While Iterating

```python
nums = [1,2,3,4,5]

for n in nums:
    if n % 2 == 0:
        nums.remove(n)

print(nums)
```

Expected:

```python
[1,3,5]
```

Actual unpredictable output.

Concept:

* modifying list during iteration

---

# Debugging 9 — Infinite Loop

```python
i = 1

while i <= 5:
    print(i)
```

Students must identify missing increment.

---

# Debugging 10 — Wrong Tuple Assignment

```python
a = 5
b = 10

a = b
b = a

print(a,b)
```

Expected:

```python
10 5
```

Actual:

```python
10 10
```

Students must understand **swap logic**.

---

# Pro Teaching Trick (very effective)

Give them this rule during debugging:

1. **Read error message**
2. **Locate line**
3. **Check data types**
4. **Print intermediate values**

Example:

```python
print(type(variable))
```

Most beginners skip step 3 and waste 30 minutes.

---

# Advanced Debugging Challenge (Optional)

Ask them to debug this:

```python
def find_max(arr):
    max = arr[0]

    for i in arr:
        if i > max:
            max = i

    return max

print(find_max([]))
```

# Debugging Set 2 (Questions 11–30)

Students must answer:

1. What is wrong
2. Why it happens
3. Fix it

---

# Debugging 11 — Default Mutable Argument

```python
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))
print(add_item(2))
print(add_item(3))
```

Expected:

```
[1]
[2]
[3]
```

Actual:

```
[1]
[1,2]
[1,2,3]
```

Concept: **mutable default arguments persist across calls**

---

# Debugging 12 — Wrong Loop Variable

```python
numbers = [1,2,3,4]

for i in numbers:
    print(numbers[i])
```

Error:

```
IndexError
```

Students must realize **i is value, not index**.

---

# Debugging 13 — Integer Division Mistake

```python
print(5/2)
```

Expected:

```
2
```

Actual:

```
2.5
```

Students must identify operator issue.

---

# Debugging 14 — List Multiplication Trap

```python
matrix = [[0]*3]*3
matrix[0][0] = 1

print(matrix)
```

Expected:

```
[[1,0,0],
 [0,0,0],
 [0,0,0]]
```

Actual:

```
[[1,0,0],
 [1,0,0],
 [1,0,0]]
```

Concept: **shared references**

---

# Debugging 15 — Incorrect Dictionary Iteration

```python
data = {"a":1,"b":2,"c":3}

for key,value in data:
    print(key,value)
```

Error:

```
ValueError
```

Students must identify dictionary iteration behavior.

---

# Debugging 16 — List Index Out of Range

```python
arr = [10,20,30]

for i in range(len(arr)+1):
    print(arr[i])
```

Classic **off-by-one bug**.

---

# Debugging 17 — String Immutability

```python
name = "python"

name[0] = "P"

print(name)
```

Error:

```
TypeError
```

Concept: **strings are immutable**.

---

# Debugging 18 — Using `is` Instead of `==`

```python
a = 1000
b = 1000

if a is b:
    print("Same")
```

Concept: **identity vs equality**.

---

# Debugging 19 — Wrong Return Placement

```python
def find_even(nums):
    evens = []

    for n in nums:
        if n % 2 == 0:
            evens.append(n)
            return evens
```

Bug: **function returns early**.

---

# Debugging 20 — Wrong List Initialization

```python
arr = []

for i in range(5):
    arr[i] = i*i

print(arr)
```

Error:

```
IndexError
```

Concept: **append vs assignment**.

---

# Debugging 21 — Global vs Local Variable

```python
count = 0

def increment():
    count += 1

increment()
print(count)
```

Error:

```
UnboundLocalError
```

Concept: **variable scope**.

---

# Debugging 22 — Removing Items During Iteration

```python
nums = [1,2,3,4,5]

for n in nums:
    if n % 2 == 0:
        nums.remove(n)

print(nums)
```

Bug: **skipped elements due to index shift**.

---

# Debugging 23 — Missing Base Case (Recursion)

```python
def factorial(n):
    return n * factorial(n-1)
```

Error:

```
RecursionError
```

Concept: **missing base case**.

---

# Debugging 24 — Wrong Boolean Condition

```python
age = 15

if age >= 13 or age <= 19:
    print("Teenager")
```

Logic bug.

This condition is **always true**.

---

# Debugging 25 — Dictionary Update Bug

```python
freq = {}

for char in "banana":
    freq[char] += 1

print(freq)
```

Error:

```
KeyError
```

Concept: **initialize dictionary values**.

---

# Debugging 26 — Incorrect Tuple Modification

```python
t = (1,2,3)

t.append(4)
```

Error:

```
AttributeError
```

Concept: **tuples immutable**.

---

# Debugging 27 — Incorrect Set Usage

```python
s = {1,2,3}

s[0] = 10
```

Error:

```
TypeError
```

Concept: sets **don't support indexing**.

---

# Debugging 28 — Generator Misunderstanding

```python
nums = (i for i in range(5))

print(nums)
```

Students expect:

```
0 1 2 3 4
```

Actual: generator object.

---

# Debugging 29 — Sorting Bug

```python
arr = [3,1,2]

print(arr.sort())
```

Expected:

```
[1,2,3]
```

Actual:

```
None
```

Concept: `sort()` modifies list **in-place**.

---

# Debugging 30 — Shadowing Built-in Name

```python
list = [1,2,3]

numbers = list((4,5,6))
```

Error:

```
TypeError
```

Concept: **overwriting built-ins**.
