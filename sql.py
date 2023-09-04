import sqlite3

# Connect to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect(':memory:')

# Create the "Ages" table if it doesn't exist
conn.execute("""CREATE TABLE IF NOT EXISTS Ages (
                 name VARCHAR(128),
                 age INTEGER
                 )"""
             )

# Delete any existing rows in the table
conn.execute("DELETE FROM Ages")

# Insert the provided rows
conn.execute("INSERT INTO Ages (name, age) VALUES ('Inemesit', 19)")
conn.execute("INSERT INTO Ages (name, age) VALUES ('Coleen', 30)")
conn.execute("INSERT INTO Ages (name, age) VALUES ('Alexzander', 32)")
conn.execute("INSERT INTO Ages (name, age) VALUES ('McKay', 36)")

# Execute the SELECT query to find the required string
result = conn.execute("SELECT hex(name || age) AS X FROM Ages ORDER BY X")
first_row = result.fetchone()
if first_row:
    required_string = first_row[0]
    print(required_string)

# Close the database connection
conn.close()