# Read file 

# Use the file name mbox-short.txt as the file name
#fname = input("Enter file name: ")
fname = 'mbox-short.txt'
fh = open(fname)
total = 0.00
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    a,b = line.split(": ", 1)
    print(float(b))
    total = total+float(b)
    count = count+1
print("Done. The Average is: ", total/count)