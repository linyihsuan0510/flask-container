from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host='db',  # Docker 裡面我們會設定 container 名為 db
        user='root',
        password='password',
        database='testdb',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    conn = get_db_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
        conn.commit()
    return 'Submitted!'

@app.route('/users')
def users():
    conn = get_db_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            data = cursor.fetchall()
    return render_template('users.html', users=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)



