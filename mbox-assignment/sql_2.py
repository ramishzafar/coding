# import sqlite3

# # Connect to the SQLite database (or create it if it doesn't exist)
# conn = sqlite3.connect('emaildb.sqlite')
# cur = conn.cursor()

# # Create the "Counts" table if it doesn't exist
# cur.execute('''CREATE TABLE IF NOT EXISTS Counts (
#                 org TEXT,
#                 count INTEGER
#                 )''')

# # Prompt the user to enter the file name
# filename = input('Enter file name: ')
# if len(filename) < 1:
#     filename = 'mbox.txt'

# # Open the file
# try:
#     fhand = open(filename)
# except:
#     print('File not found.')
#     quit()

# # Process the file
# if __name__== '__main__':
#     for line in fhand:
#         if line.startswith('From: '):
#             pieces = line.split()
#             email = pieces[1]
#             # Extract the domain from the email address
#             domain = email.split('@')[1]

#             # Update or insert the organization count in the database
#             cur.execute('SELECT count FROM Counts WHERE org = ?', (domain,))
#             row = cur.fetchone()
#             if row is None:
#                 cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domain,))
#             else:
#                 cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))

# # Commit the changes to the database
# conn.commit()

# # Retrieve and print the results
# sql_query = 'SELECT org, count FROM Counts ORDER BY count DESC'
# for row in cur.execute(sql_query):
#     print(row[0], row[1])

# # Close the database connection
# cur.close()

import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
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

conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
    # Extract the domain from the email address
    domain = row[0].split('@')[1]
    count = row[1]

    




cur.close()
