from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    transactions = conn.execute('SELECT id, * FROM transactions ORDER BY date DESC').fetchall()
    conn.close()
    return render_template('index.html', transactions=transactions)
