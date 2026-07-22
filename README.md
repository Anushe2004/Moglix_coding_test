#Author

##Name: Anush E

##Problem: Longest Valid Parentheses

##Approach: Two Traversals (Left-to-Right & Right-to-Left)

##Language: Python

##Time Complexity: O(n)

##Space Complexity: O(1)

# Longest Valid Parentheses (Two Traversals)

## Problem Statement

Given a string containing only the characters `'('` and `')'`, find the length of the **longest valid (well-formed) parentheses substring**.

### Example 1

```text
Input: s = "(()"
Output: 2

Explanation:
The longest valid substring is "()".
```

### Example 2

```text
Input: s = ")()())"
Output: 4

Explanation:
The longest valid substring is "()()".
```

### Example 3

```text
Input: s = ""
Output: 0
```

### Constraints

* `0 <= s.length <= 3 × 10⁴`
* `s[i]` is either `'('` or `')'`

---

# Approach: Two Traversals

## Intuition

A valid parentheses substring must contain an **equal number of opening and closing brackets**.

While scanning the string, we keep track of:

* `left` → Number of `'('`
* `right` → Number of `')'`

Whenever:

* `left == right`

  * We have a valid substring.
  * Length = `2 × right`.

However, a **single left-to-right traversal is not enough**.

### Why?

Consider:

```text
(()(
```

The scan ends with extra `'('`, so the valid substring is not detected correctly.

Similarly,

```text
)()())
```

contains extra `')'` at the beginning.

To handle both situations, we perform **two scans**.

---

# Traversal 1: Left → Right

Initialize:

```text
left = 0
right = 0
maxLen = 0
```

For every character:

* If `'('`

  * Increment `left`
* Else

  * Increment `right`

### Case 1

If

```text
left == right
```

then

```text
maxLen = max(maxLen, 2 × right)
```

because we have a balanced substring.

### Case 2

If

```text
right > left
```

then reset

```text
left = 0
right = 0
```

Reason:

More closing brackets than opening brackets means no valid substring can continue through this point.

---

# Traversal 2: Right → Left

Now scan from the end of the string.

Again maintain

```text
left
right
```

### Case 1

If

```text
left == right
```

update

```text
maxLen
```

### Case 2

If

```text
left > right
```

reset

```text
left = 0
right = 0
```

Reason:

While scanning backwards, extra opening brackets become invalid in the same way extra closing brackets were during the forward scan.

---

# Example

Input

```text
(()())
```

### Left → Right

| Character | Left | Right | Max |
| --------- | ---- | ----- | --- |
| (         | 1    | 0     | 0   |
| (         | 2    | 0     | 0   |
| )         | 2    | 1     | 0   |
| (         | 3    | 1     | 0   |
| )         | 3    | 2     | 0   |
| )         | 3    | 3     | 6   |

Result after first traversal:

```text
maxLen = 6
```

The second traversal confirms the same answer.

---

# Why Two Traversals Work

The first traversal correctly handles cases with **extra closing brackets**.

Example:

```text
)()())
```

The second traversal correctly handles cases with **extra opening brackets**.

Example:

```text
(()(
```

Together, they ensure every valid substring is considered.

---

# Complexity Analysis

### Time Complexity

* Left-to-right traversal → **O(n)**
* Right-to-left traversal → **O(n)**

Overall:

```text
O(n)
```

### Space Complexity

Only a few integer variables are used.

```text
O(1)
```

---

# Key Takeaways

* Count opening and closing brackets instead of using a stack.
* Reset counters when an invalid imbalance occurs.
* Perform **two traversals** to handle both extra `')'` and extra `'('`.
* Achieves **O(n)** time with **O(1)** extra space.
