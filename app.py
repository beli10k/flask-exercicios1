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

    # Exercício 6 — Página HTML via template
@app.route('/pagina')
def pagina():
    return render_template('pagina.html'), 200

# Exercício 7 — Busca em lista
@app.route('/buscar/<item>')
def buscar(item):
    lista = ['banana', 'maçã', 'uva', 'morango']
    encontrado = False

    for elemento in lista:
        if elemento == item:
            encontrado = True
            break

    if encontrado:
        return f"Item '{item}' encontrado na lista!", 200
    else:
        return f"Item '{item}' não encontrado.", 200


if __name__ == '__main__':
    app.run(debug=True)