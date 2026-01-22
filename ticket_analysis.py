import sqlite3

# 1. Connect to a database (creates it in memory)
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# 2. Create a table for Helpdesk Tickets
cursor.execute('''
CREATE TABLE tickets (
    id INTEGER PRIMARY KEY,
    issue_type TEXT,
    department TEXT,
    priority TEXT
)
''')

# 3. Insert mock data simulating real IT support requests
tickets_data = [
    ('Password Reset', 'Finance', 'High'),
    ('Hardware Failure', 'IT', 'Critical'),
    ('Software Install', 'Marketing', 'Low'),
    ('Password Reset', 'Sales', 'High'),
    ('VPN Issue', 'Finance', 'Medium'),
    ('Password Reset', 'HR', 'High')
]
cursor.executemany('INSERT INTO tickets (issue_type, department, priority) VALUES (?, ?, ?)', tickets_data)

# 4. SQL Query: Find the most common issue type
print("--- Helpdesk Trend Analysis ---")
cursor.execute('SELECT issue_type, COUNT(*) as count FROM tickets GROUP BY issue_type ORDER BY count DESC')
rows = cursor.fetchall()

for row in rows:
    print(f"Issue: {row[0]} | Frequency: {row[1]}")

conn.close()
