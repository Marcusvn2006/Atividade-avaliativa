from flask import Flask, render_template, request   

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def pagina_inicial():
    error =[]
    resultadoIMC = 0
    mode = None
    resultado = None
    if request.method == 'POST':
        try:
            peso = float(request.form['peso'])
            if peso < 0 or peso > 300:
                error.append("Coloque um peso valido para uma pessoa")
        except:
            error.append("Coloque algum peso")
        try:
            altura = float(request.form['altura'])
            if altura < 0.5 or altura > 2.5:
             error.append("Coloque uma altura valida")
        except:
            error.append("Coloque algum altura")
        if not error:
            resultadoIMC = peso /  (altura * altura )    
        if resultadoIMC < 18.5:
            mode = 'primary'
            resultado = "abaixo do peso"
        elif resultadoIMC <18.5 or resultadoIMC > 25:
            mode = "success"
            resultado = " Peso normal"

        elif resultadoIMC <25 or resultadoIMC > 30:

            resultado = "Sobrepeso"
            mode = "warning"
        elif resultadoIMC <30:
            resultado = " Obesidade"
            mode = "danger"


    return render_template('index.html', error = error, resultadoIMC = resultadoIMC, mode = mode, resultado = resultado)


@app.route('/equipe')
def equipe():
    return render_template('equipe.html')
    
if __name__ == '__main__':
    app.run(debug=True)