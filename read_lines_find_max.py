import operator

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
summary = dict()

for line in fh:
    line = line.rstrip()
    
    if len(line)>1:
        word = line.split()
        if word[0] == 'From':
            for w in word: 
                if w in summary:
                    summary[w]=summary[w]+1
                else:
                    summary[w]=1
        # print(w, summary[w])        
        
print(summary)        
sorted_summary = sorted(summary.items(), key = operator.itemgetter(1))
print()
print(sorted_summary)

