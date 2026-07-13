# 👉👈 Two Pointers — Problem Write-ups

Solutions and notes for the **Two Pointers** problems.

> **Pattern in one line:** use two indices (often one at each end, or one slow +
> one fast) that move toward each other or in step, so you solve the problem in a
> single O(n) pass with O(1) extra space instead of nested loops.

---

## 125. Valid Palindrome

**Problem:** Given a string `s`, return `True` if it is a palindrome, considering
only **alphanumeric** characters and ignoring case. Spaces, punctuation, and
symbols are skipped.

```
"A man, a plan, a canal: Panama"  → True
"race a car"                       → False
```

**Idea:** A palindrome reads the same forwards and backwards. Put one pointer at
the **start** and one at the **end**, then walk them toward the middle comparing
characters. Skip anything that isn't a letter or digit. If every compared pair
matches, it's a palindrome.

**Approach (step by step):**
1. `start` at index `0`, `end` at the last index.
2. While `start < end`:
   - Move `start` right past any non-alphanumeric characters.
   - Move `end` left past any non-alphanumeric characters.
   - Compare the two characters, lowercased. If they differ → return `False`.
   - Step both pointers inward and continue.
3. If the loop finishes with no mismatch → return `True`.

**Complexity:**
| | |
|-----------|-----------------------------------------------|
| **Time**  | O(n) — each pointer crosses the string once   |
| **Space** | O(1) — no extra string/array built            |

**My solution:**
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True
```
✅ Correct and optimal.

**Functions used here:**
> ℹ️ **`s[i].isalnum()`** — returns `True` if the character is a letter or a digit
> (alphanumeric), `False` for spaces, punctuation, symbols. Used to skip the
> characters the problem says to ignore.
>
> ℹ️ **`s[i].lower()`** — returns the lowercase version of the character, so the
> comparison ignores case (`'A'` matches `'a'`).

**How the code works (line by line):**
1. `start = 0`, `end = len(s) - 1` — the two pointers at each end of the string.
2. `while start < end:` — keep going until the pointers meet in the middle.
3. `while start < end and not s[start].isalnum(): start += 1` — skip junk on the
   left. The `start < end` guard stops the pointer from running off the end if the
   rest is all non-alphanumeric.
4. `while start < end and not s[end].isalnum(): end -= 1` — same, skipping junk on
   the right.
5. `if s[start].lower() != s[end].lower(): return False` — both pointers now sit on
   real characters; if they don't match (case-insensitive), it's **not** a palindrome.
6. `start += 1`, `end -= 1` — matched, so step both inward and check the next pair.
7. `return True` — pointers crossed with no mismatch → it's a palindrome.

**Visual — two pointers walking inward, skipping junk:**

```
"A man, a plan, a canal: Panama"
 ▲                              ▲
 start                        end     compare A == a ✔ move in
   ▲                          ▲
   (skip space)          (skip a)     compare m == m ✔ ...
              ...pointers keep closing in, all pairs match...
                    ▲    ▲
                  start end            they meet → return True
```

> Is there a much better solution? **No** — two pointers is the optimal O(n) time,
> O(1) space answer. A simpler-to-write but heavier alternative is to filter +
> lowercase into a new string and compare it to its reverse
> (`clean == clean[::-1]`); that's still O(n) time but uses O(n) extra space for
> the cleaned string.

---

## 167. Two Sum II — Input Array Is Sorted

**Problem:** Given a **sorted** (ascending) array `numbers` and a `target`, return
the **1-indexed** positions of the two numbers that add up to `target`. Exactly one
solution exists, and you must use O(1) extra space.

```
numbers = [2, 7, 11, 15], target = 9  →  [1, 2]   (2 + 7 = 9)
```

**Idea:** Because the array is **sorted**, put one pointer at the smallest value
(`left`) and one at the largest (`right`). Their sum tells you which way to move:
- Sum **too small**? Move `left` right to a bigger number.
- Sum **too big**? Move `right` left to a smaller number.
- Sum **just right**? Found it.

This is the key difference from the original Two Sum (#1): that one wasn't sorted, so
it needed a hash map. Here the sorted order lets us do it with **O(1) space**.

**Approach (step by step):**
1. `l` at the start, `r` at the end.
2. While `l < r`, look at `numbers[l] + numbers[r]`:
   - `< target` → `l += 1` (need a larger sum).
   - `> target` → `r -= 1` (need a smaller sum).
   - `== target` → return `[l+1, r+1]` (convert to 1-indexed).

**Complexity:**
| | |
|-----------|-----------------------------------------------|
| **Time**  | O(n) — pointers move toward each other once   |
| **Space** | O(1) — just two pointers, no hash map         |

**My solution:**
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            if (numbers[l] + numbers[r] < target):
                l += 1
            elif (numbers[l] + numbers[r] > target):
                r -= 1
            else:
                return [l + 1, r + 1]
        return [1]
```
✅ Correct and optimal.

**How the code works (line by line):**
1. `l = 0`, `r = len(numbers) - 1` — pointers at the smallest and largest values.
2. `while l < r:` — keep narrowing until they meet.
3. `if numbers[l] + numbers[r] < target: l += 1` — sum is too small; the only way to
   grow it is a bigger left value (right is already the max available).
4. `elif ... > target: r -= 1` — sum is too big; shrink it with a smaller right value.
5. `else: return [l + 1, r + 1]` — exact match. `+1` on each because the problem wants
   1-indexed positions, not 0-indexed.
6. `return [1]` — a fallback that's never actually reached, since the problem
   guarantees exactly one solution exists.

**Trace with `numbers = [2, 7, 11, 15]`, `target = 9`:**

| `l` | `r` | `numbers[l]+numbers[r]` | vs target | Action              |
|-----|-----|-------------------------|-----------|---------------------|
| 0   | 3   | 2 + 15 = 17             | too big   | `r -= 1`            |
| 0   | 2   | 2 + 11 = 13             | too big   | `r -= 1`            |
| 0   | 1   | 2 + 7 = 9               | match     | return `[1, 2]`     |

**Visual — pointers converge based on the sum:**

```
[ 2, 7, 11, 15 ]   target = 9
  ▲          ▲
  l          r     17 > 9 → move r left
  ▲      ▲
  l      r         13 > 9 → move r left
  ▲   ▲
  l   r            9 == 9 → return [l+1, r+1] = [1, 2]
```

> Is there a much better solution? **No** — O(n) time / O(1) space is optimal, and it
> beats the hash-map Two Sum (#1) on *space* precisely because the input is sorted.

---

## 15. 3Sum

**Problem:** Given an array `nums`, return **all unique triplets** `[a, b, c]` such
that `a + b + c == 0`. No duplicate triplets in the output.

```
nums = [-1, 0, 1, 2, -1, -4]  →  [[-1, -1, 2], [-1, 0, 1]]
```

**Idea:** **Sort the array first**, then fix one number `nums[i]` and look for two
others that sum to `-nums[i]` in the rest of the array — which is exactly the
**Two Sum II** two-pointer trick (#167) applied to the part after `i`. Sorting also
makes it easy to **skip duplicates** so triplets aren't repeated.

**Approach (step by step):**
1. Sort `nums`.
2. For each index `i`:
   - Skip it if it's the same value as the previous `i` (avoids duplicate triplets).
   - Set `l = i+1`, `r = last index`, and two-pointer for a pair summing to `-nums[i]`
     (i.e. `nums[i] + nums[l] + nums[r] == 0`).
   - On a match, record the triplet, then move **both** pointers *and* skip over any
     duplicate values so you don't record the same triplet twice.

**Complexity:**
| | |
|-----------|--------------------------------------------------------|
| **Time**  | O(n²) — one loop over `i`, an O(n) two-pointer scan each |
| **Space** | O(1) extra (ignoring the output and the sort)          |

**My solution:**
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        re = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if (nums[i] + nums[l] + nums[r] < 0):
                    l += 1
                elif (nums[i] + nums[l] + nums[r] > 0):
                    r -= 1
                else:
                    re.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return re
```
✅ Correct and optimal.

**How the code works (line by line):**
1. `nums.sort()` — sorting is what makes both the two-pointer scan and duplicate-skipping possible.
2. `for i in range(len(nums)):` — fix the first number of the triplet.
3. `if i > 0 and nums[i] == nums[i-1]: continue` — if this value is the same as the
   previous one, we already found every triplet starting with it → skip to avoid duplicates.
4. `l = i + 1`, `r = len(nums) - 1` — two pointers over the region *after* `i`.
5. `if sum < 0: l += 1` — total too small; a bigger left value grows it (array is sorted).
6. `elif sum > 0: r -= 1` — total too big; a smaller right value shrinks it.
7. `else:` — sum is exactly 0 → record `[nums[i], nums[l], nums[r]]`.
8. `l += 1`, `r -= 1` — move past the pair we just used.
9. `while l < r and nums[l] == nums[l-1]: l += 1` — skip duplicate left values so the
   same triplet isn't added again.
10. `while l < r and nums[r] == nums[r+1]: r -= 1` — same duplicate-skip on the right.
11. `return re` — all unique triplets.

**Trace with `nums = [-1, 0, 1, 2, -1, -4]` → sorted `[-4, -1, -1, 0, 1, 2]`:**

| `i` (`nums[i]`) | `l`..`r` scan | Found |
|-----------------|----------------|-------|
| 0 (`-4`) | needs pair = 4; max pair (1+2=3) < 4 → nothing | — |
| 1 (`-1`) | `-1 + (-1) + 2 = 0` ✔, then `-1 + 0 + 1 = 0` ✔ | `[-1,-1,2]`, `[-1,0,1]` |
| 2 (`-1`) | duplicate of previous `i` → **skip** | — |
| 3 (`0`) | `0 + 1 + 2 = 3 > 0`, pointers cross | — |

Result: `[[-1, -1, 2], [-1, 0, 1]]` ✅

**Visual — fix `i`, then two-pointer the rest (`i = 1`, value `-1`):**

```
sorted: [ -4, -1, -1,  0,  1,  2 ]
               i   ▲           ▲
                   l           r     -1 + (-1) + 2 = 0 ✔ record, move both
               i       ▲   ▲
                       l   r         -1 +  0  + 1 = 0 ✔ record, pointers meet → next i
```

> Is there a much better solution? **No** — O(n²) is the optimal known bound for 3Sum.
> The brute-force triple loop is O(n³); sorting + two pointers removes a whole factor
> of `n`. This is the canonical "fix one, two-pointer the rest" pattern that also
> extends to 4Sum.
