from flask import Flask, render_template

app = Flask(__name__,template_folder='template')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cadastro')
def form():
    return render_template('form.html')

@app.route('/pos_cadastro')
def pos_cadastro():
    return render_template('pos_cadastro.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/principal')
def principal():
    return render_template('principal.html')


if __name__ == '__main__':
    app.run()