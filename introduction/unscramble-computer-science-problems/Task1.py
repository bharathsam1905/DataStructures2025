"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
set_texts = set([texts[0][0],texts[0][1]])
set_calls = set([calls[0][0],calls[0][1]])

print('texts',texts[0])
print('calls',calls[0])
print('distinct numbers',set_texts|set_calls)