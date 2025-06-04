import heapq
from collections import defaultdict
from typing import Optional

# Huffman Tree Node
class HuffmanNode:
    """
    A class to represent a node in the Huffman Tree.

    Attributes:
    -----------
    char : Optional[str]
        The character stored in the node.
    freq : int
        The frequency of the character.
    left : Optional[HuffmanNode]
        The left child node.
    right : Optional[HuffmanNode]
        The right child node.
    """

    def __init__(self, char: Optional[str], freq: int) -> None:
        """
        Constructs all the necessary attributes for the HuffmanNode object.

        Parameters:
        -----------
        char : Optional[str]
            The character stored in the node.
        freq : int
            The frequency of the character.
        """
        self.char=char
        self.freq=freq
        self.left=None
        self.right=None

    def __lt__(self, other: 'HuffmanNode') -> bool:
        """
        Less-than comparison operator for HuffmanNode.

        Parameters:
        -----------
        other : HuffmanNode
            The other HuffmanNode to compare with.

        Returns:
        --------
        bool
            True if the frequency of this node is less than the other node, False otherwise.
        """
        return self.freq<other.freq

def calculate_frequencies(data: str) -> dict[str, int]:
    """
    Calculate the frequency of each character in the given data.

    Parameters:
    -----------
    data : str
        The input string for which frequencies are calculated.

    Returns:
    --------
    Dict[str, int]
        A dictionary with characters as keys and their frequencies as values.
    """
    Dict_String={}  #initialize a dictionary
    for i in data:
        if i in Dict_String:
            Dict_String[i]+=1
        else:
            Dict_String[i]=1
    return Dict_String            
 
import heapq
def build_huffman_tree(frequency: dict[str, int]) -> HuffmanNode:
    """
    Build the Huffman Tree based on the character frequencies.

    Parameters:
    -----------
    frequency : Dict[str, int]
        A dictionary with characters as keys and their frequencies as values.

    Returns:
    --------
    HuffmanNode
        The root node of the constructed Huffman Tree.
    """
    heap = []
    for char,freq in frequency.items():
        heapq.heappush(heap, HuffmanNode(char, freq))
    
    while len(heap)>1:
        left=heapq.heappop(heap)
        right=heapq.heappop(heap)
        
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left=left
        merged.right=right
        
        heapq.heappush(heap, merged)
    return heap[0]



freq = calculate_frequencies("abcaba")
build_huffman_tree(freq) 
        
    

def generate_huffman_codes(node: Optional[HuffmanNode], code: str, huffman_codes: dict[str, str]) -> None:
    """
    Generate Huffman codes for each character by traversing the Huffman Tree.

    Parameters:
    -----------
    node : Optional[HuffmanNode]
        The current node in the Huffman Tree.
    code : str
        The current Huffman code being generated.
    huffman_codes : Dict[str, str]
        A dictionary to store the generated Huffman codes.
    """
    if node is None:
        return
    if node.char is not None:
        huffman_codes[node.char]=code if code else "0"
    generate_huffman_codes(node.left,code+"0",huffman_codes)
    generate_huffman_codes(node.right,code+"1",huffman_codes)
    


def huffman_encoding(data: str) -> tuple[str, Optional[HuffmanNode]]:
    """
    Encode the given data using Huffman coding.

    Parameters:
    -----------
    data : str
        The input string to be encoded.

    Returns:
    --------
    Tuple[str, Optional[HuffmanNode]]
        A tuple containing the encoded string and the root of the Huffman Tree.
    """
    if not data:
        return "",None
    #Calculate character frequencies
    cal_freq=calculate_frequencies(data)
    #build huffman tree
    build_htree=build_huffman_tree(cal_freq)
    #generate huffman codes by traversing the tree
    huffman_codes_dict={}
    generate_hcode=generate_huffman_codes(build_htree,"",huffman_codes_dict)
    #Start encoding
    encoded_text=""
    for char in data:
        encoded_text+=huffman_codes_dict[char]
    return encoded_text,build_htree


data = "abbccc"
encoded,tree=huffman_encoding(data)
print("encoded: ",encoded)

def huffman_decoding(encoded_data: str, tree: Optional[HuffmanNode]) -> str:
    """
    Decode the given encoded data using the Huffman Tree.

    Parameters:
    -----------
    encoded_data : str
        The encoded string to be decoded.
    tree : Optional[HuffmanNode]
        The root of the Huffman Tree used for decoding.

    Returns:
    --------
    str
        The decoded string.
    """
    if not tree or not encoded_data:
        return ""
    if tree.left is None and tree.right is None:
        return tree.char*len(encoded_data)
    decoded_string=""
    current=tree
    for bit in encoded_data:
        if bit=='0':
            current=current.left
        else:
            current=current.right
            
        if current.char is not None:
            decoded_string+=current.char
            current=tree
    
    return decoded_string

encoded_data = "1100100111"
decoded_data = huffman_decoding(encoded_data, tree)
print(decoded_data) 


# Main Function
if __name__ == "__main__":
    # Test Case 1: Standard test case
    print("\nTest Case 1: Standard sentence")
    sentence = "Huffman coding is fun!"
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data

    # Test Case 2
    print("\nTest Case 2: Repeating characters")
    sentence = "aaaabbbccd"
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data

    # Test Case 3
    print("\nTest Case 3: Single unique character")
    sentence = "zzzzzzzz"
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data
