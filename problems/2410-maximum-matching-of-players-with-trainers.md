# 2410. Maximum Matching of Players With Trainers

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Two Pointers` `Greedy` `Sorting`

## Problem

> You are given a 0-indexed integer array players, where players[i] represents the ability of the ith player. You are also given a 0-indexed integer array trainers, where trainers[j] represents the training capacity of the jth trainer.  The ith player can match with the jth trainer if the player's ability is less than or equal to the trainer's training capacity. Additionally, the ith player can be m...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        idx = 0
        for trainer in trainers:
            if idx == len(players):
                break
            if trainer >= players[idx]:
                idx += 1
        return idx
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2410 Maximum Matching of Players With Trainers -->
