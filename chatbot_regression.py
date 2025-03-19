from flask import Flask, render_template, request
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

MODEL_PATH = "model.pkl"
VECTORIZER_PATH = "vectorizer.pkl"

# rótulos
LABELS_MAPPING = {
    0: "Instalação e Implantação do Prontuário Eletrônico e-SUS APS",
    1: "Manutenção do Software e Versões",
    2: "Cadastro de Pessoas (Cidadão)",
    3: "Processo de Atendimento",
    4: "Vacina",
    5: "Agente Comunitário de Saúde (ACS) e Agente de Combate às Endemias (ACE)",
    6: "Aplicativos e-SUS",
    7: "Cadastro de Profissional",
    8: "Preenchimento da Coleta de Dados Simplificada (CDS)",
    9: "Gestão de Recursos, Serviços ou Relatórios",
    10: "Demais Sistemas Relacionados à APS"
}

# modelo treinado e vetorizar
if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
    with open(MODEL_PATH, 'rb') as model_file, open(VECTORIZER_PATH, 'rb') as vectorizer_file:
        clf = pickle.load(model_file)
        vectorizer = pickle.load(vectorizer_file)
        LABELS = [LABELS_MAPPING[label] for label in clf.classes_]
else:
    raise FileNotFoundError("Arquivos do modelo e do vetorizar não encontrados.")


def classify_text(text):
    """Classifica o texto utilizando regressão logística e retorna as 3 categorias mais prováveis."""
    text_tfidf = vectorizer.transform([text])
    y_prob = clf.predict_proba(text_tfidf)[0]  # probabilidades para cada classe
    sorted_labels = sorted(zip(clf.classes_, y_prob), key=lambda x: x[1], reverse=True)
    return [LABELS_MAPPING[label] for label, prob in sorted_labels[:3]]  # retorna as 3 melhores opções


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_text = request.form['user_text']
        options = classify_text(user_text)  # regressão logística para classificar o texto
        return render_template('choose.html', user_text=user_text, options=options)
    
    return render_template('index.html')


@app.route('/finalize', methods=['POST'])
def finalize():
    classification = request.form['classification']
    if classification == "Nenhuma das Opções Apresentadas":
        return render_template('result.html', classification="Aguarde auxílio de um de nossos atendentes")
    return render_template('result.html', classification=classification)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)