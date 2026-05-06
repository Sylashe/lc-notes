# 2469. Convert the Temperature

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Math`

## Problem

> You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the temperature in Celsius.  You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].  Return the array ans. Answers within 10-5 of the actual answer will be accepted.  Note that:   	Kelvin = Celsius + 273.15 	Fahrenheit = Celsius * 1.80 + 32.00...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2469 Convert the Temperature -->
