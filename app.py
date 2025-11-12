from flask import Flask, redirect, render_template

app = Flask(__name__)

# -------------------------------------------------------
# Exercício 1 — Página inicial
@app.route('/')
def index():
    return '<h1>Hello, Flask !!</h1>', 200


# Exercício 2 — Versão do app
@app.route('/versao')
def versao():
    versao = "1.1.0"
    return f"App v{versao}", 200
