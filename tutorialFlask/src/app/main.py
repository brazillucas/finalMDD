import pickle

from flask import Flask, render_template, request

app = Flask(__name__)

modelo = pickle.load(open('tutorialFlask/models/modelo.pkl','rb'))

@app.route('/')
def home():
    return render_template('form.html',titulo="Previsão")
 
@app.route('/soma/<int:valor>')
def soma(valor):
    return "Resultado: {}".format(valor+5)

# Criando a rota GET para o modelo
@app.route('/predicao/<float:v1>/<float:v2>/<float:v3>/<float:v4>')
def predicao(v1,v2,v3,v4):
    resultado = modelo.predict([[v1,v2,v3,v4]])
    return "Classe: {}".format(resultado)

# criar uma chamada com método POST
@app.route('/predicao2', methods=['POST'])
def predicao2():
    dados = request.get_json()
    colunas = ['sepal Length (cm)', 'sepal Width (cm)', 'petal Length (cm)', 'petal Width (cm)']
    dados_input = [dados[col] for col in colunas]
    resultado = modelo.predict([dados_input])
    return "Classe: {}".format(resultado)

# Criar rota para o formulário
@app.route('/predicaoform', methods=['POST'])
def form():
    sepall = request.form['sepall']    
    sepalw = request.form['sepalw']
    petall = request.form['petall']
    petalw = request.form['petalw']
    result = modelo.predict([[sepall,sepalw,petall,petalw]])
    if result[0] == 0:
        resultado = "Iris Setosa"
    elif result[0] == 1:
        resultado = "Iris Versicolor"
    else:
        resultado = "Iris Virginica"
    return render_template('resultado.html', titulo="Previsão", resultado=resultado)

app.run(debug=True)