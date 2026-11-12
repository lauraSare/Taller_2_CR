import os
import sqlite3
from flask import Flask, request, render_template_string
 
app = Flask(__name__)
 
# Contraseña desde variable de entorno
DB_PASSWORD = os.environ.get("DB_PASSWORD")
 
 
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
 
 
# Consulta por parametros
@app.route("/buscar")
def buscar():
    nombre = request.args.get("nombre", "")
    cur = get_db().execute("SELECT * FROM users WHERE username = ?", (nombre,))
    return str(cur.fetchall())
 
 
# Plantilla con autoescape
@app.route("/saludo")
def saludo():
    nombre = request.args.get("nombre", "")
    return render_template_string("<h1>Hola {{ nombre }}</h1>", nombre=nombre)
 
 
# Sin debug
def main():
    app.run()
 
 
if __name__ == "__main__":
    main()
