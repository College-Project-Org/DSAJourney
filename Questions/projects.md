

# Mini-Project 1 — CLI To-Do List Manager

Students build a **command-line task manager**.

Features:

* add task
* remove task
* mark task complete
* view all tasks
* save tasks in a list

Example interaction

```
1. Add task
2. View tasks
3. Remove task
4. Mark complete
5. Exit
```

Concepts practiced

* lists
* loops
* conditionals
* functions

Stretch goal
Store tasks in **dictionary with status**.

```
{
 "task1": "done",
 "task2": "pending"
}
```

---

# Mini-Project 2 — Student Grade Manager

Build a system to store **student marks and calculate results**.

Example data

```
{
 "Akash": [80,90,75],
 "Rahul": [60,70,65]
}
```

Features

* add student
* add marks
* calculate average
* find topper
* display all results

Concepts

* dictionaries
* loops
* aggregation

---

# Mini-Project 3 — Word Frequency Analyzer

Input a paragraph and compute **word statistics**.

Example

```
text = "python is great and python is powerful"
```

Output

```
python → 2
is → 2
great → 1
and → 1
powerful → 1
```

Extensions

* ignore punctuation
* case insensitive
* find **top 3 words**

Concepts

* dictionaries
* string processing
* loops

---

# Mini-Project 4 — Password Strength Checker

Program evaluates **password strength**.

Rules:

* minimum length 8
* contains uppercase
* contains digit
* contains special character

Output

```
Weak
Medium
Strong
```

Concepts

* string functions
* loops
* conditionals

Real world connection: **security basics**.

---

# Mini-Project 5 — Number Guessing Game

Program randomly selects number.

User must guess.

Example

```
Guess the number between 1 and 50
```

Program gives hints:

```
Too high
Too low
Correct
```

Concepts

* loops
* conditionals
* random module

Extensions

* track number of attempts
* difficulty levels

---

# Mini-Project 6 — Contact Book

Simple **phonebook application**.

Structure

```
{
 "John": "99999999",
 "Alice": "88888888"
}
```

Features

* add contact
* search contact
* delete contact
* update number

Concepts

* dictionaries
* input validation

Extension
Allow **multiple numbers per contact**.

---

# Mini-Project 7 — Expense Tracker

User records daily expenses.

Example

```
Food 200
Transport 100
Food 150
```

Program calculates

```
Total spent
Category wise totals
```

Output example

```
Food → 350
Transport → 100
Total → 450
```

Concepts

* dictionaries
* aggregation
* loops

Extension
Monthly report.

---

# Mini-Project 8 — List Analytics Tool

Input list of numbers and compute statistics.

Example

```
[4,8,1,9,2]
```

Program outputs

```
Min
Max
Average
Median
Second largest
```

Concepts

* lists
* sorting
* functions

Extension
Remove duplicates before analysis.

---

# Mini-Project 9 — Anagram Finder

Given a list of words, group anagrams.

Example

```
["eat","tea","tan","ate","nat","bat"]
```

Output

```
{
 "aet": ["eat","tea","ate"],
 "ant": ["tan","nat"],
 "abt": ["bat"]
}
```

Concepts

* dictionaries
* sorting
* string manipulation

Real interview pattern.

---

# Mini-Project 10 — Log File Analyzer

Students simulate **DevOps style log analysis**.

Example logs

```
INFO login
ERROR db_failed
INFO logout
ERROR timeout
INFO login
```

Program outputs

```
INFO → 3
ERROR → 2
```

Extension

* detect most frequent error
* extract timestamps
* detect suspicious activity

Concepts

* string parsing
* dictionaries
* frequency counting

---

