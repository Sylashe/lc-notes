# 71. Simplify Path

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `String` `Stack`

## Problem

> You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.  The rules of a Unix-style file system are as follows:   	A single period '.' represents the current directory. 	A double period '..' represents the previous/parent directory. 	Multiple consecutive slashes such as '//' a...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for f in path:
            if f == '' or f == '.':
                continue
            elif f == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(f)
        return '/' + '/'.join(stack)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #71 Simplify Path -->
