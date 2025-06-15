## Union Function
A set is used to automatically eliminate duplicates and allow O(1) average-time lookups and insertions.
After collecting all unique values from both lists, the final list is created by sorting the set and appending to a new linked list.
### Reasoning Behind Decisions:
1) Uses two sets to capture unique elements from each list
2) No Duplicates are added by using the properties of Set
3) Sorts the result to maintain order before building the final linked list
### Time Efficiency:
O(n log n)
1) Building the set from both list O(n+m) -> O(n)
2) Sorting Order O(n log n)
3) Total Time Complexity O(n log n)


### Space Efficiency:
O(n)

1) Set to store unique elements O(n)

## Intersection Function
Two sets are used: one for each linked list.The intersection is found using set operations and the result is sorted before constructing the output linked list.
### Reasoning Behind Decisions:
1) First set stores unique elements from list 1
2) Second set stores unique elements from list 2
3) Intersection is computed using set1 & set2, then sorted to create a result linked list
### Time Efficiency:
O(n log n)
1) Building the set from both list O(n+m) -> O(n)
2) Intersection Operation O(n)
2) Sorting Order O(n log n)
3) Total Time Complexity O(n log n)

### Space Efficiency:
O(n)

1) Set1 and Set2 atmost O(n)