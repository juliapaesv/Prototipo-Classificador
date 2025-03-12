from flask import Flask, render_template, request
import random

app = Flask(__name__)

# entrada: texto inserido pelo usuário
# saída: classificação (string) ou opções (lista de strings)

#rótulos
LABELS = ['Instalação e Implantação do Prontuário Eletrônico do e-SUS APS','Configuração e Administração do e-SUS APS','Manutenção e Versões', 'Erros do Sistema', 'Atualizações', 'e-SUS Território', 'e-SUS Atividade Coletiva', 'Gestão e-SUS APS', 'e-SUS Vacinação', 'e-SUS AD (Atenção Domiciliar)', 'e-Gestor e SISAB', 'Outros Sistemas (CNES, SISVAN...)', 'Cadastro de Pessoas (cidadão)', 'Processo de Atendimento', 'Agente Comunitário de Saúde (ACS) e Agente de Combate às Endemias (ACE)', 'Gestão de Recursos, Serviços ou Relatórios', 'Gestão de Recursos, Serviços ou Relatórios', 'Preenchimento da Coleta de Dados Simplificada (CDS)', 'Vacina']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_text = request.form['user_text']
        options = random.sample(LABELS, 3)  # seleciona 3 rótulos aleatórios
        return render_template('choose.html', user_text=user_text, options=options)
    
    return render_template('index.html')

@app.route('/finalize', methods=['POST'])
def finalize():
    classification = request.form['classification']
    if classification == "Nenhuma das Opções Apresentadas":
        return render_template('result.html', classification="Aguarde auxílio de um de nossos atendentes")
    return render_template('result.html', classification=classification)

if __name__ == '__main__':
    app.run(debug=True)