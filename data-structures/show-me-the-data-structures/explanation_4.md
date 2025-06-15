
## Reasoning Behind Decisions:
1) Users can be directly inside a group or nested within subgroups.
2) A stack-based Depth-First Search is used to explore all groups and subgroups.
3) Each group is visited once, and the user list of each is checked.

## Time Efficiency:
O(n)

1) You visit each of the k groups exactly once → O(k)
2) In the worst case, you may check all n users (if the user is not found) → O(n)

## Space Efficiency:
1) The stack used for iterative DFS holds up to n groups O(n)
2) No additional storage for users or recursive call stack