"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
from datetime import datetime
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
#print('dateiem',datetime.strptime(calls[0][2],"%m-%d-%Y %H:%M:%S").date())
call_dict={}
for i in range(len(calls)):
    startdate=datetime(2016,9,1).date()  
    enddate=datetime(2016,9,30).date()
    inputdate=datetime.strptime(calls[i][2],"%d-%m-%Y %H:%M:%S").date()
    if(inputdate>=startdate and inputdate<=enddate):  
     caller=calls[i][0]
     receiver=calls[i][1]
     duration=int(calls[i][3])
     if caller in call_dict:
         call_dict[caller]+=duration
     else:
        call_dict[caller]=duration
     if receiver in call_dict:
         call_dict[receiver]+=duration
     else:
        call_dict[receiver]=duration
         
     
max_key, max_value = max(call_dict.items(), key=lambda x: x[1])
print('Telephone Number',max_key,'spent the longest time,',max_value,'seconds, on the phone during \
September 2016.')
