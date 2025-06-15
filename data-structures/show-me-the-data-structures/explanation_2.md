
## Reasoning Behind Decisions:

Uses recursion to explore all subdirectories.
Checks if each item is a file or directory.
Adds files ending with the given suffix to the result list.
Recursively searches subdirectories.
Normalizes paths for cross-platform consistency.

## Time Efficiency:
O(n) — n is the total number of files and directories.
Each item is processed once in constant time.

## Space Efficiency:
O(n) — to store:

Matched file paths in the result list.
Recursive call stack (in the worst case, depth = n).