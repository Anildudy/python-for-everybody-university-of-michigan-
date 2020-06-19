fh = open('mbox-short.txt')
count = 0
tot = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    idx = line.index('0')
    count = count+1
    va = line[idx:]
    val = float(va)
    tot = tot+val
value = tot/count
print('Average spam confidence :', value)
