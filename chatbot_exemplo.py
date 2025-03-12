from flask import Flask, render_template, request
import random
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

LABELS = ['Instalação e Implantação do Prontuário Eletrônico do e-SUS APS','Configuração e Administração do e-SUS APS','Manutenção e Versões', 'Erros do Sistema', 'Atualizações', 'e-SUS Território', 'e-SUS Atividade Coletiva', 'Gestão e-SUS APS', 'e-SUS Vacinação', 'e-SUS AD (Atenção Domiciliar)', 'e-Gestor e SISAB', 'Outros Sistemas (CNES, SISVAN...)', 'Cadastro de Pessoas (cidadão)', 'Processo de Atendimento', 'Agente Comunitário de Saúde (ACS) e Agente de Combate às Endemias (ACE)', 'Gestão de Recursos, Serviços ou Relatórios', 'Gestão de Recursos, Serviços ou Relatórios', 'Preenchimento da Coleta de Dados Simplificada (CDS)', 'Vacina']

MODEL_PATH = "app/model.pkl"
VECTORIZER_PATH = "app/vectorizer.pkl"

# se há um modelo treinado salvo
if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
    with open(MODEL_PATH, 'rb') as model_file, open(VECTORIZER_PATH, 'rb') as vectorizer_file:
        clf = pickle.load(model_file)
        vectorizer = pickle.load(vectorizer_file)
else:
    clf = None
    vectorizer = None


def classify_text(text):
    """Classifica o texto utilizando o modelo treinado ou retorna opções aleatórias."""
    if clf and vectorizer:
        text_tfidf = vectorizer.transform([text])
        y_prob = clf.predict_proba(text_tfidf)[0]
        sorted_labels = sorted(zip(LABELS, y_prob), key=lambda x: x[1], reverse=True)
        return [label for label, prob in sorted_labels[:3]]
    return random.sample(LABELS, 3)  # rótulos aleatórios se não houver modelo


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_text = request.form['user_text']
        options = classify_text(user_text)
        return render_template('choose.html', user_text=user_text, options=options)
    return render_template('index.html')


@app.route('/finalize', methods=['POST'])
def finalize():
    classification = request.form['classification']
    if classification == "Nenhuma das Opções Apresentadas":
        return render_template('result.html', classification="Aguarde auxílio de um de nossos atendentes.")
    return render_template('result.html', classification=classification)


if __name__ == '__main__':
    app.run(debug=True)
