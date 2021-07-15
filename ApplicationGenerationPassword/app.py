# import time
import string

from flask import Flask, render_template, request
from random import choice
# from itertools import combinations_with_replacement

string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits  # 0123456789
string.punctuation  # <=>?@[\]^_`{|}~.


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    variavel = "Tela: Gerando Senha"

    if request.method == 'GET':
        # Render the page
        return render_template("index.html", variavel=variavel)
    else:
        tamanho = 9
        # Criação de Função para Geração de Senha:
        valores = string.ascii_letters + string.digits + string.punctuation
        senha = ''
        for i in range(tamanho):
            senha += choice(valores)
        # senha = request.access_route

        return render_template("gerada_senha.html", senha=senha)


def password(senha):
    return render_template("gerada_senha.html", senha=senha)
    # return abort(404, "User not found")


@app.route('/<string:nome>')
def error(nome):
    variavel = f'Pagina ({nome}) não existe'
    return render_template("error.html", variavel=variavel)


app.add_url_rule('/password/<senha>/', view_func=password, endpoint='password')

if __name__ == '__main__':
    # Run the app server on localhost:4449

    # app.run('localhost', 4449)
    app.run(use_reloader=True)
