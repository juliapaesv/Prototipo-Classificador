from flask import Flask, render_template, request

app = Flask(__name__)

# entrada: texto inserido pelo usuário
# saída: classificação (string) ou opções (lista de strings)
def classify_text(text):
    # chamar o LLM e processar o texto
    # exemplo de retorno:
    # return "Rótulo XYZ", None  # caso o modelo tenha certeza
    # return None, ["Rótulo A", "Rótulo B"]  # caso o modelo precise de ajuda do usuário
    pass

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_text = request.form['user_text']
        classification, options = classify_text(user_text)

        # se o modelo tem uma classificação certa
        if classification:
            return render_template('result.html', classification=classification)
        # se o modelo precisar de ajuda do usuário
        else:
            return render_template('choose.html', user_text=user_text, options=options)

    # página inicial com formulário
    return render_template('index.html')

@app.route('/finalize', methods=['POST'])
def finalize():
    classification = request.form['classification']
    
    return render_template('result.html', classification=classification)

if __name__ == '__main__':
    app.run(debug=True)

# onde modificar:
# 1. função `classify_text`: substituir a lógica interna pelo LlaMA aqui
# 2. `render_template('choose.html')`: modificar as opções retornadas pelo LlaMA aqui
# 3. HTML `index.html`, `choose.html`, `result.html` devem ser ajustados se novos rótulos forem adicionados :)
