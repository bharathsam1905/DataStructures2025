
## Reasoning Behind Decisions:
Use of OrderedDict:
1)OrderedDict mainitains insertion Order and allows reordering of elements efficiently. This is crucial for an LRU cached since accessing a key and mark it as recently used is important

get() method:
If the key exists , it is removed using pop(key) and reinserted using cache[key]=value to mark it as recently used. Else return -1

Set() method:
1) If the key already exists remove and it and reinsert it to update both the value and usage order.
2) If cached is full remove the leaset recently used key-value pair
3) Insert the new key at the end

## Time Efficiency:
O(1)
Reason:
get(key) Method : Lookup in OrderedDict is O(1), and 
pop() + reinsertion is also O(1).
set(key,val) Method : Key existence check, insertion, and removal (if needed) are all constant time. O(1)
popitem(False) Method: Removes the least recently used item (from the start) in constant time.O(1)
## Space Efficiency:
O(n)
Reason:
OrderedDict internally uses doubly linked list and hash table where n is capacity of cache