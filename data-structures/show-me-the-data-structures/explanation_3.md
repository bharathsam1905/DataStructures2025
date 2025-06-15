
## Reasoning Behind Decisions:
1) Frequency of characters is counted in one pass over the input
2) Min-heap is used to efficiently build the Huffman Tree by always combining the two least frequent nodes
3) Huffman codes are generated via a tree traversal.
4) Encoding is done by replacing each character with its binary code
5) Decoding is done by traversing the tree per bit until reaching a character


## Time Efficiency:
O(n log n)

1) Frequency count: O(n)
2) Building heap of at most n unique characters: O(n log n)
3) Generating codes (tree traversal): O(n)
4) Encoding the input: O(n)
5) Decoding the encoded string: O(n)

## Space Efficiency:
O(n)

1) Heap storage for nodes: O(n)
2) Huffman Tree: O(n)
3) Huffman Codes dictionary: O(n)
4) Encoded string: O(n) 
5) Decoded string: O(n)
