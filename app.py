from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Docker!, this is favour's first docker app running on port 5001"

@app.route("/db")
def db_test():
    try:
        conn = psycopg2.connect(
            host="db",
            database="mydatabase",
            user="myuser",
            password="mypassword"
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return f"PostgreSQL version: {db_version}"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
