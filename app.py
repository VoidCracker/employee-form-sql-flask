from flask import Flask, render_template, request, redirect, url_for
import pyodbc

app = Flask(__name__)

# SQL Server connection settings
server = 'localhost'
database = 'saste_iitian'
conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        employeeid = request.form.get('employeeid', '').strip()
        fullname = request.form.get('fullname', '').strip()
        role = request.form.get('role', '').strip()
        email = request.form.get('email', '').strip()
        phonenumber = request.form.get('phonenumber', '').strip()
        joindate = request.form.get('joindate', '').strip()
        
        # Convert Yes/No to 1/0
        working_str = request.form.get('working', '').strip()
        working = 1 if working_str.lower() == 'yes' else 0
        
        salary = request.form.get('salary', '').strip()

        # Validate phone number length
        if len(phonenumber) != 10 or not phonenumber.isdigit():
            return "Please enter a valid 10-digit phone number."

        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO students (EMPLOYEEID, FULLNAME, ROLE, EMAIL, PHONENUMBER, JOINDATE, WORKING, SALARY)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (employeeid, fullname, role, email, phonenumber, joindate, working, salary))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('thank_you'))

    except Exception as e:
        return f"Error occurred: {e}"

@app.route('/thankyou')
def thank_you():
    return render_template('thankyou.html')

if __name__ == '__main__':
    
import os

port = int(os.environ.get('PORT', 5000))  # Use Render's port or 5000 locally
app.run(host='0.0.0.0', port=port)
