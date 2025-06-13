## Task0
Description: 
This task retrieves specific records from two files, texts.csv and calls.csv, which store logs of text messages and calls, respectively. The objective is to print:
i) The first record from texts data
ii) The last record from the calls data

Approach :
i) Read data from the texts.csv and calls.csv files using the csv.reader.
ii) Convert each file’s content to a list, so that individual records can be accessed by their position in the list.
iii) Access the first element of the texts list and the last element of the calls list directly by their indices.
iv) Print the required details in the specified format.

Complexity Analysis:
i) Algorithm: Access the first and last elements of lists and print their details.
ii) Big O Notation:O(1), constant time.
iii) Justification:
Accessing the first element of texts and the last element of calls requires only constant time, O(1)

## Task1
Description: 
The objective of this task is to determine the number of unique telephone numbers in the records from texts.csv and calls.csv. This involves counting distinct phone numbers from both incoming and answering sides of each record in both files.

Approach:
i) Read the content of texts.csv and calls.csv into lists.
ii) Create a set called distinct_numbers to store unique telephone numbers.
iii) Loop through each record in texts and calls and add both the sender and receiver numbers from each record to distinct_numbers.
iv) Count the total unique numbers by measuring the size of call_dict using len().
Complexity Analysis:
Algorithm: This approach iterates through each record in the texts and calls lists, adding numbers to a set to ensure uniqueness.
Big O notation: O(n)
Justificaiton: O(n+n) where n is number of records in texts and calls. Which will be represented as O(n) since constants are eliminated.
## Task2
Description: Identify the phone number with the longest total call time during September 2016, considering both incoming and outgoing call durations.

Approach:
Read call data from calls.csv.
Initialize call_dict to store each phone number’s total call duration.
For each call record in September 2016:
Add the call duration to both the caller's and receiver's totals.


Complexity Analysis:
Algorithm: Traverse the list once, updating a dictionary.
Big O Notation: 
O(n), where n is the number of call records.
Justification: One pass through calls with constant-time dictionary operations.

## Task3
Description: This task identifies the unique area codes and mobile prefixes called by Bangalore numbers. It also calculates the percentage of calls made from Bangalore numbers to other Bangalore numbers.
Approach:
PartA:
i) for loop takes 2 lists : O(2n)  implies O(n)
ii) if block will take O(m^2) since there are 2 if blocks where m is a constant, so O(1^2)=O(1).
iii) elif takes O(n),  O(n)
iv) Sorting takes O(nlogn)
Complexity Analysis:
Algorithm: This traverses through call list and  sorts records
Big O Notation: O(nlogn)
Justificaiton: O(n)+O(1)+O(nlogn)=O(nlogn)

Approach:
PartB: 
i) for loop takes 2 lists : O(2n)  implies O(n)
ii) if block will take O(m) where m is a constant phone numbers are fixed, so O(1).
iii) Calculate Percentage O(1)
Complexity Analysis:
Algorithm: This traverses through call list 
Big O Notation: O(n)
Justificaiton: O(n)+O(1)+O(1)=O(n)

## Task4

Description: Identify potential telemarketers as numbers that make outgoing calls but do not receive calls, send texts, or receive texts.

Approach:
i) Call Callers + Call Receivers + Text Callers + Text Receivers O(4n) = O(n)
ii) Sorting O(nlogn)
Complexity Analysis:
Algorithm: Uses set operations to identify telemarketers in constant time per operation and also sorts the output.
Big O Notation: O(nlogn)
Justification : O(n)+O(nlogn)=O(nlogn)