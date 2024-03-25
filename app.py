from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/verificacao_covid', methods=['GET'])
def verificacao_covid():
    return render_template('verificacao_covid.html')

@app.route('/verificar_covid', methods=['POST'])
def verificar_covid():
    tosse = request.form['tosse']
    febre = request.form['febre']
    falta_ar = request.form['falta_ar']

    # Lógica de verificação de COVID-19
    # Aqui você pode adicionar a lógica para analisar os sintomas e retornar uma mensagem adequada

    return render_template('resultado_covid.html', tosse=tosse, febre=febre, falta_ar=falta_ar)

if __name__ == '__main__':
    app.run(debug=True)
