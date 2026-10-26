# Exercise Sheet 1 - Worked solutions

Run all cells from top to bottom in a fresh Python kernel. Uses basic Python 3 syntax. NumPy is needed for the array example. Use a NumPy and Jupyter installation compatible with your Python version. If NumPy is missing, install it in that environment before running these cells. Question 12 creates calculator.py and triangle.py inside a local `sheet-01-files` folder. The companion `object_oriented_solution.py` contains the final classes.


## Question 1 - Functions

### Question

The volume of a sphere with radius $r$ is $V=\frac{4}{3}\pi r^3$. Use $3.14159$ for $\pi$, or import `pi` from `math`.

Save the following template as `sphere_volume.py`. Complete the docstring and replace `pass` with a return statement that calculates the volume. Keep the calculation on one line.

```python
def sphere_volume(r):
    """Complete this docstring."""
    # Replace pass with a return statement.
    pass


if __name__ == "__main__":
    print("r = 0:", sphere_volume(0.0))
    print("r = 1:", sphere_volume(1.0))
```

Run `python3 sphere_volume.py` in the terminal. The main block calls your function with two test inputs and prints the results. Check that radius 0 gives 0 and radius 1 gives approximately 4.18879.

When the file is run directly, Python sets `__name__` to `"__main__"`, so the test block runs. If another file imports `sphere_volume`, the function is available but the test block is skipped.

Use a short docstring to describe the inputs and return value in this and the following questions.

### Solution


#### Function and tests

Return the volume rather than printing inside the function. The main block runs when this cell is executed, just as it would when the file is run directly. print can receive several values separated by commas; it puts a space between them and normally ends with a new line. For example, print("r = 0:", value) prints the label followed by the value.


```python
from math import pi

def sphere_volume(r):
    """Return the volume of a sphere with non-negative radius r."""
    return (4 / 3) * pi * r**3

if __name__ == "__main__":
    print("r = 0:", sphere_volume(0.0))
    print("r = 1:", sphere_volume(1.0))

print("Expected: 0.0 and approximately 4.18879")
```

```text
r = 0: 0.0
r = 1: 4.1887902047863905
Expected: 0.0 and approximately 4.18879
```

Save this definition and main block as sphere_volume.py to run it from the terminal. Importing that file defines the function but skips the main block.


## Question 2 - Summary statistics

### Question

Write a function `summary_statistics(L)` that accepts a non-empty list of numbers and returns the minimum, maximum, and average (in that order). Can you implement this function in a single line?

Test your function on `[1, 2, 3, 4]`, `[-3, -1, 2, 6]`, and `[5]`. Work out the expected results by hand, then compare them with the returned values. Include these tests in an `if __name__ == "__main__":` block.

### Solution


#### Printing values

The simplest approach is to pass labels and values to print, separated by commas. To control their placement within a sentence, use a string followed by .format(...). The placeholders {0}, {1} and {2} are replaced by the first, second and third arguments to .format, respectively. The numbering starts at zero. Formatting changes how values are displayed; it does not change their stored values.


```python
print("Minimum:", 1, "Maximum:", 4, "Mean:", 2.5)
print("Minimum: {0}; maximum: {1}; mean: {2}".format(1, 4, 2.5))
```

```text
Minimum: 1 Maximum: 4 Mean: 2.5
Minimum: 1; maximum: 4; mean: 2.5
```

The solution below uses the same idea to display the input list, the returned tuple and the expected tuple on one line.


#### Function and example checks

The three expressions form a tuple. The input must be non-empty, as specified in the question. The function body is one line.


```python
def summary_statistics(L):
    """Return the minimum, maximum and mean of a non-empty list."""
    return min(L), max(L), sum(L) / len(L)

if __name__ == "__main__":
    examples = [([1, 2, 3, 4], (1, 4, 2.5)),
                ([-3, -1, 2, 6], (-3, 6, 1.0)),
                ([5], (5, 5, 5.0))]
    for values, expected in examples:
        result = summary_statistics(values)
        print('{0} -> {1}; expected {2}'.format(values, result, expected))
```

```text
[1, 2, 3, 4] -> (1, 4, 2.5); expected (1, 4, 2.5)
[-3, -1, 2, 6] -> (-3, 6, 1.0); expected (-3, 6, 1.0)
[5] -> (5, 5, 5.0); expected (5, 5, 5.0)
```

## Question 3 - FizzBuzz

### Question

Write a list of the integers from 1 to 100 (inclusive) in which any number divisible by
three is replaced by the word “fizz” and any divisible by five by the
word “buzz”. Numbers divisible by both become “fizz buzz”. Can you
create a numpy array containing this list?

### Solution


#### List

Test divisibility by both 3 and 5 first; otherwise a multiple of 15 would be classified as only fizz or buzz.


```python
fizz_buzz = []
for n in range(1, 101):
    if n % 15 == 0:
        fizz_buzz.append("fizz buzz")
    elif n % 3 == 0:
        fizz_buzz.append("fizz")
    elif n % 5 == 0:
        fizz_buzz.append("buzz")
    else:
        fizz_buzz.append(n)
print("First 15 entries:", fizz_buzz[:15])
print("Total entries:", len(fizz_buzz))

print("Expected: 100 entries; entry 15 is fizz buzz")
```

```text
First 15 entries: [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizz buzz']
Total entries: 100
Expected: 100 entries; entry 15 is fizz buzz
```

#### NumPy array

NumPy can create an array from the list. Its default conversion makes all entries strings. Use dtype=object to preserve the mixture of integers and strings.


```python
import numpy as np
text_array = np.array(fizz_buzz)
mixed_array = np.array(fizz_buzz, dtype=object)
print("Default array:", text_array[:5])
print("Default entry type:", type(text_array[0]).__name__)
print("Object array:", mixed_array[:5])
print("Preserved types:", type(mixed_array[0]).__name__,
      type(mixed_array[2]).__name__)
```

```text
Default array: ['1' '2' 'fizz' '4' 'buzz']
Default entry type: str_
Object array: [1 2 'fizz' 4 'buzz']
Preserved types: int str
```

An object array is possible, but does not provide the usual advantages of a homogeneous numerical array. A Python list is a natural choice here.


## Question 4 - String slicing

### Question

Write two new functions manipulating strings, called `first_half()` and `backward()`.

- `first_half()` should accept a parameter and return the first half of it,
excluding the middle character if there is an odd number of characters.  (Hint:
the built-in function `len()` returns the length of the input.)

  
- The `backward()` function should accept a parameter and reverse the order of
its characters using slicing, then return the reversed string. (Hint: The `step`
parameter used in slicing can be negative.)

Use IPython/Jupyter to quickly test your syntax for each function.

### Solution


#### 1. First half

The slice stops before len(text) // 2. For an odd length, this excludes the middle character. In the printed output, {0!r} means: insert the first argument using its Python representation. For a string this includes quotes, so an empty string is visible as two quotes. {1!r} does the same for the second argument.


```python
def first_half(text):
    """Return the first half, excluding an odd middle character."""
    return text[:len(text) // 2]

for text in ["abcdef", "abcde", "x", ""]:
    print('{0!r} -> {1!r}'.format(text, first_half(text)))

print("Expected: 'abc', 'ab', '', ''")
```

```text
'abcdef' -> 'abc'
'abcde' -> 'ab'
'x' -> ''
'' -> ''
Expected: 'abc', 'ab', '', ''
```

#### 2. Reversal

A slice step of -1 visits the characters in reverse order.


```python
def backward(text):
    """Return text with its characters reversed."""
    return text[::-1]

for text in ["abcd", "level", ""]:
    print('{0!r} -> {1!r}'.format(text, backward(text)))

print("Expected: 'dcba', 'level', ''")
```

```text
'abcd' -> 'dcba'
'level' -> 'level'
'' -> ''
Expected: 'dcba', 'level', ''
```

## Question 5 - Lists

### Question

Write a function called `list_ops()`.
Define a list with the entries `"bear"`, `"ant"`, `"cat"`, and `"dog"`, in that order.
Then perform the following operations on the list:

- Append `"eagle"`.

  
- Replace the entry at index 2 with `"fox"`.

  
- Remove (or pop) the entry at index 1.

  
- Sort the list in reverse alphabetical order.

  
- Replace `"eagle"` with `"hawk"`. (Hint: the list’s `index(val)` method may be helpful.)

  
- Add the string `"hunter"` to the last entry in the list.

Return the resulting list.

Work out (on paper) what the result should be, then check that your function returns the correct list.
Consider printing the list at each step to see the intermediate results.

### Solution


#### Operations 1-6

The comments follow the six operations in the question. Sorting modifies the list in place; it does not return the sorted list.


```python
def list_ops():
    """Perform the six specified list operations and return the result."""
    animals = ["bear", "ant", "cat", "dog"]
    animals.append("eagle")                         # 1
    animals[2] = "fox"                              # 2
    animals.pop(1)                                  # 3
    animals.sort(reverse=True)                      # 4
    animals[animals.index("eagle")] = "hawk"         # 5
    animals[-1] += "hunter"                         # 6
    return animals

print(list_ops())

print("Expected: ['fox', 'hawk', 'dog', 'bearhunter']")
```

```text
['fox', 'hawk', 'dog', 'bearhunter']
Expected: ['fox', 'hawk', 'dog', 'bearhunter']
```

After reverse sorting the list is ["fox", "eagle", "dog", "bear"]. Replacing eagle with hawk does not sort it again.


## Question 6 - Comprehensions and iterators

### Question

Write one-line Python expressions for (a)–(c).

a) Construct the set $S=\{x\in\mathbb{Z}\mid 0\leq x\leq100,\ x\bmod3=1\}$.

b) Use a list comprehension to construct the pairs $(i,j)$ with $i\in\{1,2,3,4\}$ and $j\in\{5,7,9\}$.

c) Invert a dictionary whose values are unique and hashable, so that each value becomes a key and each key becomes its value.

d) What does each expression below return? If an expression returns an iterator, convert it to a list to see its values.

```python
map(lambda x: x % 3, range(5))
list(filter(lambda x: x % 2 == 0, range(5)))
```

### Solution


#### (a) Set comprehension

range(101) includes 100. Keep exactly those integers whose remainder on division by 3 is 1.


```python
S = {x for x in range(101) if x % 3 == 1}
print(sorted(S))

print("Number of elements:", len(S), "; expected: 34")
```

```text
[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70, 73, 76, 79, 82, 85, 88, 91, 94, 97, 100]
Number of elements: 34 ; expected: 34
```

Sorting is used only to display the set in a predictable order.


#### (b) Pairs

The nested comprehension visits every allowed j for each i.


```python
pairs = [(i, j) for i in (1, 2, 3, 4) for j in (5, 7, 9)]
print(pairs)

print("Number of pairs:", len(pairs), "; expected: 12")
```

```text
[(1, 5), (1, 7), (1, 9), (2, 5), (2, 7), (2, 9), (3, 5), (3, 7), (3, 9), (4, 5), (4, 7), (4, 9)]
Number of pairs: 12 ; expected: 12
```

#### (c) Dictionary inversion

Iterate over key-value pairs and swap them. Uniqueness prevents different entries from overwriting the same new key.


```python
original = {"a": 1, "b": 2, "c": 3}
inverse = {value: key for key, value in original.items()}
print(inverse)

print("Expected: {1: 'a', 2: 'b', 3: 'c'}")
```

```text
{1: 'a', 2: 'b', 3: 'c'}
Expected: {1: 'a', 2: 'b', 3: 'c'}
```

#### (d) Iterators and filtering

map returns an iterator, so convert it to a list to inspect its values. The second expression already calls list on the filter iterator.


```python
mapped = map(lambda x: x % 3, range(5))
print("map type:", type(mapped).__name__)
print("map values:", list(mapped))
filtered = list(filter(lambda x: x % 2 == 0, range(5)))
print("filter values:", filtered)
print("map after consumption:", list(mapped))
```

```text
map type: map
map values: [0, 1, 2, 0, 1]
filter values: [0, 2, 4]
map after consumption: []
```

An iterator is consumed as it is traversed. Converting the same map object a second time produces an empty list.


## Question 7 - Pig Latin

### Question

Write a function called `pig_latin()`.  Accept a parameter `word`, translate it
into Pig Latin, then return the translation.  Specifically, if `word` starts
with a vowel, add `"hay"` to the end; if `word` starts with a consonant, take
the first character of `word`, move it to the end, and add `"ay"`.  (Hint: use
the `in` operator to check if the first letter is a vowel.)

### Solution


#### Translation and tests

Move the first character with slicing. Check whether it is a vowel before choosing the suffix.


```python
def pig_latin(word):
    """Translate one word with the exercise's Pig Latin rules."""
    if not word:
        return ""
    if word[0].lower() in "aeiou":
        return word + "hay"
    return word[1:] + word[0] + "ay"
print(pig_latin("apple"))
print(pig_latin("banana"))
print(pig_latin("bob"))

print("Expected: applehay, ananabay, obbay")
```

```text
applehay
ananabay
obbay
Expected: applehay, ananabay, obbay
```

The empty-string check avoids indexing an empty string. This implements the simplified rules given in the question.


## Question 8 - Palindromes

### Question

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is $9009 = 91 \times 99.$
Write a function called `palindrome()` that finds and returns the
largest palindromic number made from the product of two 3-digit numbers.

### Solution


#### Search and result

Check every unordered pair of three-digit factors, including equal factors. Keep the largest palindrome seen so far instead of storing all candidates.


```python
def palindrome():
    """Return the largest palindrome from two three-digit factors."""
    largest = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            product = i * j
            if product > largest and str(product) == str(product)[::-1]:
                largest = product
    return largest

answer = palindrome()
print(answer, "= 913 * 993")

print("Expected: 906609")
```

```text
906609 = 913 * 993
Expected: 906609
```

Starting j at i avoids checking both (i, j) and (j, i). This still covers every possible product.


## Question 9 - Approximating pi

### Question

We can approximate $\pi$ using either random samples or a finite sum. Implement both methods and compare their errors. Assume $N$ is a positive integer.

**(a) Monte Carlo: points in a quarter-circle**

The unit circle has equation $x^2+y^2=1$, radius 1 and area $\pi$. Its part in the first quadrant lies inside the square $[0,1]\times[0,1]$. The square has area 1 and the quarter-circle has area $\pi/4$.

Choose $N$ points independently and uniformly in the square: for each point, draw $x$ and $y$ independently from $[0,1)$. A point is inside the quarter-circle when $x^2+y^2\leq1$. If $M$ of the $N$ points are inside, their fraction estimates the area ratio:

\[\frac{M}{N}\approx\frac{\pi}{4},\qquad \widehat{\pi}_{\mathrm{MC}}=4\frac{M}{N}.\]

Write `estimate_pi_mc(N)` to generate the points, count those inside the quarter-circle, and return the estimate. You may use `random.random()` or a NumPy random generator; both can draw uniform samples from $[0,1)$.

**(b) Series: add alternating terms**

The Leibniz series gives

\[\frac{\pi}{4}=1-\frac13+\frac15-\frac17+\cdots=\sum_{k=0}^{\infty}\frac{(-1)^k}{2k+1}.\]

Using only the first $N$ terms gives

\[\widehat{\pi}_{\mathrm{series}}=4\sum_{k=0}^{N-1}\frac{(-1)^k}{2k+1}.\]

The signs alternate and the denominators are the odd integers. For example, $N=3$ gives $4(1-1/3+1/5)$. Write `estimate_pi_series(N)` to return this finite-sum approximation. You may use a loop or `sum()` with a comprehension.

**(c) Compare the approximations**

For $N=100$, $1000$, and $10000$, record both estimates and their absolute errors $|\widehat{\pi}-\texttt{math.pi}|$, using `math.pi` as the reference value. Repeat the Monte Carlo calculation five times for each $N$. Do the estimates remain the same?

### Solution


#### (a) Monte Carlo

Each sampled point falls inside the quarter-circle with probability pi/4. Multiply the fraction inside by 4. The function does not reset the random seed.


```python
import random
import math

def estimate_pi_mc(N):
    """Estimate pi using N independent uniform points; assume N > 0."""
    inside = 0
    for _ in range(N):
        x, y = random.random(), random.random()
        if x*x + y*y <= 1:
            inside += 1
    return 4 * inside / N
```

#### (b) Leibniz series

Sum the first N alternating terms with odd denominators, then multiply by 4.


```python
def estimate_pi_series(N):
    """Return the N-term Leibniz approximation; assume N > 0."""
    return 4 * sum((-1)**k / (2*k + 1) for k in range(N))

print("N = 3:", estimate_pi_series(3))

print("Expected:", 4 * (1 - 1/3 + 1/5))
```

```text
N = 3: 3.466666666666667
Expected: 3.466666666666667
```

#### (c) Estimates and absolute errors

Seed once before the experiment so rerunning the notebook reproduces this table. Successive calls still draw different samples. The series is calculated once for each N because it is deterministic. Here {0:.8f} displays the first argument in fixed-point notation with eight digits after the decimal point; {1:.8f} does the same for the second. The colon introduces the display format, .8 gives the number of decimal places, and f selects fixed-point notation. This rounds the displayed text only.


```python
random.seed(587)
for N in (100, 1000, 10000):
    series = estimate_pi_series(N)
    print('N = {0}'.format(N))
    print('  Series: {0:.8f}; error {1:.8f}'.format(series, abs(series - math.pi)))
    for trial in range(1, 6):
        estimate = estimate_pi_mc(N)
        print('  MC {0}:   {1:.8f}; error {2:.8f}'.format(trial, estimate, abs(estimate - math.pi)))
    print()
```

```text
N = 100
  Series: 3.13159290; error 0.00999975
  MC 1:   3.08000000; error 0.06159265
  MC 2:   3.12000000; error 0.02159265
  MC 3:   3.00000000; error 0.14159265
  MC 4:   3.36000000; error 0.21840735
  MC 5:   3.20000000; error 0.05840735

N = 1000
  Series: 3.14059265; error 0.00100000
  MC 1:   3.14800000; error 0.00640735
  MC 2:   3.13600000; error 0.00559265
  MC 3:   3.14400000; error 0.00240735
  MC 4:   3.08400000; error 0.05759265
  MC 5:   3.15200000; error 0.01040735

N = 10000
  Series: 3.14149265; error 0.00010000
  MC 1:   3.14280000; error 0.00120735
  MC 2:   3.12320000; error 0.01839265
  MC 3:   3.12840000; error 0.01319265
  MC 4:   3.16680000; error 0.02520735
  MC 5:   3.14720000; error 0.00560735
```

The Monte Carlo estimates need not remain the same: they use different random samples. Two runs can nevertheless agree by chance, since the estimate depends only on the count inside. The series gives the same value for a fixed N.


## Question 10 - Letter frequencies

### Question

Write a function `letter_frequencies(text)` that returns a dictionary containing a counter for each of the 26 English letters, `a` through `z`. Include letters that do not occur, with count zero.

1. Start with all 26 counters set to zero. You may use the string `"abcdefghijklmnopqrstuvwxyz"` or `string.ascii_lowercase` to obtain the letters.
2. Treat uppercase and lowercase as the same letter: convert the input with `.lower()`. Ignore spaces, punctuation, digits and any characters outside `a`–`z`.
3. Loop through the converted string once and update the corresponding counter for each English letter.
4. In an `if __name__ == "__main__":` block, call your function on a string and print the 26-letter frequency table in alphabetical order. Then print the most frequent letter and its count.

If several letters share the largest count, choose the alphabetically first. If there are no English letters, print `"No letters"` instead of selecting a letter.

Test cases:

- `"Banana!"`: `a` occurs 3 times, `n` twice, and `b` once; all other counts are zero. The most frequent letter is `a`, with count 3.
- `"cab"`: all three letters occur once; choose `a` because it comes first alphabetically.
- `"123!"`: all counts are zero; print `"No letters"`.

Your function should return the counts; printing belongs in the main block.

### Solution


#### 1-3. Initialise, normalise and count

Create all 26 keys before counting. Testing membership in the dictionary ignores everything outside the English alphabet.


```python
from string import ascii_lowercase

def letter_frequencies(text):
    """Count English letters, ignoring case and other characters."""
    counts = {letter: 0 for letter in ascii_lowercase}   # 1
    for character in text.lower():                     # 2
        if character in counts:
            counts[character] += 1                     # 3
    return counts
```

#### 4. Frequency table and most frequent letter

Print in alphabetical order. The key (-count, letter) chooses the greatest count first, then the alphabetically first letter in a tie. Check for all-zero counts before selecting a letter. print(..., end="  ") finishes with two spaces instead of a new line, so the next entry stays on the same line. A bare print() starts a new line. As in Question 4, !r displays quotes around the input string.


```python
if __name__ == "__main__":
    for text in ["Banana!", "cab", "123!"]:
        counts = letter_frequencies(text)
        print('Input: {0!r}'.format(text))
        for letter in ascii_lowercase:
            print('{0}: {1}'.format(letter, counts[letter]), end="  ")
            if letter in "mtz":
                print()
        if not any(counts.values()):
            print("No letters")
        else:
            winner = min(counts, key=lambda c: (-counts[c], c))
            print('Most frequent: {0} ({1})'.format(winner, counts[winner]))
        print()
```

```text
Input: 'Banana!'
a: 3  b: 1  c: 0  d: 0  e: 0  f: 0  g: 0  h: 0  i: 0  j: 0  k: 0  l: 0  m: 0  
n: 2  o: 0  p: 0  q: 0  r: 0  s: 0  t: 0  
u: 0  v: 0  w: 0  x: 0  y: 0  z: 0  
Most frequent: a (3)

Input: 'cab'
a: 1  b: 1  c: 1  d: 0  e: 0  f: 0  g: 0  h: 0  i: 0  j: 0  k: 0  l: 0  m: 0  
n: 0  o: 0  p: 0  q: 0  r: 0  s: 0  t: 0  
u: 0  v: 0  w: 0  x: 0  y: 0  z: 0  
Most frequent: a (1)

Input: '123!'
a: 0  b: 0  c: 0  d: 0  e: 0  f: 0  g: 0  h: 0  i: 0  j: 0  k: 0  l: 0  m: 0  
n: 0  o: 0  p: 0  q: 0  r: 0  s: 0  t: 0  
u: 0  v: 0  w: 0  x: 0  y: 0  z: 0  
No letters
```

Banana! selects a with count 3; cab selects a in the tie; 123! prints No letters. Counting and displaying are kept separate.


## Question 11 - Mutable and immutable objects

### Question

Determine which types are mutable: `int`, `str`, `list`, `tuple`, and `set`.

For each type:

1. Create an object named `a`, then write `b = a`. Check `a is b`.
2. Operate on `b`: use `b += 1` for an integer, `b += "!"` for a string, `b.append(3)` for a list, `b += (1,)` for a tuple, or `b.add(3)` for a set.
3. Print `a`, `b`, and `a is b`. Did the operation change the shared object, or rebind `b` to a different object?

Assignment gives the same object a second name. Mutating it can affect both names; rebinding one name leaves the other unchanged. Use identity (`is`) as well as values to distinguish these cases.

For example:

```python
a = {1: "x", 2: "b"}
b = a
b[1] = "a"
print(a, b, a is b)
```

State which types are mutable and which are immutable.

### Solution


#### int - steps 1-3

First inspect identity, then apply the requested operation and inspect both values.


```python
a = 1
b = a
print("Before: a is b =", a is b)
b += 1
print("After: a =", a, "; b =", b, "; a is b =", a is b)
```

```text
Before: a is b = True
After: a = 1 ; b = 2 ; a is b = False
```

#### str - steps 1-3

First inspect identity, then apply the requested operation and inspect both values.


```python
a = "hi"
b = a
print("Before: a is b =", a is b)
b += "!"
print("After: a =", a, "; b =", b, "; a is b =", a is b)
```

```text
Before: a is b = True
After: a = hi ; b = hi! ; a is b = False
```

#### list - steps 1-3

First inspect identity, then apply the requested operation and inspect both values.


```python
a = [1, 2]
b = a
print("Before: a is b =", a is b)
b.append(3)
print("After: a =", a, "; b =", b, "; a is b =", a is b)
```

```text
Before: a is b = True
After: a = [1, 2, 3] ; b = [1, 2, 3] ; a is b = True
```

#### tuple - steps 1-3

First inspect identity, then apply the requested operation and inspect both values.


```python
a = (1, 2)
b = a
print("Before: a is b =", a is b)
b += (1,)
print("After: a =", a, "; b =", b, "; a is b =", a is b)
```

```text
Before: a is b = True
After: a = (1, 2) ; b = (1, 2, 1) ; a is b = False
```

#### set - steps 1-3

First inspect identity, then apply the requested operation and inspect both values.


```python
a = {1, 2}
b = a
print("Before: a is b =", a is b)
b.add(3)
print("After: a =", a, "; b =", b, "; a is b =", a is b)
```

```text
Before: a is b = True
After: a = {1, 2, 3} ; b = {1, 2, 3} ; a is b = True
```

#### Dictionary example and conclusion

The dictionary operation mutates the shared object.


```python
a = {1: "x", 2: "b"}
b = a
b[1] = "a"
print(a, b, a is b)
```

```text
{1: 'a', 2: 'b'} {1: 'a', 2: 'b'} True
```

int, str and tuple are immutable: these operations rebind b. list and set are mutable: the requested operations modify the shared object. Dictionaries are mutable too. A tuple can contain mutable objects, although the tuple itself cannot be changed.


## Question 12 - Modules

### Question

A module is a Python file whose functions and other names can be imported and reused in another file. Here you will create your own module and use it in a separate program. Save both files in the same folder.

(a) Create `calculator.py` using this template. Complete `add()` and `multiply()` so they return the sum and product of their two inputs. The import makes `sqrt` available through this module as well.

```python
# calculator.py
from math import sqrt


def add(a, b):
    # Return the sum.
    pass


def multiply(a, b):
    # Return the product.
    pass
```

Keep this file to imports and function definitions: it should not print results or call the functions when run or imported.

(b) Create a second file, `triangle.py`, using the template below. `import calculator` gives access to the module; for example, `calculator.add(2, 3)` calls its `add()` function. The dot specifies which module the function belongs to.

```python
# triangle.py
import calculator


def hypotenuse(a, b):
    # Complete using calculator.add, calculator.multiply,
    # and calculator.sqrt. Do not use +, * or ** here.
    pass


if __name__ == "__main__":
    print(hypotenuse(3.0, 4.0))
    print(hypotenuse(5.0, 12.0))
```

For positive side lengths $a$ and $b$, the hypotenuse is $c=\sqrt{a^2+b^2}$. Use only functions accessed through `calculator` to compute and return it.

(c) Run `python3 triangle.py` and check the results.

### Solution


#### (a) calculator.py

This cell writes the completed module into a local sheet-01-files folder. It contains imports and function definitions, with no demonstration calls. The triple-quoted text is the file content.


```python
import os
module_folder = "sheet-01-files"
if not os.path.isdir(module_folder):
    os.makedirs(module_folder)
calculator_source = '''
from math import sqrt

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b
'''
with open(os.path.join(module_folder, "calculator.py"), "w",
          encoding="utf-8") as source_file:
    source_file.write(calculator_source.lstrip())
print("Created sheet-01-files/calculator.py")
```

```text
Created sheet-01-files/calculator.py
```

#### (b) triangle.py

This file imports calculator and calls its three functions using the module name. Both files are saved in the same folder.


```python
triangle_source = '''
import calculator

def hypotenuse(a, b):
    """Return the hypotenuse for positive side lengths a and b."""
    return calculator.sqrt(calculator.add(
        calculator.multiply(a, a), calculator.multiply(b, b)))

if __name__ == "__main__":
    print(hypotenuse(3.0, 4.0))
    print(hypotenuse(5.0, 12.0))
'''
with open(os.path.join(module_folder, "triangle.py"), "w",
          encoding="utf-8") as source_file:
    source_file.write(triangle_source.lstrip())
print("Created sheet-01-files/triangle.py")
```

```text
Created sheet-01-files/triangle.py
```

#### (c) Run and check

Use the notebook's Python executable to run the saved triangle.py. This is equivalent to running python3 triangle.py in the folder containing the two files. The captured output already ends with a newline, so end="" avoids adding a second one. Popen starts the saved program, and communicate waits for it and collects its output. These lines let us run the two-file example from a notebook; in a terminal, simply run python3 triangle.py instead.


```python
import subprocess
import sys
process = subprocess.Popen(
    [sys.executable, "triangle.py"], cwd=module_folder,
    stdout=subprocess.PIPE, universal_newlines=True)
output, unused = process.communicate()
print(output, end="")
print("Expected: 5.0 and 13.0")
```

```text
5.0
13.0
Expected: 5.0 and 13.0
```

## Question 13 - Power sets

### Question

The power set of a set $A$, denoted $\mathcal{P}(A)$ or $2^A$, is
the set of all subsets of $A$, including the empty set $\emptyset$ and
$A$ itself.  For example, the power set of the set $A = \{a, b, c\}$ is
$2^A = \{\emptyset, \{a\}, \{b\}, \{c\}, \{a,b\}, \{a,c\}, \{b,c\},
\{a,b,c\} \}$.

Write a function that accepts an iterable $A$ and uses an `itertools`
function to compute the power set of $A$ as a list of sets (why couldn’t
it be a set of sets in Python?). (Hint: The power set of a set with
$n$ elements should have exactly $2^n$ elements.)

### Solution


#### All subsets

Generate combinations of every size and convert each combination to a set.


```python
from itertools import combinations

def power_set(iterable):
    """Return all subsets as a list of sets."""
    elements = []
    for value in iterable:
        if value not in elements:
            elements.append(value)
    return [set(subset) for r in range(len(elements) + 1)
            for subset in combinations(elements, r)]
subsets = power_set([1, 2, 3])
print(subsets)
print("Number of subsets:", len(subsets))
print("A set cannot contain mutable, unhashable sets; a list can.")
```

```text
[set(), {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]
Number of subsets: 8
A set cannot contain mutable, unhashable sets; a list can.
```

A set element must be hashable. Ordinary sets are mutable and unhashable, so a set cannot contain them. The requested list can contain sets. frozenset would be an alternative if a set-based representation were needed. Duplicate inputs are removed so the result is the power set of the distinct elements.


## Question 14 - Classes

### Question

Expand the `Backpack` class from the file
[object_oriented.py](object_oriented.py)
to match the following specifications. Complete this class before continuing with Questions 15–16.

- Modify the constructor so that it accepts three total arguments:
`name`, `color`, and
`max_size` (in that order). Make `max_size` an optional parameter with default value $5$.
Store each input as an attribute.

  
- Modify the `put()` method to check that the backpack
does not go over capacity. If there are already
`max_size` items or more, print “No Room!” and do not
add the item to the contents list.

  
- Write a new method called `dump()` that resets the
contents of the backpack to an empty list. This method should not
receive any arguments (except `self`).

  
- Documentation is especially important in classes so that the user
knows what an object’s attributes represent and how to use methods
appropriately. Update (or write) the docstrings for the
`__init__()`, `put()`, and
`dump()` methods, as well as the actual class docstring
(under `class` but before `__init__()`) to
reflect the changes from parts 1-3 of this problem.

To ensure that your class works properly, write a test function outside the `Backpack` class that instantiates and
analyzes a `Backpack` object.

```python
def test_backpack():
    testpack = Backpack("Barry", "black")       # Instantiate the object.
    if testpack.name != "Barry":                # Test an attribute.
        print("Backpack.name assigned incorrectly")
    for item in ["pencil", "pen", "paper", "computer"]:
        testpack.put(item)                      # Test a method.
    print("Contents:", testpack.contents)
    # ...
```

### Solution


#### 1-4. Completed Backpack

1: The constructor stores name, color and max_size. 2: put checks capacity before appending. 3: dump replaces contents with an empty list. 4: The class and methods have docstrings. Each instance receives its own contents list. The starter take, addition and comparison methods are retained.


```python
class Backpack:
    """A pack with an owner, colour, item capacity and independent contents."""

    def __init__(self, name, color, max_size = 5):
        """Store the owner, colour and capacity; start with no items."""
        self.name = name
        self.color = color
        self.max_size = max_size
        self.contents = []

    def put(self, item):
        """Add item if capacity permits; otherwise print No Room!."""
        if len(self.contents) >= self.max_size:
            print("No Room!")
        else:
            self.contents.append(item)

    def take(self, item):
        """Remove an existing item, as in the starter class."""
        self.contents.remove(item)

    def dump(self):
        """Reset contents to an empty list."""
        self.contents = []

    def __add__(self, other):
        """Return the total item count of two packs (starter method)."""
        return len(self.contents) + len(other.contents)

    def __lt__(self, other):
        """Compare item counts (starter method)."""
        return len(self.contents) < len(other.contents)
```

#### Tests

Check the default capacity and independent contents, then use a small capacity to exercise both successful insertion and a full backpack.


```python
def test_backpack():
    first = Backpack("Barry", "black")
    second = Backpack("Alice", "blue")
    first.put("pencil")
    print("Other backpack contents:", second.contents, "; expected: []")
    print("Owner, colour, capacity:", first.name, first.color, first.max_size)
    pack = Backpack("Barry", "black", max_size=2)
    pack.put("pencil")
    pack.put("paper")
    pack.put("computer")
    print("Contents:", pack.contents)
    print("Expected: ['pencil', 'paper']")
    pack.dump()
    print("After dump:", pack.contents, "; expected: []")

test_backpack()
```

```text
Other backpack contents: [] ; expected: []
Owner, colour, capacity: Barry black 5
No Room!
Contents: ['pencil', 'paper']
Expected: ['pencil', 'paper']
After dump: [] ; expected: []
```

## Question 15 - Inheritance

### Question

In [object_oriented.py](object_oriented.py) write a `Jetpack` class that inherits from the
`Backpack` class.

- Override the constructor so that in addition to a name, color, and
maximum size, it also accepts an amount of fuel. Change the default
value of `max_size` to $2$, and set the default value
of fuel to $10$. Store the fuel as an attribute.

  
- Add a `fly()` method that accepts an amount of fuel to
be burned and decrements the fuel attribute by that amount. If the
user tries to burn more fuel than remains, print “Not enough fuel!”
and do not decrement the fuel.

  
- Override the `dump()` method so that both the contents
and the fuel tank are emptied.

  
- Write clear, detailed docstrings for the class and each of
its methods.

### Solution


#### 1-4. Jetpack

1: super().__init__ initialises the inherited attributes, with capacity 2 by default. 2: fly burns fuel only when enough remains. 3: dump empties both contents and fuel. 4: Docstrings describe the class and methods. As in the question, fuel amounts are assumed non-negative.


```python
class Jetpack(Backpack):
    """A backpack with a fuel supply used for flying."""
    def __init__(self, name, color, max_size = 2, fuel = 10):
        """Initialise the inherited pack attributes and fuel balance."""
        super().__init__(name, color, max_size)
        self.fuel = fuel

    def fly(self, amount):
        """Burn a non-negative amount of fuel if enough remains."""
        if amount > self.fuel:
            print("Not enough fuel!")
        else:
            self.fuel -= amount

    def dump(self):
        """Empty both contents and fuel."""
        super().dump()
        self.fuel = 0
```

#### Tests

Test default values, partial and exact fuel use, an unsuccessful flight, inherited capacity, and dumping.


```python
jet = Jetpack("Barry", "silver")
print("Default capacity and fuel:", jet.max_size, jet.fuel, "; expected: 2, 10")
jet.fly(3)
print("After flying with 3 units:", jet.fuel, "; expected: 7")
jet.fly(8)
print("After unsuccessful flight:", jet.fuel, "; expected: 7")
jet.fly(7)
print("After using all remaining fuel:", jet.fuel, "; expected: 0")
jet.put("map")
jet.put("water")
jet.put("coat")
print("Contents:", jet.contents, "; expected: ['map', 'water']")
jet.dump()
print("After dump:", jet.contents, jet.fuel, "; expected: [], 0")
```

```text
Default capacity and fuel: 2 10 ; expected: 2, 10
After flying with 3 units: 7 ; expected: 7
Not enough fuel!
After unsuccessful flight: 7 ; expected: 7
After using all remaining fuel: 0 ; expected: 0
No Room!
Contents: ['map', 'water'] ; expected: ['map', 'water']
After dump: [] 0 ; expected: [], 0
```

## Question 16 - Special methods

### Question

Endow the `Backpack` class from the file [object_oriented.py](object_oriented.py) that you have been developing in the two previous questions with two additional magic
methods:

- The `__eq__()` magic method is used to determine if two
objects are equal, and is invoked by the `==` operator.
Implement the `__eq__()` magic method for the
`Backpack` class so that two `Backpack`
objects are equal if and only if they have the same name, color, and
number of contents.

  
- The `__str__()` magic method returns the string
representation of an object. This method is invoked by
`str()` and used by `print()`. Implement
the `__str__()` method in the `Backpack`
class so that printing a `Backpack` object yields the
following output (that is, construct and return the
following string).


    
Use `\t` for tabs and `\n` for newlines in the returned string.

```python
<<Owner:      <name>
Color:      <color>
Size:       <number of items in contents>
Max Size:   <max_size>
Contents:   [<item1>, <item2>, ...]>>
```


    


### Solution


#### 1. Equality; 2. String representation

Add __eq__ and __str__ inside Backpack. The complete class is repeated below so the code is executable without manually inserting methods. Equality follows the question: it compares the number of items, not their values or max_size. __str__ returns text; print displays it. In the returned string, \t inserts a tab and \n starts a new line. The placeholders {0} through {4} insert the five values passed to .format in order.


```python
class Backpack:
    """A pack with an owner, colour, item capacity and independent contents."""

    def __init__(self, name, color, max_size = 5):
        """Store the owner, colour and capacity; start with no items."""
        self.name = name
        self.color = color
        self.max_size = max_size
        self.contents = []

    def put(self, item):
        """Add item if capacity permits; otherwise print No Room!."""
        if len(self.contents) >= self.max_size:
            print("No Room!")
        else:
            self.contents.append(item)

    def take(self, item):
        """Remove an existing item, as in the starter class."""
        self.contents.remove(item)

    def dump(self):
        """Reset contents to an empty list."""
        self.contents = []

    def __add__(self, other):
        """Return the total item count of two packs (starter method)."""
        return len(self.contents) + len(other.contents)

    def __lt__(self, other):
        """Compare item counts (starter method)."""
        return len(self.contents) < len(other.contents)

    def __eq__(self, other):
        """Compare name, colour and item count, as specified."""
        if not isinstance(other, Backpack):
            return NotImplemented
        return (self.name == other.name and self.color == other.color
                and len(self.contents) == len(other.contents))

    def __str__(self):
        """Return the requested multiline description."""
        return ('<<Owner:\t{0}\nColor:\t\t{1}\nSize:\t\t{2}\nMax Size:\t{3}\nContents:\t{4}>>'.format(self.name, self.color, len(self.contents), self.max_size, self.contents))
```

#### 1. Equality checks

Different contents can still count as equal under the specified rule. Test each field used by the comparison.


```python
p = Backpack("Barry", "black")
q = Backpack("Barry", "black")
p.put("pen")
q.put("book")
print("Different items, same count:", p == q)
q.put("paper")
print("Different counts:", p == q)
different_name = Backpack("Alice", "black")
different_color = Backpack("Barry", "blue")
different_name.put("pen")
different_color.put("pen")
print("Different names, same count:", p == different_name)
print("Different colours, same count:", p == different_color)

print("Expected comparisons: True, False, False, False")
```

```text
Different items, same count: True
Different counts: False
Different names, same count: False
Different colours, same count: False
Expected comparisons: True, False, False, False
```

#### 2. Printed representation

Tabs separate labels from values, and newline characters start each new line.


```python
print(p)
```

```text
<<Owner:	Barry
Color:		black
Size:		1
Max Size:	5
Contents:	['pen']>>
```
