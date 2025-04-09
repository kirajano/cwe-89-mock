from flask import Flask, request, render_template_string
import sqlite3
app = Flask(__name__)
DATABASE = 'users.db'
# Initialize the database (create a table if it doesn't exist)
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    cursor.execute('''
            INSERT INTO users (id, username, password)
                VALUES
                    (1, "elias", "union_123"),
                    (2, "rohan", "secret_sauce123"),
                    (3, "thomas", "heavy_load123")
                    ;
        ''')
    conn.commit()
    conn.close()

init_db()
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        query = f"SELECT * FROM users WHERE username = '{username}'"
        try:
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            conn.close()
            if results:
                return render_template_string(f"<p>User found: {results}</p>")
            else:
                return "<p>User not found.</p>"
        except sqlite3.Error as e:
            return f"<p>Database error: {e}</p>"
    else:
        return render_template_string('''
            <form method="post">
                Username: <input type="text" name="username">
                <input type="submit" value="Search">
            </form>
        ''')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
