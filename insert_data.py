import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

def insert_data():
    c.execute('''INSERT INTO hrm_users
(employee_id, name, age, ranking)
VALUES ('GJ009', 'HARRY MCLAREN', '22', '3.0');''')
    conn.commit()
    c.close()
    conn.close()

insert_data()
