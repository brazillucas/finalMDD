import pickle

from flask import Flask, render_template, request

app = Flask(__name__)

# Modelo de classificação Arvore de Decisão
# modelo = pickle.load(open('trabalhofinalmd/models/modeloCervicalC.pkl','rb'))

# Modelo de classificação Regressão Logística
modelo = pickle.load(open('trabalhofinalmd/models/modeloCervicalC.pkl','rb'))

@app.route('/')
def home():
    return render_template('form.html',titulo="Previsão")
 
@app.route('/soma/<int:valor>')
def soma(valor):
    return "Resultado: {}".format(valor+5)

# Criando a rota GET para o modelo
@app.route('/predicao/<int:v1>/<int:v2>/<int:v3>/<int:v4>/<int:v5>/<int:v6>/<int:v7>/<int:v8>/<int:v9>/<int:v10>/<int:v11>')
def predicao(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11,):
    resultado = modelo.predict([[v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11]])
    return "Classe: {}".format(resultado)

# criar uma chamada com método POST
@app.route('/predicao2', methods=['POST'])
def predicao2():
    dados = request.get_json()
    colunas = ["idade","num_sex_parc",
"num_gravidez","fumante","fumante_anos","cntrcep_hormo","cntrcep_hormo_anos","diu","diu_anos","ists","num_ists"]
    dados_input = [dados[col] for col in colunas]
    print(dados_input)
    resultado = modelo.predict([dados_input])
    return "Classe: {}".format(resultado)

# Criar rota para o formulário com os seguintes campos:
    # idade
    # num_sex_parc
    # num_gravidez
    # fumante
    # fumante_anos
    # cntrcep_hormo
    # cntrcep_hormo_anos
    # DIU
    # DIU_anos
    # ISTs
    # num_ISTs

@app.route('/predicaoform', methods=['POST'])
def form():
    idade = request.form['idade']
    num_sex_parc =  request.form['num_sex_parc']
    num_gravidez =  request.form['num_gravidez']
    fumante =       request.form['fumante']
    fumante_anos =  request.form['fumante_anos']
    cntrcep_hormo = request.form['cntrcep_hormo']
    cntrcep_hormo_anos = request.form['cntrcep_hormo_anos']
    diu = request.form['diu']
    diu_anos = request.form['diu_anos']
    ists = request.form['ists']
    num_ists = request.form['num_ists']

    result = modelo.predict([[idade, num_sex_parc, num_gravidez, fumante, fumante_anos, cntrcep_hormo, cntrcep_hormo_anos, diu, diu_anos, ists, num_ists]])

    if result[0] == 1:
        resultado = "Positivo"
    else:
        resultado = "Negativo"

    return render_template('resultado.html', titulo="Previsão", resultado=resultado)

app.run(debug=True)