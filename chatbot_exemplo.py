from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# entrada: texto inserido pelo usuário
# saída: classificação (string) ou opções (lista de strings)
def classify_text(text):
    if "bom" in text.lower():
        return "Positivo", None
    elif "ruim" in text.lower():
        return "Negativo", None
    else:
        return None, ["Positivo", "Negativo"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_text = request.form['user_text']
        classification, options = classify_text(user_text)
        
        if classification:
            return render_template('result.html', classification=classification)
        else:
            return render_template('choose.html', user_text=user_text, options=options)
    
    return render_template('index.html')

@app.route('/finalize', methods=['POST'])
def finalize():
    classification = request.form['classification']
    return render_template('result.html', classification=classification)

if __name__ == '__main__':
    app.run(debug=True)
