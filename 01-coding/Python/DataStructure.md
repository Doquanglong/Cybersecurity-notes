# 📚 Data Structures — Notes & Code for LeetCode

> A personal reference for every core data structure: what it is, when to use it,
> its time/space complexity, and clean Python code I can reuse while solving
> LeetCode problems.

---

## 🎯 How to use this note

- Each data structure gets its own section with the **same layout** (see template below).
- Keep the code **copy-paste ready** — tested snippets, not pseudocode.
- Add LeetCode problems I solved with it under **Practice** so I build pattern recognition.
- Skim the **Complexity** and **When to use** parts before contests/interviews.

### 📄 Section template

```markdown
## <Data Structure Name>

**Idea:** one-line description of what it is.

**When to use:** the kind of problems it fits.

**Complexity:**
| Operation | Time | Space |
|-----------|------|-------|
| Access    |      |       |
| Search    |      |       |
| Insert    |      |       |
| Delete    |      |       |

**Code:**
​```python
# implementation / usage
​```
```

---

## 🗂️ Table of Contents

### Linear
- [x] Array / List
- [x] String
- [x] Linked List (singly / doubly)
- [x] Stack
- [x] Queue / Deque

### Hashing
- [x] Hash Map (dict)
- [x] Hash Set (set)

### Trees
- [ ] Binary Tree
- [ ] Binary Search Tree (BST)
- [ ] Heap / Priority Queue
- [ ] Trie (Prefix Tree)

### Graphs
- [ ] Graph (adjacency list / matrix)
- [ ] Union-Find (Disjoint Set)

### Advanced
- [ ] Segment Tree
- [ ] Fenwick Tree (BIT)

---

# Linear

## Array / List

**Idea:** An ordered, index-based collection of elements stored contiguously. In
Python the built-in `list` is a **dynamic array** — it resizes automatically, so
you never manage capacity yourself.

**When to use:**
- You need fast access by index (`arr[i]`).
- Order matters and you append/pop mostly at the **end**.
- Two-pointer, sliding-window, and prefix-sum patterns.

**Complexity:**
| Operation                    | Time      | Note                               |
|------------------------------|-----------|------------------------------------|
| Access `arr[i]`              | O(1)      | direct index                       |
| Update `arr[i] = x`          | O(1)      |                                    |
| Append `arr.append(x)`       | O(1)*     | amortized; occasional resize       |
| Pop end `arr.pop()`          | O(1)      |                                    |
| Insert / Pop at front/middle | O(n)      | shifts elements                    |
| Search (`x in arr`)          | O(n)      | linear scan (unsorted)             |
| Sort `arr.sort()`            | O(n log n)| Timsort, in place                  |

> Space: O(n)

**Code:**
```python
# --- Create ---
arr = [3, 1, 4, 1, 5]
zeros = [0] * 5                 # [0, 0, 0, 0, 0]
grid = [[0] * 3 for _ in range(2)]   # 2x3 matrix (avoid [[0]*3]*2 — shared rows!)

# --- Access / Update ---
first, last = arr[0], arr[-1]   # -1 = last element
arr[2] = 9

# --- Add / Remove ---
arr.append(6)        # add to end            -> O(1)
arr.pop()            # remove & return end   -> O(1)
arr.insert(0, 8)     # insert at index 0     -> O(n)
arr.pop(0)           # remove from front     -> O(n)
arr.remove(1)        # remove first value 1  -> O(n)

# --- Slice (start:stop:step) ---
sub = arr[1:4]       # index 1..3
rev = arr[::-1]      # reversed copy

# --- Iterate ---
for i, val in enumerate(arr):     # index + value
    print(i, val)

# --- Common patterns ---
total = sum(arr)
biggest = max(arr)
arr.sort()                        # ascending, in place
arr.sort(reverse=True)            # descending
squares = [x * x for x in arr]    # list comprehension
```

**Built-in methods:**
| Method       | Description                                                          |
|--------------|----------------------------------------------------------------------|
| `append()`   | Adds an element at the end of the list                               |
| `clear()`    | Removes all the elements from the list                              |
| `copy()`     | Returns a copy of the list                                          |
| `count()`    | Returns the number of elements with the specified value            |
| `extend()`   | Adds the elements of a list (or any iterable) to the end of the current list |
| `index()`    | Returns the index of the first element with the specified value     |
| `insert()`   | Adds an element at the specified position                           |
| `pop()`      | Removes the element at the specified position                       |
| `remove()`   | Removes the first item with the specified value                     |
| `reverse()`  | Reverses the order of the list                                      |
| `sort()`     | Sorts the list                                                      |

<br>

---

<br>

## String

**Idea:** An **immutable** ordered sequence of characters. "Immutable" means you
can never change a string in place — every edit creates a new string. To build a
string efficiently, collect parts in a list and `"".join()` them at the end.

**When to use:**
- Any text/character problem: parsing, palindromes, anagrams, pattern matching.
- Two-pointer and sliding-window patterns over characters.

**Complexity:**
| Operation                  | Time  | Note                                    |
|----------------------------|-------|-----------------------------------------|
| Access `s[i]`              | O(1)  | direct index                            |
| Slice `s[a:b]`            | O(k)  | k = length of slice (creates new string)|
| Concatenate `s1 + s2`      | O(n)  | builds a new string                     |
| `x in s` (substring)       | O(n·m)| search                                  |
| `"".join(list)`            | O(n)  | preferred way to build strings          |

> Space: O(n)

**Code:**
```python
# --- Create ---
s = "hello world"
s = 'single quotes work too'
s = str(123)                      # '123'  (convert to string)
s = "ab" * 3                      # 'ababab'  (repeat)

# --- Access / Slice (strings are immutable — cannot do s[0] = 'H') ---
first = s[0]            # 'h'
sub   = s[0:5]         # 'hello'
rev   = s[::-1]        # 'dlrow olleh'

# --- Build a new string (efficient) ---
chars = ['a', 'b', 'c']
word = "".join(chars)             # 'abc'

# --- Split / Join ---
parts = "a,b,c".split(",")        # ['a', 'b', 'c']
line  = " ".join(["a", "b"])      # 'a b'

# --- Case / Check ---
s.upper(); s.lower()              # 'HELLO WORLD' / 'hello world'
"abc".isalpha()                   # True
"123".isdigit()                   # True

# --- Char <-> code ---
ord('a')   # 97   (char -> int)
chr(97)    # 'a'  (int -> char)

# --- Count / Find ---
s.count("l")       # 3
s.find("world")    # 6  (-1 if not found)
s.replace("l", "L")  # new string, original unchanged
```

**Built-in methods (common):**
| Method        | Description                                                       |
|---------------|------------------------------------------------------------------|
| `split()`     | Splits the string into a list at the given separator            |
| `join()`      | Joins an iterable of strings into one string                     |
| `strip()`     | Removes leading/trailing whitespace (or given chars)            |
| `replace()`   | Returns a new string with occurrences replaced                  |
| `find()`      | Returns the index of the first match (-1 if not found)          |
| `count()`     | Returns how many times a substring appears                       |
| `upper()`     | Returns an uppercase copy                                        |
| `lower()`     | Returns a lowercase copy                                         |
| `startswith()`| Returns True if the string starts with the given prefix         |
| `endswith()`  | Returns True if the string ends with the given suffix           |
| `isdigit()`   | Returns True if all characters are digits                        |
| `isalpha()`   | Returns True if all characters are letters                       |

<br>

---

<br>

## Linked List

**Idea:** A chain of **nodes**, where each node holds a value and a pointer to the
next node (and, in a doubly linked list, also to the previous one). Elements are
**not** stored contiguously — you follow pointers to move around.

**When to use:**
- Fast insert/delete at the ends or at a known node (O(1), no shifting).
- Problems that explicitly give you a linked list (reverse, detect cycle, merge).

**Complexity:**
| Operation             | Time | Note                                  |
|-----------------------|------|---------------------------------------|
| Access by index       | O(n) | must walk from the head               |
| Search                | O(n) | linear scan                           |
| Insert/Delete at head | O(1) | just re-point                         |
| Insert/Delete at tail | O(1) | if a tail pointer is kept, else O(n)  |

> Space: O(n)

**Code:**
```python
# --- Node definition (this is what LeetCode gives you) ---
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# --- Build:  1 -> 2 -> 3 ---
head = ListNode(1, ListNode(2, ListNode(3)))

# --- Traverse ---
cur = head
while cur:
    print(cur.val)
    cur = cur.next

# --- Insert at head ---
head = ListNode(0, head)          # 0 -> 1 -> 2 -> 3

# --- Reverse a linked list (classic pattern) ---
def reverse(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next     # save next
        cur.next = prev    # flip pointer
        prev = cur         # advance prev
        cur = nxt          # advance cur
    return prev            # new head

# --- Dummy node trick (simplifies edge cases at the head) ---
dummy = ListNode(0)
tail = dummy
for v in [1, 2, 3]:
    tail.next = ListNode(v)
    tail = tail.next
result = dummy.next        # 1 -> 2 -> 3
```

<br>

---

<br>

## Stack

**Idea:** A **LIFO** (Last In, First Out) collection — the last item pushed is the
first one popped, like a stack of plates. In Python just use a `list`: `append()`
to push, `pop()` to pop.

**When to use:**
- Matching/nesting problems (valid parentheses, evaluate expressions).
- Undo history, DFS (iterative), monotonic-stack patterns.

**Complexity:**
| Operation        | Time | Note                    |
|------------------|------|-------------------------|
| Push `append()`  | O(1) | add to top (end)        |
| Pop `pop()`      | O(1) | remove from top (end)   |
| Peek `stack[-1]` | O(1) | look at top             |
| Search           | O(n) |                         |

> Space: O(n)

**Code:**
```python
# --- Create (just use a list) ---
stack = []

stack.append(1)     # push -> [1]
stack.append(2)     # push -> [1, 2]
top = stack[-1]     # peek  -> 2 (does NOT remove)
val = stack.pop()   # pop   -> 2, stack is now [1]
is_empty = not stack   # True when empty

# --- Example: valid parentheses ---
def is_valid(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for c in s:
        if c in pairs:                       # closing bracket
            if not stack or stack.pop() != pairs[c]:
                return False
        else:                                # opening bracket
            stack.append(c)
    return not stack
```

<br>

---

<br>

## Queue / Deque

**Idea:** A **FIFO** (First In, First Out) collection — the first item added is the
first removed, like a line of people. Use `collections.deque` (double-ended queue),
which supports O(1) add/remove at **both** ends. Don't use `list.pop(0)` — that's O(n).

**When to use:**
- BFS (breadth-first search) on trees/graphs.
- Sliding-window maximum (monotonic deque), scheduling/order processing.

**Complexity:**
| Operation                | Time | Note                        |
|--------------------------|------|-----------------------------|
| `append()` / `appendleft()` | O(1) | add to right / left      |
| `pop()` / `popleft()`    | O(1) | remove from right / left    |
| Access middle            | O(n) | not indexed for random access |

> Space: O(n)

**Code:**
```python
from collections import deque

# --- Create ---
q = deque()                  # empty
q = deque([1, 2, 3])         # from a list -> deque([1, 2, 3])

q.append(1)         # enqueue at right -> deque([1])
q.append(2)         #                  -> deque([1, 2])
front = q[0]        # peek front       -> 1
val = q.popleft()   # dequeue from left-> 1, q is now deque([2])

# Can also be used as a stack, or from both ends:
q.appendleft(0)     # add to front
q.pop()             # remove from right

# --- Example: BFS level-order traversal of a tree ---
def bfs(root):
    if not root:
        return []
    q = deque([root])
    order = []
    while q:
        node = q.popleft()
        order.append(node.val)
        if node.left:  q.append(node.left)
        if node.right: q.append(node.right)
    return order
```

**Built-in methods (deque):**
| Method         | Description                             |
|----------------|-----------------------------------------|
| `append()`     | Add an element to the right end         |
| `appendleft()` | Add an element to the left end          |
| `pop()`        | Remove and return the rightmost element |
| `popleft()`    | Remove and return the leftmost element  |
| `extend()`     | Add multiple elements to the right      |
| `extendleft()` | Add multiple elements to the left       |
| `rotate()`     | Rotate the deque n steps to the right   |

<br>

---

<br>

# Hashing

## Hash Map (dict)

**Idea:** A collection of **key → value** pairs with (average) O(1) lookup, insert,
and delete. Python's `dict` is the hash map. Keys must be **hashable** (immutable
types like int, str, tuple). This is the single most useful structure on LeetCode.

**When to use:**
- Counting frequencies, grouping, caching/memoization.
- "Have I seen this before?" + "where/how many?" — e.g. Two Sum, anagrams.

**Complexity:**
| Operation           | Time (avg) | Worst | Note                    |
|---------------------|------------|-------|-------------------------|
| Insert `d[k] = v`   | O(1)       | O(n)  | worst case = collisions |
| Access `d[k]`       | O(1)       | O(n)  |                         |
| Delete `del d[k]`   | O(1)       | O(n)  |                         |
| Search `k in d`     | O(1)       | O(n)  | checks keys             |

> Space: O(n)

**Code:**
```python
# --- Create ---
d = {}                       # empty dict
d = {"a": 1, "b": 2}
d = dict(a=1, b=2)           # {'a': 1, 'b': 2}
d = {x: x * x for x in range(3)}   # dict comprehension {0:0, 1:1, 2:4}

# --- Access / Update ---
d["c"] = 3                   # insert / overwrite
val = d["a"]                 # 1  (KeyError if missing)
val = d.get("z", 0)          # 0  (safe default, no error)
exists = "a" in d            # True (checks keys)
del d["b"]                   # remove key

# --- Iterate ---
for key in d:                 print(key)
for key, val in d.items():    print(key, val)
for val in d.values():        print(val)

# --- Counting pattern ---
from collections import defaultdict, Counter
count = defaultdict(int)
for ch in "banana":
    count[ch] += 1            # no KeyError; defaults to 0

freq = Counter("banana")      # Counter({'a': 3, 'n': 2, 'b': 1})
freq.most_common(1)           # [('a', 3)]

# --- Example: Two Sum ---
def two_sum(nums, target):
    seen = {}                        # value -> index
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
    return []
```

**Built-in methods (dict):**
| Method        | Description                                                    |
|---------------|---------------------------------------------------------------|
| `get()`       | Returns the value for a key, or a default if missing          |
| `keys()`      | Returns a view of all keys                                     |
| `values()`    | Returns a view of all values                                   |
| `items()`     | Returns a view of all (key, value) pairs                       |
| `pop()`       | Removes the specified key and returns its value               |
| `setdefault()`| Returns a key's value; inserts it with a default if missing    |
| `update()`    | Merges another dict/iterable of pairs into this one           |
| `clear()`     | Removes all items                                              |

<br>

---

<br>

## Hash Set (set)

**Idea:** An **unordered** collection of **unique** elements with O(1) membership
testing. Python's `set` is the hash set — like a dict with keys but no values.

**When to use:**
- Deduplication, fast "does this exist?" checks.
- Tracking visited nodes in graph/grid traversal, detecting duplicates.

**Complexity:**
| Operation          | Time (avg) | Worst | Note              |
|--------------------|------------|-------|-------------------|
| Add `s.add(x)`     | O(1)       | O(n)  |                   |
| Remove `s.remove(x)`| O(1)      | O(n)  |                   |
| Search `x in s`    | O(1)       | O(n)  | the main use case |

> Space: O(n)

**Code:**
```python
# --- Create ---
s = set()                    # empty set (NOT {} — that's a dict!)
s = {1, 2, 3}
s = set([1, 1, 2])           # {1, 2}  — duplicates removed
s = {x for x in range(3)}    # set comprehension {0, 1, 2}

# --- Add / Remove ---
s.add(4)                     # {1, 2, 3, 4}
s.discard(10)                # no error if missing
s.remove(1)                  # KeyError if missing
exists = 2 in s              # True  -> O(1)

# --- Set operations ---
a, b = {1, 2, 3}, {2, 3, 4}
a | b     # union         {1, 2, 3, 4}
a & b     # intersection  {2, 3}
a - b     # difference    {1}
a ^ b     # symmetric diff {1, 4}

# --- Example: contains duplicate ---
def has_duplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False
```

**Built-in methods (set):**
| Method           | Description                                             |
|------------------|--------------------------------------------------------|
| `add()`          | Adds an element to the set                              |
| `remove()`       | Removes an element (raises KeyError if missing)        |
| `discard()`      | Removes an element (no error if missing)               |
| `pop()`          | Removes and returns an arbitrary element               |
| `union()`        | Returns the union of sets (`|`)                        |
| `intersection()` | Returns the intersection of sets (`&`)                 |
| `difference()`   | Returns the difference of sets (`-`)                   |
| `clear()`        | Removes all elements                                   |

<br>

---
```
