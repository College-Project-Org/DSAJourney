

# 1. Conditionals (Quick refresher)

Conditionals control **decision flow**. Python evaluates boolean expressions and executes blocks accordingly.

Key things they usually miss:

* **Truthiness** (`if my_list:`)
* **Short-circuit logic**
* `elif` vs nested `if`

Example explanation:

```python
x = 10

if x > 5:
    print("Greater")
elif x == 5:
    print("Equal")
else:
    print("Smaller")
```

Important concept:

```python
if []:
    print("True")
else:
    print("False")
```

Empty collections are **False**.

### Questions

1. Write a program to check **leap year**.
2. Check if a number is **prime**.
3. Given three numbers, **find the largest without using `max()`**.
4. Write a program that categorizes age:

   * child
   * teenager
   * adult
   * senior
5. Given a character, check if it is:

   * vowel
   * consonant
   * digit

---

# 2. Loops (Where logic actually develops)

Focus on **iteration patterns**.

Example:

```python
for i in range(1, 6):
    print(i)
```

Key concepts:

* `range(start, stop, step)`
* nested loops
* `break`
* `continue`
* loop else (rare but useful)

### Questions

1. Print numbers **1 to 100 divisible by 3 and 5**.
2. Reverse a number.

Example input
`1234`

Output
`4321`

3. Print this pattern:

```
*
**
***
****
*****
```

4. Print this pattern:

```
1
12
123
1234
```

5. Find **factorial using loops**.

6. Find **sum of digits of a number**.

Example
`345 → 12`

7. Generate **first n Fibonacci numbers**.

---

# 3. Functions (Important for interviews)

Functions create **modular reusable code**.

Example:

```python
def square(x):
    return x * x
```

Concepts to explain:

* parameters vs arguments
* return vs print
* default parameters
* recursion (brief intro)

### Questions

1. Write a function to **check palindrome**.

Example
`madam → True`

2. Write a function to **count vowels in a string**.

3. Write a function that returns **largest element in list**.

4. Write a function to **calculate GCD of two numbers**.

5. Write a function to **flatten a nested list**.

Example

```
[1, [2,3], [4,[5]]]
→ [1,2,3,4,5]
```

6. Write a recursive function for **factorial**.

---

# 4. Lists (Most commonly asked)

Lists are **mutable ordered collections**.

Example:

```python
arr = [1,2,3,4]
```

Important concepts:

* indexing
* slicing
* list comprehension
* mutability

### Questions

1. Remove **duplicates from a list**.

Example

```
[1,2,2,3,4,4]
→ [1,2,3,4]
```

2. Find **second largest element**.

3. Rotate a list **k times**.

Example

```
[1,2,3,4,5], k=2
→ [4,5,1,2,3]
```

4. Find **intersection of two lists**.

5. Find **frequency of elements in list**.

6. Move **all zeros to end**.

Example

```
[0,1,0,3,12]
→ [1,3,12,0,0]
```

---

# 5. Tuples

Explain that tuples are **immutable lists**.

Example:

```python
t = (1,2,3)
```

Where they are useful:

* fixed data
* hashing
* dictionary keys

### Questions

1. Convert list to tuple.
2. Swap two numbers using tuple unpacking.

```python
a, b = b, a
```

3. Count occurrences of element in tuple.
4. Find **index of element**.

---

# 6. Sets (Very useful in interviews)

Sets store **unique elements**.

Example:

```python
s = {1,2,3}
```

Concepts:

* uniqueness
* set operations

### Questions

1. Remove duplicates using set.
2. Find **intersection of two sets**.
3. Find **difference of sets**.
4. Check if two lists have **common element**.
5. Find **first repeating element in list** using set.

---

# 7. Dictionaries (Most powerful Python DS)

Dictionaries store **key-value pairs**.

Example:

```python
student = {
    "name": "Akash",
    "age": 22
}
```

Important concepts:

* hashing
* key lookup O(1)

### Questions

1. Count **frequency of characters in string**.

Example

```
"banana"
→ {'b':1,'a':3,'n':2}
```

2. Find **most frequent element in list**.

3. Group words by **length**.

Example

```
["hi","hello","cat","dog"]
→ {2:["hi"],3:["cat","dog"],5:["hello"]}
```

4. Invert dictionary.

Example

```
{'a':1,'b':2}
→ {1:'a',2:'b'}
```

5. Merge two dictionaries.

---

# 8. Pythonic Thinking Questions (Important)

These separate good programmers from average ones.

### Question 1

```python
a = [1,2,3]
b = a
b.append(4)

print(a)
```

Concept: **mutable reference**

---

### Question 2

```python
a = [1,2,3]
b = a[:]
b.append(4)

print(a)
```

Concept: **copy vs reference**

---

### Question 3

```python
print([i*i for i in range(5)])
```

Concept: **list comprehension**

---

### Question 4

```python
print("".join(reversed("python")))
```

Concept: **iterables**

---

# 9. Real Interview-Type Problems

Give these in class.

1. **Two Sum problem**
2. **Find duplicate in array**
3. **Longest word in sentence**
4. **Check anagram**
5. **Remove nth element from list**
6. **Find missing number in array**

---

