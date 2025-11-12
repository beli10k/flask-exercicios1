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

# Exercício 3 — Saudação por parâmetro
@app.route('/saudar/<nome>')
def saudar(nome):
    nome_formatado = nome.capitalize()
    return f"Olá, {nome_formatado}!", 200

# Exercício 4 — Quadrado de um número
@app.route('/quadrado/<int:n>')
def quadrado(n):
    resultado = n ** 2
    return f"{n}² = {resultado}", 200

# Exercício 5 — Redirect simples
@app.route('/home')
def home():
    return redirect('/'), 302