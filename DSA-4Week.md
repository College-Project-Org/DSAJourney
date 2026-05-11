# DSA Journey — Python Foundations to FAANG

> **Platform:** Neetcode.io + LeetCode | **Daily time:** 1.5–2 hrs
> **Path:** Python basics → Arrays → Hashing → Two Pointers → Sliding Window → Binary Search → Stack → Linked Lists → Trees

This plan starts from zero Python knowledge and builds up to solving medium DSA problems with confidence.
Every concept is introduced with a real-world analogy before any code. Every action earns XP.

---

## The Reward System

### Earning XP

| Action | XP |
|---|---|
| Learn a Python concept (Pre-Week) | +5 |
| Solve an Easy problem | +10 |
| Solve a Medium problem | +25 |
| Solve a Hard problem | +50 |
| Re-solve a problem clean on a Review Day | +15 |
| Complete every item in a single day | +10 *(Perfect Day bonus)* |
| Complete a full week | +75 |

### Levels

| XP | Level |
|---|---|
| 0 | Seed — *"You've started. That's already more than most."* |
| 50 | Apprentice |
| 150 | Coder |
| 350 | Problem Solver |
| 650 | Algorithm Ace |
| 1000 | DSA Ninja |
| 1400 | FAANG Ready |

### Weekly Badges

| Badge | Earned when |
|---|---|
| Python Hatchling | Pre-Week complete |
| Array Warrior | Week 1 complete |
| Hash Explorer | Week 2 complete |
| Binary Blade | Week 3 complete |
| Tree Whisperer | Week 4 complete |

### Special Badges

| Badge | How to earn |
|---|---|
| Ignition | Solve your very first problem |
| Speedster | Solve any Easy in under 10 minutes |
| Grinder | Complete 5 consecutive days without skipping |
| Sharpshooter | Solve a Medium without looking at hints |
| Revisor | Complete every problem on a Review Day |
| Month Master | Complete all 4 DSA weeks |

---

## How to Use This Plan

- Check off `[ ]` to `[x]` as you complete each item
- Track XP in the **Progress Dashboard** below — update it at the end of each day
- Read the analogy block *before* looking at code for every new concept
- After every problem, write the pattern name + time/space complexity in a comment at the top of your solution file
- Never skip a Review Day — spaced repetition is what makes things stick

---

## Progress Dashboard

*Update this after each week.*

| Section | XP Earned | Badges |
|---|---|---|
| Pre-Week | | |
| Week 1 | | |
| Week 2 | | |
| Week 3 | | |
| Week 4 | | |
| **Total** | | |

**My current level:** Seed

**Badges earned:** *(none yet — go earn Ignition)*

---
---

# Pre-Week — Python Foundations

> Before you can solve DSA problems you need Python to feel like a natural language.
> This pre-week covers exactly what you need — nothing more, nothing less.
> Take as many days as you need. The goal is comfort, not speed.

---

## Day P1 — Variables, Types, and I/O

### Analogy
A variable is a **labelled box**. You put a value inside, give the box a name, and Python figures out what kind of thing is inside automatically. The five types you will use in 90% of DSA problems are below.

### Concepts — +5 XP each

- [ ] Integers, floats, strings, booleans, None +5 XP
- [ ] Type casting with `int()`, `float()`, `str()` +5 XP
- [ ] Reading input with `input()` and printing with f-strings +5 XP

```python
name = "Akash"         # str  — text, always in quotes
score = 95             # int  — whole numbers
ratio = 0.75           # float — decimals
passed = True          # bool  — True or False (capital T/F)
empty = None           # NoneType — absence of a value

# input() always returns a string — cast to use as a number
age = int(input("Your age: "))
price = float(input("Price: "))

# f-strings are the cleanest output format
print(f"Hello {name}, your score is {score}/100")

# Check the type of anything
print(type(score))     # <class 'int'>
```

### Practice

- [ ] Ask for a name and year of birth, then print: `"<name> is <age> years old in 2026"` +5 XP
- [ ] Ask for two numbers. Print their sum, difference, product, and quotient on separate lines +5 XP
- [ ] Print the type of each: `42`, `"hello"`, `3.14`, `True`, `None` +5 XP

---

## Day P2 — Conditionals and Loops

### Analogy
**Conditionals** are forks in a road — your program reads the situation and picks a direction.
**Loops** are round trips — instead of writing the same code 10 times, you write it once and tell Python "do this 10 times."

### Concepts — +5 XP each

- [ ] `if / elif / else` and Python truthiness +5 XP
- [ ] `for` loop with `range()` and `enumerate()` +5 XP
- [ ] `while` loop with `break` and `continue` +5 XP

```python
# Conditionals
x = 10
if x > 5:
    print("big")
elif x == 5:
    print("exactly 5")
else:
    print("small")

# Truthiness — these all behave like False:
# 0, "", [], {}, set(), None
if []:
    print("won't print")  # empty list is falsy

# for — iterate over any sequence
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(5):           # 0, 1, 2, 3, 4
    print(i)

for i, val in enumerate(fruits):   # gives index + value together
    print(i, val)

# while — loop until condition fails
count = 0
while count < 3:
    count += 1

# break exits early; continue skips to next iteration
for n in range(10):
    if n == 5:
        break        # stops here
    if n % 2 == 0:
        continue     # skip even numbers
    print(n)         # prints 1, 3
```

### Practice

- [ ] Print all even numbers from 1 to 50 using a for loop +5 XP
- [ ] Ask the user to guess a hardcoded number (42). Keep asking until they get it right +5 XP
- [ ] Print a right-angled star triangle: row 1 has 1 star, row 5 has 5 stars +5 XP

---

## Day P3 — Functions

### Analogy
A function is a **recipe**. You write it once, then call it any time you need the dish — with different ingredients each time. Without functions you repeat code everywhere, and fixing one bug means finding every copy.

### Concepts — +5 XP each

- [ ] Defining and calling functions with `def` and `return` +5 XP
- [ ] Default arguments and multiple return values +5 XP
- [ ] Breaking a big problem into small named functions +5 XP

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Akash"))          # Hello, Akash!

# Default arguments — used when caller doesn't provide a value
def power(base, exp=2):
    return base ** exp

print(power(3))                # 9   (exp defaults to 2)
print(power(3, 3))             # 27

# Multiple return values — Python packs them as a tuple
def min_max(nums):
    return min(nums), max(nums)

low, high = min_max([4, 1, 9, 2])
print(low, high)               # 1 9

# Functions calling functions — build complexity from simplicity
def is_even(n):
    return n % 2 == 0

def count_evens(nums):
    return sum(1 for n in nums if is_even(n))
```

### Practice

- [ ] Write `is_prime(n)` — returns True if n is prime, False otherwise +5 XP
- [ ] Write `fibonacci(n)` — returns the first n Fibonacci numbers as a list +5 XP
- [ ] Write `reverse_string(s)` — returns the string reversed *without* using `[::-1]` +5 XP

---

## Day P4 — Lists

### Analogy
A list is a **row of numbered compartments** starting at index 0. You can store anything in them, access any compartment instantly by number, and cheaply add to the end. Inserting in the middle makes everything shift over — that's a cost worth knowing.

### Concepts — +5 XP each

- [ ] Indexing, slicing, and negative indices +5 XP
- [ ] Mutating: `append`, `pop`, `insert`, `sort` +5 XP
- [ ] List comprehension — Python's most useful one-liner +5 XP

```python
nums = [10, 20, 30, 40, 50]

print(nums[0])        # 10  — first element
print(nums[-1])       # 50  — last element
print(nums[1:4])      # [20, 30, 40]  — index 1 up to but not including 4
print(nums[::-1])     # [50, 40, 30, 20, 10]  — reversed copy

# Mutating
nums.append(60)       # add to end — O(1)
nums.pop()            # remove from end — O(1)
nums.insert(2, 25)    # insert at index 2 — O(n), everything after shifts
nums.pop(0)           # remove from front — O(n), everything shifts left

sorted_copy = sorted(nums)   # new sorted list, original unchanged
nums.sort()                  # sorts in-place

# Searching
print(30 in nums)            # O(n) — checks every element
print(len(nums))             # length — O(1)

# List comprehension
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
matrix  = [[0] * 3 for _ in range(3)]   # 3x3 grid of zeros
```

> **DSA cost table to memorise:**
> Index access: O(1) | Append/pop end: O(1) | Search with `in`: O(n) | Insert/delete middle: O(n)

### Practice

- [ ] Given a list of numbers, return only elements greater than the average +5 XP
- [ ] Rotate a list left by k positions without using slicing tricks +5 XP
- [ ] Flatten a 2D list into a single list using list comprehension +5 XP

---

## Day P5 — Strings

### Analogy
Strings are lists of characters — but **immutable**: you can never change a character in place. Every "modification" creates a brand new string. This matters in DSA: building a string inside a loop with `+=` creates a new object each iteration — O(n²) total. The fix: collect into a list, then `"".join()` at the end.

### Concepts — +5 XP each

- [ ] Slicing, `lower/upper`, `strip`, `split`, `join` +5 XP
- [ ] Character checking: `isalpha`, `isdigit`, `isalnum` +5 XP
- [ ] Efficient string building with `join` instead of `+=` +5 XP

```python
s = "Hello, World!"

print(s[7:12])                        # World
print(s[::-1])                        # !dlroW ,olleH
print(s.lower())                      # hello, world!
print("  hello  ".strip())            # "hello"

words = "one two three".split()       # ["one", "two", "three"]
print("-".join(words))                # "one-two-three"

print("abc".isalpha())                # True
print("123".isdigit())                # True
print("abc123".isalnum())             # True (letter OR digit)

# Efficient building — O(n) total instead of O(n²)
parts = []
for i in range(5):
    parts.append(str(i))
result = "".join(parts)               # "01234"
# Avoid: result += str(i) inside a loop
```

### Practice

- [ ] Count vowels in a string, case-insensitive +5 XP
- [ ] Check if a string is a palindrome using two-pointer logic (no `[::-1]`) +5 XP
- [ ] Title-case a sentence without using `.title()` — capitalise the first letter of each word manually +5 XP

---

## Day P6 — Dictionaries and Sets

### Analogy
**Dictionary:** a magical phone book. You say a name (key) and the book instantly opens to that entry (value). No page flipping. O(1).

**Set:** a bag where every item is unique. "Is this in the bag?" is answered instantly — O(1). With a list, you'd check every item one by one.

These two structures power more than half of all hashmap/hashset DSA problems.

### Concepts — +5 XP each

- [ ] Dictionary: create, read, update, delete, iterate +5 XP
- [ ] Frequency counter pattern with `Counter` and `defaultdict` +5 XP
- [ ] Set: add, membership check, union/intersection/difference +5 XP

```python
from collections import Counter, defaultdict

# Dictionary
book = {"Alice": "555-1234", "Bob": "555-5678"}
print(book["Alice"])                       # "555-1234"
print(book.get("Charlie", "not found"))    # safe — returns default if missing

book["Charlie"] = "555-9999"               # add or update
del book["Bob"]

for name, number in book.items():
    print(f"{name}: {number}")

# Frequency counter — the most common DSA pattern
text = "abracadabra"
freq = Counter(text)                       # {'a': 5, 'b': 2, 'r': 2, ...}
print(freq.most_common(2))                 # [('a', 5), ('b', 2)]

freq2 = defaultdict(int)                   # never raises KeyError, defaults to 0
for char in text:
    freq2[char] += 1

# Set
seen = set()
seen.add("apple")
seen.add("apple")        # ignored — already there
print("apple" in seen)   # True  — O(1)
print("mango" in seen)   # False — O(1)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a & b)    # {3, 4}          — intersection
print(a | b)    # {1, 2, 3, 4, 5, 6} — union
print(a - b)    # {1, 2}          — in a but not b
```

### Practice

- [ ] Count word frequency in a sentence and print sorted by count, most common first +5 XP
- [ ] Check if two strings are anagrams using `Counter` +5 XP
- [ ] Given two lists, find: elements only in A | elements only in B | elements in both — using sets +5 XP

---

## Day P7 — Big O + Pre-Week Challenge

### Analogy
Big O tells you **how your code scales as input grows**. You don't count every operation — you identify what changes when n doubles.

| Notation | Name | Analogy |
|---|---|---|
| O(1) | Constant | Opening locker #42 directly |
| O(log n) | Logarithmic | Guessing 1–100 with higher/lower — at most 7 guesses |
| O(n) | Linear | Reading every page of a book once |
| O(n log n) | Linearithmic | Efficiently sorting a deck of cards |
| O(n²) | Quadratic | Every student shakes hands with every other student |

```python
def get_first(lst):          # O(1) — index access, input size doesn't matter
    return lst[0]

def find_max(lst):           # O(n) — one pass through
    best = lst[0]
    for x in lst:
        if x > best:
            best = x
    return best

def has_pair_slow(lst, t):   # O(n²) — nested loops
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == t:
                return True
    return False

def has_pair_fast(lst, t):   # O(n) — hashset eliminates the inner loop
    seen = set()
    for x in lst:
        if t - x in seen:
            return True
        seen.add(x)
    return False
```

> The goal of every DSA optimisation: replace O(n²) brute force with O(n) or O(n log n) using a smarter data structure.

### Concepts — +5 XP each

- [ ] Understand O(1), O(n), O(n²) and identify them in your own code +5 XP
- [ ] Understand O(log n) — why halving is so powerful +5 XP
- [ ] Know which list operations are O(1) vs O(n) from memory +5 XP

### Pre-Week Challenge — +10 XP each

- [ ] **Word Frequency** — input a paragraph, print each unique word and its count sorted by frequency +10 XP
- [ ] **Two Sum Brute Force** — given a list and a target, find two indices whose values sum to the target. O(n²) is fine for now. +10 XP

---

**Pre-Week complete — claim your Python Hatchling badge! +50 XP**

---
---

# Week 1 — Arrays, Strings & Hashing

> **Theme:** Use hashsets to make the impossible O(n). See arrays as your canvas.
> **Goal:** Solve Easy problems in under 15 minutes. Always write brute force before optimising.

---

## Day 1 — Hashset: Trading Space for Speed

### Analogy
Checking if any name appears twice on a class list of 1,000 students.

**Brute force:** compare every name to every other name — 1,000 × 1,000 comparisons. O(n²).

**With a hashset:** as you read each name, instantly check a set of names you've already seen. Only 1,000 checks. O(n). You used extra memory (the set) and got massive speed in return.

This is the fundamental DSA trade-off — **space for time**.

### Problems

- [ ] **Contains Duplicate** (Easy) — [neetcode.io](https://neetcode.io/problems/duplicate-integer) +10 XP
  - Write brute force first (two nested loops)
  - Then optimise to one-pass with a set
  - Why can't we do better than O(n)?

- [ ] **Valid Anagram** (Easy) — [neetcode.io](https://neetcode.io/problems/is-anagram) +10 XP
  - Approach 1: `sorted(s) == sorted(t)` — O(n log n)
  - Approach 2: `Counter(s) == Counter(t)` — O(n)
  - Why is approach 2 faster?

---

## Day 2 — Hashmap: The Complement Trick

### Analogy
You want two numbers from a list that add to a target. Brute force: try every pair — O(n²).

The insight: for each number `x`, the number you need is `target - x`. If you store every number you've seen so far in a hashmap (value → index), you can check "does my complement already exist?" in O(1). You find the pair in a single pass.

Hashmaps let you *remember what you've seen* and *instantly look up what you need*.

### Problems

- [ ] **Two Sum** (Easy) — [neetcode.io](https://neetcode.io/problems/two-integer-sum) +10 XP
  - Build `{value: index}` as you iterate
  - At each step: check if `target - nums[i]` is already in the map

- [ ] **Best Time to Buy and Sell Stock** (Easy) — [neetcode.io](https://neetcode.io/problems/buy-and-sell-crypto) +10 XP
  - Track the minimum price seen so far
  - At each price: `profit = current - min_so_far`; update the answer

---

## Day 3 — Two Pointers

### Analogy
Two people stand at opposite ends of a hallway and walk toward each other. Together they cover the whole hallway in half the steps either would take alone.

Two pointers use this idea on arrays: instead of trying every pair (O(n²)), start one pointer at each end and move them inward. One pass. O(n).

> When to use: sorted array, palindrome check, looking for a pair with a sum constraint.

```python
left, right = 0, len(arr) - 1
while left < right:
    if condition_met:
        return left, right
    elif need_bigger_value:
        left += 1
    else:
        right -= 1
```

### Problems

- [ ] **Valid Palindrome** (Easy) — [neetcode.io](https://neetcode.io/problems/is-palindrome) +10 XP
  - Keep only alphanumeric chars with `isalnum()`
  - Two pointers moving inward — compare `s[left]` and `s[right]`

- [ ] **3Sum** (Medium) — [neetcode.io](https://neetcode.io/problems/three-integer-sum) +25 XP
  - Sort the array first — this is what enables two pointers
  - Fix one element with an outer loop; two pointers for the rest
  - Skip duplicate values carefully after finding each valid triple

---

## Day 4 — Sliding Window Introduction

### Analogy
You are reading a novel through a window that shows exactly 5 words at a time. As you slide the window right, one new word enters from the right and one leaves from the left. You never re-read the full book — you only update the two edges.

A sliding window applies this to subarrays and substrings: instead of recomputing the whole window from scratch, you maintain it by adding the new right element and removing the old left.

> When to use: "find the longest/shortest subarray or substring with some property."

```python
left = 0
for right in range(len(s)):
    # expand: include s[right] in the window
    while window_is_invalid:
        # shrink from the left until valid again
        left += 1
    # window [left..right] is valid — update answer
    answer = max(answer, right - left + 1)
```

### Problems

- [ ] **Longest Substring Without Repeating Characters** (Medium) — [neetcode.io](https://neetcode.io/problems/longest-substring-without-duplicates) +25 XP
  - Use a set to track characters currently in the window
  - When a duplicate enters from the right: shrink from the left until it's removed

- [ ] Revisit **Best Time to Buy and Sell Stock** — write a one-line comment explaining how it fits the sliding window pattern

---

## Day 5 — Two Pointers: Greedy Choice

### Analogy
Two walls, water between them. Area = `min(left height, right height) × distance`.

Moving the taller wall inward: distance shrinks, height can only stay or drop — area can only decrease. Moving the shorter wall inward: distance shrinks but height might improve enough to compensate. So **always move the shorter pointer**. It's the only choice with any upside.

### Problems

- [ ] **Container With Most Water** (Medium) — [neetcode.io](https://neetcode.io/problems/max-water-container) +25 XP
  - Two pointers from both ends; always move the pointer at the shorter height
  - After solving: write in a comment exactly *why* moving the taller pointer is never better

- [ ] **Trapping Rain Water** (Hard) — [neetcode.io](https://neetcode.io/problems/trapping-rain-water) +50 XP
  - Water at position i = `min(max_left[i], max_right[i]) - height[i]`
  - Build a prefix-max from the left and one from the right, then combine

---

## Day 6 — Prefix Products and Grouping

### Analogy
**No-division product:** for each position you need the product of everything *except* that element. Dividing is off-limits. The answer at position i = (product of everything left of i) × (product of everything right of i). Two passes, zero division.

**Anagram grouping:** every anagram of the same letters, when sorted, produces the same string. `"eat"`, `"tea"`, `"ate"` all sort to `"aet"`. Use that fingerprint as a hashmap key.

### Problems

- [ ] **Product of Array Except Self** (Medium) — [neetcode.io](https://neetcode.io/problems/products-of-array-discluding-self) +25 XP
  - Left pass: `left[i]` = product of all elements before index i
  - Right pass: multiply `left[i]` by the running product of elements after i

- [ ] **Group Anagrams** (Medium) — [neetcode.io](https://neetcode.io/problems/anagram-groups) +25 XP
  - Key per word: `tuple(sorted(word))`
  - `defaultdict(list)` to collect words under each key

---

## Day 7 — Week 1 Review

### Review Problems — +15 XP each (re-solve clean, no hints)

- [ ] **Two Sum** — finish in under 10 minutes +15 XP
- [ ] **3Sum** — finish in under 25 minutes +15 XP
- [ ] **Container With Most Water** — finish in under 15 minutes +15 XP
- [ ] Write on paper the pattern name + time + space complexity for every problem you solved this week +10 XP

---

**Week 1 complete — +75 XP — claim your Array Warrior badge!**

---
---

# Week 2 — Hashmaps Deep + Sliding Window Advanced

> **Theme:** Master hashmap patterns. Push through medium problems confidently.

---

## Day 8 — Bucket Sort for Top K

### Analogy
Normal sorting is O(n log n). But if you know the *range* of values — frequencies can only go from 1 to n — you build an array indexed by frequency and place items directly into their bucket. Reading from the highest bucket down gives you most-frequent first. O(n).

### Problems

- [ ] **Top K Frequent Elements** (Medium) — [neetcode.io](https://neetcode.io/problems/top-k-elements-in-list) +25 XP
  - Approach 1: sort by frequency — O(n log n)
  - Approach 2: bucket array of size n+1 indexed by frequency — O(n)

- [ ] **Encode and Decode Strings** (Medium) — [neetcode.io](https://neetcode.io/problems/string-encode-and-decode) +25 XP
  - Design a delimiter that cannot appear inside any word
  - Length-prefix encoding: `"4#word"`

---

## Day 9 — Hashset for Sequence Detection

### Analogy
You want the longest consecutive run (1, 2, 3, 4…) in an unsorted list. The O(n²) approach starts counting from every number. The insight: only start counting from numbers with **no left neighbour** (n−1 is not in the set). Those are sequence beginnings. Follow each chain. Every number is visited at most twice — O(n).

### Problems

- [ ] **Longest Consecutive Sequence** (Medium) — [neetcode.io](https://neetcode.io/problems/longest-consecutive-sequence) +25 XP
  - Put all numbers in a set
  - Only start counting from `n` where `n-1` is not in the set

- [ ] **Valid Sudoku** (Medium) — [neetcode.io](https://neetcode.io/problems/valid-sudoku) +25 XP
  - Three sets: `rows[r]`, `cols[c]`, `boxes[(r//3, c//3)]`
  - For each filled cell: if value is in any of the three sets → invalid

---

## Day 10 — Prefix Sum

### Analogy
You have a list of daily temperatures and need to answer "what was the total between day 3 and day 7?" repeatedly. Computing it each time is O(k) per query. With a prefix sum array (running totals), any range becomes one subtraction — O(1). Precompute once, answer instantly every time.

Combined with a hashmap of seen sums, you can answer "does any subarray sum to k?" in a single O(n) pass.

```
prefix[0] = 0
prefix[i] = prefix[i-1] + arr[i-1]
sum(arr[i..j]) = prefix[j+1] - prefix[i]
```

### Problems

- [ ] **Subarray Sum Equals K** (Medium) — [LeetCode 560](https://leetcode.com/problems/subarray-sum-equals-k/) +25 XP
  - Maintain `{prefix_sum: count}` starting with `{0: 1}`
  - At each index: if `curr_sum - k` is in the map, add its count to the answer

- [ ] **Range Sum Query** (Easy) — [LeetCode 303](https://leetcode.com/problems/range-sum-query-immutable/) +10 XP
  - Pure prefix sum warmup — build the array, answer queries in O(1)

---

## Day 11 — Sliding Window: Frequency Constraints

### Analogy
The window now has a requirement: it must contain all characters of a pattern string, with the right frequencies. Track `have` (characters in the window meeting their count) and `need` (how many unique characters still need to be satisfied). Expand right freely; the moment `have == need`, the window is valid — try shrinking from the left to find the smallest one.

### Problems

- [ ] **Minimum Window Substring** (Hard) — [neetcode.io](https://neetcode.io/problems/minimum-window-with-characters) +50 XP
  - `Counter(t)` is your requirement map
  - `have` increments only when a character's window count *exactly equals* its required count
  - Store `(length, left, right)` for the best window seen

- [ ] **Permutation in String** (Medium) — [neetcode.io](https://neetcode.io/problems/permutation-string) +25 XP
  - Fixed-size window (length of s1)
  - Slide one step at a time; compare window frequency to s1 frequency

---

## Day 12 — Monotonic Deque

### Analogy
You want the maximum of a sliding window that moves right every step. A monotonic deque holds candidates in decreasing order. When a new value arrives: pop from the back all values smaller than it — they can never be the maximum while the new value is in the window. Pop from the front when that index falls outside the window. The front is always the current maximum.

### Problems

- [ ] **Sliding Window Maximum** (Hard) — [neetcode.io](https://neetcode.io/problems/sliding-window-maximum) +50 XP
  - Deque stores **indices**, not values
  - Pop back when `nums[dq[-1]] <= nums[right]`
  - Pop front when `dq[0] < left` (out of window)

- [ ] Revisit **Minimum Window Substring** — re-trace the logic without looking at your solution

---

## Day 13 — Mixed Practice

### Problems

- [ ] **Maximum Product Subarray** (Medium) — [neetcode.io](https://neetcode.io/problems/maximum-product-subarray) +25 XP
  - Track both `max_prod` and `min_prod` at every step — a negative times a negative becomes the new max

- [ ] **Find Minimum in Rotated Sorted Array** (Medium) — [neetcode.io](https://neetcode.io/problems/find-minimum-in-rotated-sorted-array) +25 XP
  - First contact with the rotated array pattern — identify which half is sorted

---

## Day 14 — Week 2 Review

### Review Problems — +15 XP each

- [ ] **Longest Consecutive Sequence** — finish in under 20 minutes +15 XP
- [ ] **Minimum Window Substring** — finish in under 35 minutes +15 XP
- [ ] **Top K Frequent Elements** — use the bucket sort approach specifically +15 XP
- [ ] Rate yourself 1–5 on each pattern: Hashmap | Sliding Window | Prefix Sum. Write it down. +10 XP

---

**Week 2 complete — +75 XP — claim your Hash Explorer badge!**

---
---

# Week 3 — Binary Search & Stack

> **Theme:** Sorted-space thinking. Binary search is a mindset, not just a recipe.

---

## Day 15 — Two Pointers on Sorted Arrays

### Analogy
With a sorted array, two pointers become even more powerful. If `arr[left] + arr[right]` is too large, moving `right` left decreases it. Too small? Moving `left` right increases it. One pointer moves per step, one valid combination is ruled out. O(n) to find any pair.

### Problems

- [ ] **Two Sum II** (Medium) — [neetcode.io](https://neetcode.io/problems/two-integer-sum-ii) +25 XP
  - O(1) extra space required — no hashmap

- [ ] **4Sum** (Medium) — [LeetCode 18](https://leetcode.com/problems/4sum/) +25 XP
  - Fix two elements with nested loops; two pointers for the rest

---

## Day 16 — Binary Search Fundamentals

### Analogy
Guess a number between 1 and 1,000. Each guess with "higher/lower" cuts the remaining options in half. Worst case: 10 guesses. `log₂(1000) ≈ 10`. Binary search is that game applied to a sorted array — **halving is extraordinarily fast.**

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1      # target is in the right half
        else:
            right = mid - 1     # target is in the left half
    return -1
```

### Problems

- [ ] **Binary Search** (Easy) — [neetcode.io](https://neetcode.io/problems/binary-search) +10 XP
  - Implement from scratch, no template peeking

- [ ] **Search a 2D Matrix** (Medium) — [neetcode.io](https://neetcode.io/problems/search-2d-matrix) +25 XP
  - Treat the m×n matrix as a flat sorted array
  - `row = mid // cols`, `col = mid % cols`

---

## Day 17 — Binary Search on Rotated Arrays

### Analogy
A sorted array `[1,2,3,4,5,6,7]` rotated by 3 becomes `[4,5,6,7,1,2,3]`. It is sorted in two halves. At any midpoint, **one half is always fully sorted**. Check which: if `arr[left] <= arr[mid]`, the left half is sorted; otherwise the right is. Then check if your target falls in the sorted half — if yes, search there; if no, search the other.

### Problems

- [ ] **Search in Rotated Sorted Array** (Medium) — [neetcode.io](https://neetcode.io/problems/find-target-in-rotated-sorted-array) +25 XP

- [ ] **Find Minimum in Rotated Sorted Array** — revisit from Day 13 with fresh eyes +15 XP

---

## Day 18 — Binary Search on the Answer

### Analogy
The most powerful form: you are not searching the array — you are **searching for the answer value itself**.

Frame the problem as: "Can I achieve answer X?" That is a yes/no question. If the answer space is monotone (once you can, you can for all larger values too — or vice versa), binary search over the range of possible X. Each "can I?" check is O(n); you run it O(log(range)) times — total O(n log n).

> This unlocks "minimize the maximum" and "maximize the minimum" hard problems.

### Problems

- [ ] **Koko Eating Bananas** (Medium) — [neetcode.io](https://neetcode.io/problems/eating-bananas) +25 XP
  - Binary search on speed `k`, not on the piles
  - Range: `[1, max(piles)]`
  - "Can I?" check: `sum(ceil(pile/k) for pile in piles) <= h`

- [ ] **Find Minimum in Rotated Array II** (Hard) — [LeetCode 154](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/) +50 XP
  - Has duplicates — the edge case that breaks the naive approach

---

## Day 19 — Stack Introduction

### Analogy
A stack of plates: you can only add (push) or remove (pop) from the top. **Last In, First Out (LIFO).** Perfect for "most recent state" problems: undo operations, matching brackets (the most recently opened bracket must close first), backtracking.

```python
stack = []
stack.append(x)     # push — O(1)
stack.pop()         # remove top — O(1)
stack[-1]           # peek at top — O(1)
if not stack:       # check empty before popping
    ...
```

### Problems

- [ ] **Valid Parentheses** (Easy) — [neetcode.io](https://neetcode.io/problems/validate-parentheses) +10 XP
  - Push opening brackets; on closing bracket, check if top of stack is the matching opener

- [ ] **Min Stack** (Medium) — [neetcode.io](https://neetcode.io/problems/minimum-stack) +25 XP
  - Store `(value, current_minimum)` at each push — retrieve the minimum in O(1)

---

## Day 20 — Monotonic Stack

### Analogy
A monotonic stack maintains a strict order — say, always decreasing from bottom to top. When a new element arrives and breaks the order, pop until order is restored. The key insight: **at the moment you pop an element, you have found the "next greater element" for it**. This answers "for each element, what comes next that is larger?" in one O(n) pass.

### Problems

- [ ] **Daily Temperatures** (Medium) — [neetcode.io](https://neetcode.io/problems/daily-temperatures) +25 XP
  - Monotonic decreasing stack of indices
  - When a warmer day arrives: pop and record the wait days

- [ ] **Car Fleet** (Medium) — [neetcode.io](https://neetcode.io/problems/car-fleet) +25 XP
  - Sort by position descending; compute each car's arrival time at the target
  - If a car behind arrives no later than the car ahead → same fleet

---

## Day 21 — Week 3 Review

### Review Problems — +15 XP each

- [ ] **Binary Search** — implement from memory in under 5 minutes +15 XP
- [ ] **Search in Rotated Sorted Array** — finish in under 20 minutes +15 XP
- [ ] **Koko Eating Bananas** — finish in under 20 minutes +15 XP
- [ ] **Valid Parentheses** — finish in under 5 minutes +15 XP
- [ ] Write "binary search on the answer space" in your own words with an example you invented +10 XP

---

**Week 3 complete — +75 XP — claim your Binary Blade badge!**

---
---

# Week 4 — Linked Lists & Trees

> **Theme:** Pointer manipulation and recursive thinking.
> These patterns are the foundation for graphs and dynamic programming later.

---

## Day 22 — Linked List Basics

### Analogy
A linked list is a treasure hunt. Each clue (node) has a value and tells you where the next clue is. You cannot skip to clue #5 — you follow the chain from #1. But inserting a new clue anywhere? Just update two pointers. No shifting like an array.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

curr = head
while curr:
    print(curr.val)
    curr = curr.next
```

### Problems

- [ ] **Reverse Linked List** (Easy) — [neetcode.io](https://neetcode.io/problems/reverse-a-linked-list) +10 XP
  - Iterative: three pointers — `prev = None`, `curr = head`, save `nxt` before overwriting
  - After iterative works, write the recursive version too

- [ ] **Merge Two Sorted Lists** (Easy) — [neetcode.io](https://neetcode.io/problems/merge-two-sorted-linked-lists) +10 XP
  - Dummy node trick: `dummy = ListNode(0)` — avoids special-casing which list provides the head

---

## Day 23 — Fast and Slow Pointers

### Analogy
Two runners on a circular track: one takes 2 steps per turn, one takes 1. If there is a loop, the fast runner eventually laps the slow one — they meet. No loop? The fast runner hits the end.

For finding the middle: when the fast pointer reaches the end, the slow pointer is exactly at the midpoint.

### Problems

- [ ] **Linked List Cycle** (Easy) — [neetcode.io](https://neetcode.io/problems/linked-list-cycle-detection) +10 XP
  - `fast = fast.next.next`, `slow = slow.next` — meeting means a cycle exists

- [ ] **Remove Nth Node From End** (Medium) — [neetcode.io](https://neetcode.io/problems/remove-node-from-end-of-linked-list) +25 XP
  - Advance the front pointer n steps ahead; then move both until front hits the end — back is at the target

---

## Day 24 — Composite List Problems

### Analogy
**Reorder List** looks hard until you see it as three sub-problems you have already solved: find the middle (slow/fast), reverse the second half, interleave the two halves. Hard problems are often just combinations of simple ones stacked together.

**LRU Cache** combines a hashmap (O(1) key lookup) with a doubly linked list (O(1) move-to-front). Either data structure alone cannot do both operations in O(1) — together they can.

### Problems

- [ ] **Reorder List** (Medium) — [neetcode.io](https://neetcode.io/problems/reorder-linked-list) +25 XP

- [ ] **LRU Cache** (Medium) — [neetcode.io](https://neetcode.io/problems/lru-cache) +25 XP
  - Read the design first, then implement. `OrderedDict` is allowed as a shortcut.

---

## Day 25 — Binary Tree Basics

### Analogy
Your family tree — but each person has at most 2 children: left and right. **Recursion** is the natural language of trees: "do something at this node, then do the same at the left child, then the right child." The call stack handles the rest automatically.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(node):    # left → root → right (gives sorted order for BST)
    if not node:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)
```

### Problems

- [ ] **Invert Binary Tree** (Easy) — [neetcode.io](https://neetcode.io/problems/invert-a-binary-tree) +10 XP
  - `node.left, node.right = node.right, node.left`; recurse on both children

- [ ] **Maximum Depth of Binary Tree** (Easy) — [neetcode.io](https://neetcode.io/problems/depth-of-binary-tree) +10 XP
  - `return 1 + max(depth(node.left), depth(node.right))`

---

## Day 26 — Tree: Diameter and Level Order

### Analogy
**Diameter:** the longest path between any two nodes. At each node, the longest path *through that node* = left subtree height + right subtree height. You compute height bottom-up and update the global answer at each node. The longest path may not pass through the root — that is the key insight.

**Level order (BFS):** use a queue. Snapshot the queue size at the start of each level — process exactly that many nodes, then move to the next level.

### Problems

- [ ] **Diameter of Binary Tree** (Easy) — [neetcode.io](https://neetcode.io/problems/binary-tree-diameter) +10 XP
- [ ] **Balanced Binary Tree** (Easy) — [neetcode.io](https://neetcode.io/problems/balanced-binary-tree) +10 XP
  - Return `−1` from the recursive call to signal an unbalanced subtree — avoids recomputing

- [ ] **Level Order Traversal** (Medium) — [neetcode.io](https://neetcode.io/problems/level-order-traversal-of-binary-tree) +25 XP
  - `from collections import deque`; snapshot `level_size = len(q)` before each level loop

---

## Day 27 — Binary Search Tree

### Analogy
A BST has one rule: everything in the left subtree is smaller than the node; everything right is larger. Searching: at each node, go left if smaller, right if larger — you eliminate half the remaining tree each step. O(log n) average. Inorder traversal of a BST always yields values in sorted ascending order.

### Problems

- [ ] **Validate Binary Search Tree** (Medium) — [neetcode.io](https://neetcode.io/problems/valid-binary-search-tree) +25 XP
  - Pass `(node, min_allowed, max_allowed)` down the recursion
  - At each node: `min_allowed < node.val < max_allowed`

- [ ] **Kth Smallest Element in BST** (Medium) — [neetcode.io](https://neetcode.io/problems/kth-smallest-integer-in-bst) +25 XP
  - Inorder traversal gives sorted order — pick the k-th element

---

## Day 28 — Final Review + Mock Session

### Review Problems — +15 XP each

- [ ] **Reverse Linked List** — finish in under 5 minutes +15 XP
- [ ] **Reorder List** — finish in under 25 minutes +15 XP
- [ ] **Maximum Depth of Binary Tree** — finish in under 5 minutes +15 XP
- [ ] **Validate BST** — finish in under 20 minutes +15 XP

### Mock Interview Simulation — +25 XP

- [ ] Pick 2 medium problems from this plan at random +25 XP
  - Set a 35-minute timer
  - Solve out loud — explain your thinking as you go
  - After time is up: note what you couldn't finish and add it to a revision list

---

**Week 4 complete — +75 XP — claim your Tree Whisperer badge!**

**All 4 weeks done — claim your Month Master badge!**

---
---

## Pattern Summary

| Pattern | Introduced | Core insight |
|---|---|---|
| Hashset | Week 1 | Trade O(n) search for O(1) by storing seen values |
| Hashmap complement | Week 1 | Store what you've seen; look up what you need |
| Two Pointers | Week 1, 3 | Sorted array → eliminate pairs in one pass |
| Sliding Window | Week 1, 2 | Maintain a valid window; update only the edges |
| Prefix Sum | Week 2 | Precompute totals; answer any range query in O(1) |
| Bucket Sort | Week 2 | When value range is known, sort in O(n) |
| Monotonic Deque | Week 2 | Track window max/min without rescanning |
| Binary Search | Week 3 | Halve the search space each step |
| Binary Search on Answer | Week 3 | "Can I achieve X?" → binary search over X |
| Stack (LIFO) | Week 3 | Most-recent state; bracket matching; backtracking |
| Monotonic Stack | Week 3 | "Next greater/smaller" for each element in O(n) |
| Linked List pointers | Week 4 | Fast/slow; dummy node; three-pointer reverse |
| Tree DFS | Week 4 | Recursion is an implicit call stack; process bottom-up for heights |
| Tree BFS | Week 4 | Level-order with deque; snapshot level size before processing |

---

## What's Next After Week 4

- [ ] Graphs — BFS/DFS on grids, connected components, topological sort
- [ ] Dynamic Programming — 1D → 2D → interval DP
- [ ] Heaps / Priority Queues
- [ ] Backtracking
- [ ] Tries

---

*Started: __________ | Target finish: __________*
