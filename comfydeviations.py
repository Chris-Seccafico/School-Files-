#######################################
# File: comfydeviations.py
#Author C. Seccafico
#Date 5 May, 2022
#######################################
from prettytable import PrettyTable
import statistics
count = 0
numlist = []
while count < 10:
    x = float(input("enter temp between 68 and 82:"  ""))
    if x >= 68 and x <= 82 :
        numlist.append(x)
        count = count + 1
    else:
        print("temp needs to be between 68 and 82")
    
sample = numlist
sd = statistics.stdev(sample)
if sd > 1:
    c = "not comfy" 

else:
    c = "comfy"
head = PrettyTable(["Standard deviation", "data","comfy/notcomfy"])
for d in sample:
    head.add_row([sd,d,c])
print(head)







    





























