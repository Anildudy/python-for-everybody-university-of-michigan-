name = input("Enter file name: ")
fh = open(name)
count = dict()
for line in fh:
    if not line.startswith("From "):
        continue
    lst = line.split()
    hr = lst[5].split(':')
    count[hr[0]] = count.get(hr[0],0)+1
newLst = list()
for key,val in count.items():
    tup = (key, val)
    newLst.append(tup)
newLst = sorted(newLst)
for key,val in newLst:
    print(key,val)
