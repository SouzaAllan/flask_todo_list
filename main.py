from flask import Flask, render_template, request
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

'''@app.route('/pos_cad')
def pos_cad():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    username = request.form['username']
    pay_load = {
    'username': '{}'.format(username),
    'password': '{}'.format(password),
    'email' : '{}'.format(email),
    'name' : '{}'.format(name)
    }
    recurso = 'user'    # Resources (veja na documentação)
    servico = 'new'   # Cada resource tem seu métodos para os seviços
    url = f"https://todolist-api.edsonmelo.com.br/api/{recurso}/{servico}/"
    # Cabeçalho da requisição informando o que deverá ser enviado e qual o formato
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    # Envio da requisição e armazenamento dos dados recebidos
    dados = rs.post(url, data=json.dumps(pay_load), headers=headers)
    # Aqui devem ser realizados os tratamentos no caso de ocorrerem erros
    try:
        # Converte os dados recebidos em em dicionário Python
        dicionario = json.loads(dados.text)

        if 'message' in dicionario:
            # Gera uma mensagem de erro com o valor retornado pela API ou conexão
            raise Exception(dicionario.get('message'))
            return render_template('falha_cadastro.html')
            
        else:
            # Mostra os dados retornados já convertidos
           url_login = f"https://todolist-api.edsonmelo.com.br/api/user/login/"
           pay_load_lg = {
            'username': '{}'.format(username),
            'password': '{}'.format(password)
            }
           headers_lg = {'Content-type': 'application/json', 'Accept': 'text/plain'}
           dados = rs.post(url_login, data=json.dumps(pay_load_lg), headers=headers_lg)
           return render_template('principal.html')

    except Exception as error:
       return render_template('falha_cadastro.html')

'''

@app.route('/submit', methods=['POST'])
def submit():

    # get form data
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    username = request.form['username']
    recurso = 'user'    # Resources (veja na documentação)
    servico = 'new'   # Cada resource tem seu métodos para os seviços
    url = f"https://todolist-api.edsonmelo.com.br/api/{recurso}/{servico}/"
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
    a= response.text
    #b= json.dumps(a)
    dicionario = a
    specific_key = 'message'
    if specific_key in dicionario and dicionario[specific_key] != 'User Successfully Added':
        # Gera uma mensagem de erro com o valor retornado pela API ou conexão
        return render_template('falha_cadastro.html')
        
        
    else:
        return render_template('principal.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/principal')
def principal():
    return render_template('principal.html')


if __name__ == '__main__':
    app.run()