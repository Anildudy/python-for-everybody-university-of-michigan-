name = input("file name :")
fh = open(name)
counts = dict()
for line in fh:
    if not line.startswith("From "):
        continue
    words = line.split()
    counts[words[1]] = counts.get(words[1],0)+1

bigCount = None
bigWord = None
for word,count in counts.items():
    if bigCount is None or count > bigCount:
        bigWord = word
        bigCount = count

print(bigWord,bigCount)
