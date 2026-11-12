import sqlite3
from flask import Flask, request
 
app = Flask(__name__)
 
DB_PASSWORD = "admin123"
 
 
def get_db():
    conn = sqlite3.connect("taller.db")
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, username TEXT)")
    if conn.execute("SELECT COUNT(*) FROM users").fetchone()[0] == 0:
        conn.execute("INSERT INTO users VALUES (1, 'ana'), (2, 'luis'), (3, 'admin')")
        conn.commit()
    return conn
 
 
@app.route("/")
def inicio():
    return "App taller SAST"
 
 
# SQL Inyection
@app.route("/buscar")
def buscar():
    nombre = request.args.get("nombre", "")
    cur = get_db().execute("SELECT * FROM users WHERE username = '" + nombre + "'")
    return str(cur.fetchall())
 
 
# XSS
@app.route("/saludo")
def saludo():
    nombre = request.args.get("nombre", "")
    return "<h1>Hola " + nombre + "</h1>"
 
 
# Debug activo
if __name__ == "__main__":
    app.run(debug=True)
