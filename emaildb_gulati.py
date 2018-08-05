import sqlite3

conn = sqlite3.connect('email_messages.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
print("Committing 1...")

conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# add counts by org in a separate table
cur.execute('DROP TABLE IF EXISTS org_counts')

cur.execute('CREATE TABLE org_counts (org TEXT, count INTEGER)')


query2 = '''SELECT substr(email, instr(email, '@') + 1) as org, sum(count) as count 
from Counts
GROUP BY 1
ORDER BY sum(count) DESC'''
results = cur.execute(query2)
print("Starting 2nd execution...")
print(type(results))
print(results)
for row in results.fetchall():
    print(str(row[0]), row[1])
    cur.execute('INSERT INTO org_counts (org, count) VALUES (?, ?)', (str(row[0]), row[1]))

print("Committing 2... Deleting Count table")
cur.execute('DROP TABLE Counts')
print("Renaming org_counts table to Counts")
cur.execute('ALTER TABLE org_counts RENAME TO Counts')

conn.commit()
cur.close()