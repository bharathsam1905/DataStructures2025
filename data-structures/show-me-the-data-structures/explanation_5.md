
## Reasoning Behind Decisions:
1) The blockchain stores a sequence of Block objects in a list
2) Each Block includes metadata (timestamp), data payload, and cryptographic hashes (current and previous)
3) The hash is computed using SHA-256 which processes the entire block content (timestamp + data + previous_hash)
4) Adding a new block involves accessing the last block, creating a new one, and appending it — all efficient operations
5) Data size (m) can vary per block, so both time and space   complexities depend on it

## Time Efficiency:
O(n)
1) Creating Genesis Block: O(1)
2) Adding Each Block: Access last block: O(1)
3) SHA-256 hash computation: O(n) (where n is length of the data string)
4) Total for n blocks: O(n * m) If m is constant, it simplifies to O(n)


## Space Efficiency:
O(n)

Total for n blocks


