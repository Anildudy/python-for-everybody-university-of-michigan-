import re
file = input("Enter file name: ")
fh = open(file)
mylst = list()
for line in fh:
        line.rstrip()
        lst = re.findall('[0-9]+',line)
        if len(lst)>=1:
            mylst.extend(lst)
total = 0
for item in mylst:
    new = int(item)
    total = total+new
print(total)
