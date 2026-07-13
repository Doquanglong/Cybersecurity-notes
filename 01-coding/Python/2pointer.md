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

**Trace with `s = "a,b a"`:** (alphanumeric chars are `a`, `b`, `a`)

| `start` | `end` | `s[start]` | `s[end]` | Action                          |
|---------|-------|------------|----------|---------------------------------|
| 0       | 4     | `a`        | `a`      | match → move inward             |
| 1       | 3     | `,` → skip | ` ` → skip | skip junk → start=2, end=2     |
| 2       | 2     | —          | —        | `start < end` false → stop      |

`return True` ✅

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
