# Two Sum

🔗 [LeetCode URL](https://leetcode.com/problems/valid-parentheses)

## Approach
- Use a stack or a queue (list in this case) to store previously seen characters.
- While looping over string, check if the matching character is the most recent in the stack, if so, then remove it from the stack. If not add it to the stack.
- The goal is that at the end of the string, check if the stack is empty, if so return true, if not return false.

## Complexity
- ⏱️ Time: O(n)
- 🧠 Space: O(n)

## Data
- Category: String, Stack
- Difficulty: Easy

## Optimizations
- Break early, I assume it is possible to leave early from a str.
- Change the comparing if statements to just a dictionary of pairs.