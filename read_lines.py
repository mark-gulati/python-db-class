fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    lines = line.split()
    if len(lines)>1 and lines[0] == 'From':
        print(lines[1])
        count = count + 1
        
print("There were", count, "lines in the file with From as the first word")

