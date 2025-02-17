# Protótipo-Classificador

## Comece por aqui
### chatbot_exemplo.py
Este arquivo possui um exemplo do protótipo que criei, rode ele primeiro para ter uma ideia geral do que ele faz:

python3 chatbot_exemplo.py

O código exemplo cria um site Flask que recebe um texto e tenta classificá-lo automaticamente como "Positivo" ou "Negativo", usando uma busca por palavra muito simples: se a palabra "bom" está presente, é positivo, se "mal" está, negativo. Se a classificação for incerta, o usuário pode escolher entre as opções sugeridas.

Agora o arquivo _chatbot.py_ fará mais sentido: ele é o esqueleto para o protótipo real que usa o LlaMA. As partes a serem modificadas estão explicitadas no próprio arquivo :).

## Protótipo
### chatbot.py
Esqueleto a ser completado com a lógica do classificador.

### templates
Pasta contendo os .htmls, neles, as modificações mais relevantes são:
1. _choose.html_: rótulos dinâmicos a serem implementados junto com a lógica de retorno do LlaMA, ajustando o loop {% for option in options %} para isso;
2. _result.html_: talvez mostrar também a confiança do modelo na classificação e adicionar um botão de "Classificar outro texto.". A função render_template() no código Python é a que envia dados (classification, options, etc.) para os HTMLs. Ela pode ser ajustada para retornar outras coisas, por exemplo, score, explanation etc.