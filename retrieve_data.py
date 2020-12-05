import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

def retrieve_data():
    c.execute('''SELECT * FROM hrm_users WHERE employee_id='GJ001';''')
    result = c.fetchall()
    for row in result:
        print(row)
    conn.commit()
    c.close()
    conn.close()

retrieve_data()
