from flask import Flask, request, redirect, render_template_string
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return "<h1>Welcome to Secure Flask App</h1>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
        cursor.execute(query)  # SQL Injection vulnerability
        user = cursor.fetchone()
        conn.close()
        
        if user:
            return "<h1>Login successful</h1>"
        else:
            return "<h1>Invalid credentials</h1>"
    
    return render_template_string('<form method="post">Username: <input type="text" name="username"><br>Password: <input type="password" name="password"><br><input type="submit"></form>')

if __name__ == '__main__':
    app.run(debug=True)
