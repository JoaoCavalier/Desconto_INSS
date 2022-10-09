from flask import Flask, render_template, request, redirect, url_for
from desconto_inss import Calculadora

app = Flask(__name__)

app.secret_key = 'INSS'

class AnoeSalario:
    def __init__(self, salario, ano, resultado, valor_inss, aliq):
        self.salario = salario
        self.ano = ano
        self.resultado = resultado
        self.valor_inss = valor_inss
        self.aliq = aliq

lista = []

@app.route('/')
def home():
    return render_template('home.html', titulo='Calculadora INSS', AnoeSalario=lista)

@app.route('/tabela', methods=['POST', ])
def tabela():
    ano = request.form['ano']
    salario = request.form['salario']

    calc = Calculadora()
    resultado = calc.calcular(float(salario),int(ano))
    resultado = round(resultado or 0,2)

    valor_inss = (float(salario) - resultado)

    aliq = calc.aliq(float(salario), resultado)
    aliq = round(aliq, 2)


    ano_salario = AnoeSalario(salario, ano, resultado,valor_inss, aliq)
    lista.append(ano_salario)

    return redirect(url_for('home'))

app.run(debug=True)
