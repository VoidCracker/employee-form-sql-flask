import pyodbc

try:
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=saste_iitian;'
        'Trusted_Connection=yes;'
    )
    cursor = conn.cursor()
    
    # Insert example
    cursor.execute("""
        INSERT INTO students (EMPLOYEEID, FULLNAME, ROLE, EMAIL, PHONENUMBER, JOINDATE, WORKING, SALARY)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (1006, 'Test User', 'Tester', 'testuser@example.com', '1234567890', '2025-05-29', 1, 5000.00))
    
    conn.commit()  # Save changes
    
    # Fetch data example
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    cursor.close()
    conn.close()
except Exception as e:
    print("Error:", e)
