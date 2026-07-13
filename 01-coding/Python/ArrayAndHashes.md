# 🗂️ Arrays & Hashing — Problem Write-ups

Solutions and notes for the **Arrays & Hashing** problems.

---

## 217. Contains Duplicate

**Problem:** Given an integer array `nums`, return `True` if any value appears
**at least twice**, and `False` if every element is distinct.

**Idea:** Walk through the array once and remember every number we've already
seen in a hash map (a `set` works too). The instant we meet a number that's
already in there, we've found a duplicate and can stop early. Hash lookups are
O(1) on average, so checking "have I seen this before?" is cheap.

**Approach (step by step):**
1. Create an empty container `seen` to track numbers we've passed.
2. Loop over each number `i` in `nums`.
3. If `i` is **not** in `seen`, record it.
4. If `i` **is** already in `seen`, a duplicate exists → return `True`.
5. If the loop finishes with no repeats → return `False`.

**Complexity:**
| | |
|-----------|-----------------------------------------------|
| **Time**  | O(n) — one pass, each lookup/insert is O(1)   |
| **Space** | O(n) — worst case we store every element      |

**My solution:**
```python
class Solution(object):
    def hasDuplicate(self, nums):
        dict = {}

        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                return True
        return False
```
✅ Correct and optimal.

**How the code works (line by line):**
1. `dict = {}` — start with an empty hash map that will hold every number we've
   already visited (the keys are the numbers; the value `1` is just a placeholder).
2. `for i in nums:` — visit each number one at a time, left to right.
3. `if i not in dict:` — a membership check on a hash map is O(1). It asks
   "have I seen this number before?"
4. `dict[i] = 1` — if it's new, store it so future iterations can find it.
5. `else: return True` — if it's already a key, we've hit a repeat → answer is
   `True`, and we stop immediately (no need to look at the rest).
6. `return False` — reached only if the loop ends without ever taking the `else`
   branch, meaning every element was unique.

**Trace with `nums = [1, 2, 3, 1]`:**

| Step | `i` | `dict` before | `i in dict`? | Action                    |
|------|-----|---------------|--------------|---------------------------|
| 1    | 1   | `{}`          | no           | add 1 → `{1}`             |
| 2    | 2   | `{1}`         | no           | add 2 → `{1, 2}`         |
| 3    | 3   | `{1, 2}`      | no           | add 3 → `{1, 2, 3}`     |
| 4    | 1   | `{1, 2, 3}`   | **yes**      | duplicate! → `return True`|

**Visual — the "seen" set fills as we scan:**

```
nums:   [ 1 ] [ 2 ] [ 3 ] [ 1 ]
           │     │     │     │
           ▼     ▼     ▼     ▼
seen:    {1}  {1,2} {1,2,3}  1 already here ✋
 new? →  new   new   new   DUPLICATE → return True
```

We never even reach the end of the array — the early exit at the second `1`
is what makes this efficient in practice.

---

## 242. Valid Anagram

**Problem:** Given two strings `s` and `t`, return `True` if `t` is an anagram of
`s` — i.e. it uses exactly the same letters the same number of times, just
reordered.

**Idea:** Two strings are anagrams only if every character appears the **same
number of times** in both. So count the letters of each string into a hash map
and compare the two counts.

**Approach (step by step):**
1. If the lengths differ, they can't be anagrams → return `False` early.
2. Count how many times each character appears in `s` (`s_character`).
3. Do the same for `t` (`t_character`).
4. For every character in `s`'s counts, check it exists in `t` **and** has the
   same count. If any mismatch → return `False`.
5. If all counts match → return `True`.

**Complexity:**
| | |
|-----------|-------------------------------------------------|
| **Time**  | O(n) — count both strings, then compare         |
| **Space** | O(k) — k = number of distinct characters        |

**My solution:**
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        if s == "":
            return True
        s_character = {}
        t_character = {}

        for char in s:
            if char not in s_character:
                s_character[char] = 1
            else:
                s_character[char] += 1

        for char in t:
            if char not in t_character:
                t_character[char] = 1
            else:
                t_character[char] += 1

        for char in s_character:
            if char not in t_character:
                return False
            if (s_character[char] != t_character[char]):
                return False
        return True
```
✅ Correct and optimal.

**How the code works (line by line):**
1. `if len(s) != len(t): return False` — different lengths can't match, quick exit.
2. `if s == "": return True` — both empty (lengths are equal here) → trivially anagrams.
3. First `for` loop — build `s_character`, a map of `letter → how many times it appears in s`.
4. Second `for` loop — build the same frequency map for `t`.
5. Final `for` loop — walk every letter in `s`'s map and confirm `t` has that letter
   with the **exact same count**. Because the lengths are equal, matching all of
   `s`'s counts guarantees `t` has no extra letters either.

**Visual — the two frequency maps must be identical:**

```
s = "anagram"        t = "nagaram"
s_character:         t_character:
  a → 3                a → 3      ✔ same
  n → 1                n → 1      ✔ same
  g → 1                g → 1      ✔ same
  r → 1                r → 1      ✔ same
  m → 1                m → 1      ✔ same
                     → every count matches → True
```

> Is there a much better solution? **No** — O(n) counting is optimal. The exact
> same idea can be written in one line with `collections.Counter`:
> `return Counter(s) == Counter(t)`. Sorting both strings (`sorted(s) == sorted(t)`)
> also works but is **slower** at O(n log n).

---

## 1. Two Sum

**Problem:** Given an array `nums` and a `target`, return the **indices** of the
two numbers that add up to `target`. Exactly one valid answer exists.

**Idea:** For each number `num`, the number we still need is `complement =
target - num`. If we've already seen that complement earlier, we're done. Store
each number's index in a hash map as we go so the "have I seen it?" check is O(1).

**Approach (step by step):**
1. Create an empty hash map `hash` mapping `value → its index`.
2. Loop through `nums` with both the index and value.
3. Compute `complement = target - num`.
4. If `complement` is already in the map → return its stored index plus the current one.
5. Otherwise store `num → index` and keep going.

**Complexity:**
| | |
|-----------|-----------------------------------------------|
| **Time**  | O(n) — single pass, O(1) lookups              |
| **Space** | O(n) — the hash map of seen numbers           |

**My solution:**
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in hash:
                return [hash[complement], index]

            hash[num] = index
```
✅ Correct and optimal.

> ℹ️ **`enumerate(nums)`** loops over the list and hands you **both the index and
> the value** on each step — `(0, nums[0])`, `(1, nums[1])`, … — so you don't have
> to keep a separate counter variable. That's why `for index, num in enumerate(nums)`
> unpacks into two variables.

**How the code works (line by line):**
1. `hash = {}` — will remember every number we've passed and where it was (`value → index`).
2. `for index, num in enumerate(nums):` — visit each number, keeping its position.
3. `complement = target - num` — the partner value that would complete the pair.
4. `if complement in hash:` — O(1) check: did an earlier number equal this complement?
   If so, return that earlier index together with the current one.
5. `hash[num] = index` — not found yet, so record this number for future steps.

**Trace with `nums = [2, 7, 11, 15]`, `target = 9`:**

| Step | `index` | `num` | `complement` | in `hash`? | `hash` after        |
|------|---------|-------|--------------|------------|---------------------|
| 1    | 0       | 2     | 7            | no         | `{2: 0}`           |
| 2    | 1       | 7     | 2            | **yes**    | → return `[0, 1]`  |

> Is there a much better solution? **No** — this is the optimal O(n) approach.
> The brute-force alternative (two nested loops checking every pair) is O(n²).

---

## 49. Group Anagrams

**Problem:** Given a list of strings, group together the ones that are anagrams
of each other. Return a list of these groups (order doesn't matter).

```
Input:  ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
```

**Idea:** Build a **signature** (key) that is identical for anagrams and different
for non-anagrams, then drop every word into a bucket named after its signature.
Here the signature is a **letter-count** — anagrams have the exact same counts, so
they produce the same key. (This is the Valid Anagram idea scaled up to many words.)

**Approach (step by step):**
1. Make a hash map `groups` mapping `signature → list of words`.
2. For each `word`, build a 26-slot count of its letters (`a`..`z`).
3. Turn that count into a `tuple` so it can be used as a dict key.
4. Append the original `word` to the bucket for that key.
5. Return all the buckets (`groups.values()`).

**Complexity:**
| | |
|-----------|---------------------------------------------------|
| **Time**  | O(n · k) — n words, k letters each (count only)   |
| **Space** | O(n · k) — every word stored in the map           |

**My solution:**
```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            count = [0] * 26              # counts for 'a'..'z'

            for char in word:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)            # lists can't be dict keys, tuples can
            groups[key].append(word)

        return list(groups.values())
```
✅ Correct and optimal.

**Functions / tricks used here:**
> ℹ️ **`defaultdict(list)`** — a dict that auto-creates an empty list `[]` the first
> time you touch a new key, so `groups[key].append(word)` works without checking
> "does this key exist yet?".
>
> ℹ️ **`ord(char)`** — gives a character's numeric code (`ord('a')`=97, `ord('e')`=101).
> Subtracting `ord('a')` maps `'a'→0, 'b'→1, … 'z'→25`, i.e. the slot in `count`.
>
> ℹ️ **`tuple(count)`** — a `list` can't be a dict key (mutable/unhashable); a `tuple`
> is immutable and hashable, so we convert the count list into a tuple to use as the key.
>
> ℹ️ **`list(groups.values())`** — `.values()` returns a live *view* (`dict_values`),
> not a real list. Wrapping in `list()` produces the actual `List[List[str]]` the
> problem requires.

**How the code works (line by line):**
1. `groups = defaultdict(list)` — the bucket map; each new key starts as `[]`.
2. `for word in strs:` — process one word at a time.
3. `count = [0] * 26` — fresh 26-zero list (one slot per letter), reset per word.
4. Inner `for char in word:` + `count[ord(char) - ord('a')] += 1` — tally each letter
   into its slot.
5. `key = tuple(count)` — freeze the count into a hashable signature.
6. `groups[key].append(word)` — file the original word into its signature's bucket.
7. `return list(groups.values())` — hand back all buckets as a real list.

**Visual — one word becomes a count fingerprint:**

```
word "eat":
letter:   a  b  c  d  e  ...  t  ...  z
index:    0  1  2  3  4  ...  19 ...  25
count:  [ 1, 0, 0, 0, 1, ..., 1, ...,  0 ]   → a=1, e=1, t=1
                                              → key (1,0,0,0,1,...,1,...,0)

"tea" and "ate" build the SAME count → SAME key → same bucket.
```

**Visual — `groups` fills up (keys shortened for readability):**

```
"eat" → (a1,e1,t1)   groups = { (a1,e1,t1): ["eat"] }
"tea" → (a1,e1,t1)   groups = { (a1,e1,t1): ["eat","tea"] }
"tan" → (a1,n1,t1)   groups = { (a1,e1,t1): ["eat","tea"], (a1,n1,t1): ["tan"] }
"ate" → (a1,e1,t1)   groups = { (a1,e1,t1): ["eat","tea","ate"], (a1,n1,t1): ["tan"] }
"nat" → (a1,n1,t1)   groups = { (a1,e1,t1): [...],            (a1,n1,t1): ["tan","nat"] }
"bat" → (a1,b1,t1)   groups = { ...,                          (a1,b1,t1): ["bat"] }

list(groups.values()) → [["eat","tea","ate"], ["tan","nat"], ["bat"]]
```

> Is there a much better solution? **No** — O(n · k) counting is optimal. An
> alternative uses a **sorted string** as the key (`"".join(sorted(word))`) with a
> plain `dict`; it's simpler to write but slightly slower at O(n · k log k) because
> of the sort.

---

## 347. Top K Frequent Elements

**Problem:** Given an integer array `nums` and an integer `k`, return the `k` most
frequent elements. The answer can be in any order.

**Idea:** Sorting by frequency would cost O(n log n), but frequency itself is
bounded — it can never be higher than `len(nums)`. That means we can use
**bucket sort**: make one bucket per possible frequency (`0` .. `len(nums)`),
drop each number into the bucket matching how many times it showed up, then
walk the buckets from highest frequency down, collecting numbers until we have
`k` of them.

**Approach (step by step):**
1. Count each number's frequency into a hash map `freq`.
2. Create `sort`, a list of `len(nums)+1` buckets, all starting as `0` (empty marker).
3. For every `(key, val)` in `freq`, drop `key` into `sort[val]` — start a new
   list `[key]` if the bucket is still `0`, otherwise `append` to the existing list.
4. Walk `sort` **backwards**, from the highest index (highest frequency) to `0`.
5. Any time a bucket isn't `0` (i.e. it has numbers in it), dump its contents
   into `ret` and subtract however many we just added from `k`.
6. Stop the moment `k` hits `0` — we've collected exactly `k` numbers.

**Complexity:**
| | |
|-----------|-----------------------------------------------------------------|
| **Time**  | O(n) — counting is O(n), bucket fill is O(n), bucket scan is O(n) |
| **Space** | O(n) — the `freq` map and the `sort` bucket array                |

**My solution:**
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            if num not in freq:
                freq[num]=1
            else:
                freq[num]+=1
        sort= [0] * (len(nums)+1)
        for key,val in freq.items():
             if sort[val]==0:
                sort[val]=[key]
             else:
                sort[val].append(key)
        ret=[]
        for i in range (len(sort)-1,-1,-1):
            if sort[i] != 0:
                ret.extend(sort[i])
                k-=len(sort[i])
                if k==0:
                    break
        return ret
```
✅ Correct and optimal.

**How the code works (line by line):**
1. `freq={}` — will hold `number → how many times it appears`.
2. First `for` loop — the usual count-with-a-dict pattern (same idea as *Contains
   Duplicate*'s `dict`).
3. `sort = [0] * (len(nums)+1)` — one bucket per possible frequency, `0` used
   as an "empty" marker. Frequency can be at most `len(nums)`, so `len(nums)+1`
   buckets is always enough.
4. Second `for` loop — is `sort[val]` still `0`? Start a fresh list `[key]`.
   Otherwise `append(key)` — several different numbers can share the same
   frequency, so each bucket is a **list**, not a single value.
5. `for i in range(len(sort)-1, -1, -1):` — scan buckets from the **highest**
   frequency down to the lowest. `len(sort)-1` (not `len(sort)`) is the last
   valid index, since indices only go `0` .. `len(nums)`.
6. `if sort[i] != 0:` — skip untouched buckets (still the int `0`). This only
   works because the comparison is against `0`, matching how the bucket array
   was initialized — comparing against `[0]` instead would break it.
7. `ret.extend(sort[i])` + `k -= len(sort[i])` — take the whole bucket at once
   and shrink the remaining count by however many numbers were just taken.
8. `if k==0: break` — stop as soon as exactly `k` numbers have been gathered.
9. `return ret` — hand back the collected numbers. **Note:** this returns `ret`
   directly, not `ret[:k]` — that matters, because `k` has been mutated down to
   `0` by this point, so slicing with the mutated `k` would wipe the result.

**Trace with `nums = [1,2,2,3,3,3]`, `k = 2`:**

`freq = {1: 1, 2: 2, 3: 3}` → `sort = [0, [1], [2], [3], 0, 0, 0]` (indices `0`–`6`)

| Step | `i` | `sort[i]` | Action                            | `ret`     | `k` |
|------|-----|-----------|------------------------------------|-----------|-----|
| 1    | 6   | `0`       | skip                                | `[]`      | 2   |
| 2    | 5   | `0`       | skip                                | `[]`      | 2   |
| 3    | 4   | `0`       | skip                                | `[]`      | 2   |
| 4    | 3   | `[3]`     | extend → `k -= 1`                   | `[3]`     | 1   |
| 5    | 2   | `[2]`     | extend → `k -= 1` → `k==0`, break   | `[3, 2]`  | 0   |

`return ret` → `[3, 2]` ✅

**Visual — buckets scanned from highest frequency to lowest:**

```
index (frequency): 0     1     2     3     4     5     6
sort:              0    [1]   [2]   [3]    0     0     0
                                     ▲
scan direction:  ◄───────────────────┴── start here (i = 6, walk down)

i=6,5,4 → empty, skip
i=3 → [3] → ret=[3], k=1
i=2 → [2] → ret=[3,2], k=0 → stop
```

> Is there a much better solution? **No** — O(n) bucket sort is optimal here,
> and it beats the common heap-based approach
> (`heapq.nlargest(k, freq, key=freq.get)`, O(n log k)) precisely because
> frequency is bounded by `len(nums)`, which a heap doesn't exploit.


## 271. Encode and Decode Strings

**Problem:** Design two functions: `encode` turns a list of strings into a single
string, and `decode` turns that single string back into the original list. The
tricky part: the strings can contain **any** characters (including spaces, digits,
and `#`), so you can't just join them with a separator.

```
["neet","code","love","you"]  --encode-->  "4#neet4#code4#love3#you"
"4#neet4#code4#love3#you"      --decode-->  ["neet","code","love","you"]
```

**Idea:** Use **length-prefixing**. Before each string, write its length followed
by a marker `#`. On decode, read the number up to the `#`, then read exactly that
many characters. Because you always know *how many* characters to grab, it doesn't
matter if the string itself contains `#` or digits — you never rely on searching
for a delimiter inside the data.

**Approach — encode:**
1. Start with an empty result string.
2. For each string, append `len(string)` + `"#"` + the string itself.

**Approach — decode:**
1. Walk the encoded string with a pointer `i`.
2. From `i`, read forward until you hit `#` — those characters are the length number.
3. Convert that to an int `num`; the actual string is the next `num` characters after the `#`.
4. Jump the pointer past that string and repeat until the end.

**Complexity:**
| | |
|-----------|--------------------------------------------------|
| **Time**  | O(n) — n = total characters across all strings   |
| **Space** | O(n) — the encoded/decoded output                |

**My solution:**
```python
class Solution:

    def encode(self, strs: List[str]) -> str:
        en = ""
        for i in strs:
            en += (str(len(i)) + "#" + i)
        print(en)
        return en

    def decode(self, s: str) -> List[str]:
        de = []
        i = 0

        while i < len(s):
            sta = i

            while s[i] != "#":
                i += 1

            num = int(s[sta:i])
            de.append(s[i+1:i+1+num])

            i = i + 1 + num

        return de
```
✅ Correct and optimal.

**How the code works (line by line) — encode:**
1. `en = ""` — the growing encoded string.
2. `for i in strs:` — for each original string `i`.
3. `en += str(len(i)) + "#" + i` — write its length, the `#` marker, then the string.
   e.g. `"neet"` → `"4#neet"`.
4. `print(en)` — a leftover **debug line**; harmless, but you can delete it.

**How the code works (line by line) — decode:**
1. `de = []`, `i = 0` — the rebuilt list and a scanning pointer.
2. `while i < len(s):` — keep going until the whole encoded string is consumed.
3. `sta = i` — remember where this chunk's length-number starts.
4. `while s[i] != "#": i += 1` — advance until the `#`; now `s[sta:i]` is the digits.
5. `num = int(s[sta:i])` — how many characters the upcoming string has.
6. `de.append(s[i+1:i+1+num])` — the string is the `num` chars right **after** the `#`
   (`i+1` skips the `#` itself).
7. `i = i + 1 + num` — jump the pointer past the `#` and the string to the next chunk.

**Visual — decoding `"4#neet4#code"`:**

```
index:  0 1 2 3 4 5 6 7 8 9 ...
chars:  4 # n e e t 4 # c o ...
        ▲ ▲ └──┬───┘
       sta │   the 4 chars after '#'  → "neet"
           └ i stops at '#'  (s[0:1] = "4")

then jump i to index 6 and repeat → reads "4#code" → "code"
```

**Why the length-prefix beats a plain separator:** if you encoded with, say, a comma
(`"neet,code"`), a string that itself contains a comma would break decoding. The
length tells you exactly how far to read, so **no character is ever "special"
inside the data**.

> Is there a much better solution? **No** — this length-prefix scheme is the
> standard optimal answer, O(n) both ways. A tiny robustness note: reading the
> length up to `#` (rather than assuming a single digit) is exactly what makes it
> handle strings of length 10+ correctly — which your code already does.