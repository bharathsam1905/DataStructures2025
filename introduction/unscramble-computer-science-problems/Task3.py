"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
#print(calls)
codes_called_by_bangalore=set()

for call in calls:
  caller,receiver=call[0],call[1]
  if re.match(r'^\(080\)',caller):   #calls intiated from bangalore
    if re.match(r'^\(0\d+\)',receiver):
      area_code=re.match(r'^\(0\d+\)',receiver).group()
      codes_called_by_bangalore.add(area_code)
    elif re.match(r'^[789]\d{3}',receiver)  and ' ' in receiver:
      mobile_numbers=receiver[:4]
      codes_called_by_bangalore.add(mobile_numbers)
    elif receiver.startswith('140'):
      codes_called_by_bangalore.add('140')
#PartA
print("The numbers called by people in Bangalore have codes:")
for code in sorted(codes_called_by_bangalore):
    print(code)

#PartB
total_b_calls=0
b2b_calls=0
  
for call in calls:
  caller,receiver=call[0],call[1]
  if re.match(r'^\(080\)',caller):
    total_b_calls+=1
    if re.match(r'^\(080\)',receiver):
     b2b_calls+=1

if total_b_calls>0:
  call_percentage=(b2b_calls/total_b_calls)*100
  print(round(call_percentage,2),\
  'percent of calls from fixed lines in Bangalore are calls',\
  'to other fixed lines in Bangalore.')
else:
  print("No calls were made from Bangalore numbers")