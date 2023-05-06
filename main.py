from flask import Flask, render_template, request, redirect, url_for
import json
import requests as rs

app = Flask(__name__,template_folder='template')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cadastro')
def form():
    return render_template('form.html')

@app.route('/test_cad')
def test_cad():
    return render_template('test_cad.html')


@app.route('/submit', methods=['POST'])
def submit():

    # get form data
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    username = request.form['username']
    url = f"https://todolist-api.edsonmelo.com.br/api/user/new/"
    # Cabeçalho da requisição informando o que deverá ser enviado e qual o formato
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    
    # send data to external API
    data = {
        'name': name,
        'email': email,
        'password': password,
        'username' : username
    }
    response = rs.post(url, data=json.dumps(data), headers=headers)
    dicionario= response.text
    specific_key = 'message'
    if isinstance(dicionario, dict) and specific_key in dicionario and isinstance(dicionario[specific_key], str) and dicionario[specific_key] != 'User Successfully Added':
        # Gera uma mensagem de erro com o valor retornado pela API ou conexão
        return redirect(url_for('falha_cadastro'))
    else:
        # Handle other cases or continue with the rest of the code
        return redirect(url_for('login'))

@app.route('/falha_cadastro')
def falha_cadastro():
    return render_template('falha_cadastro.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/falha_login')
def falha_login():
    return render_template('falha_login.html')

@app.route('/principal', methods=['POST'])
def principal():
# get form data
    password = request.form['password']
    username = request.form['username']
    url = f"https://todolist-api.edsonmelo.com.br/api/user/login/"
    # Cabeçalho da requisição informando o que deverá ser enviado e qual o formato
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    # send data to external API
    data_log = {

        'password': password,
        'username' : username
    }
    dados = rs.post(url, data=json.dumps(data_log), headers=headers)
    dictlogin = json.loads(dados.text)

    if 'token' in dictlogin:
        # Gera uma mensagem de erro com o valor retornado pela API ou conexão
        user_name = dictlogin.get('name')
        token  = dictlogin.get('token')
        return render_template('principal.html', username = user_name, token = token)
        
    else:
        return redirect(url_for('falha_login'))



if __name__ == '__main__':
    app.run(debug=True)