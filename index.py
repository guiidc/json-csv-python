import csv
import json

with open('escrita3.csv', 'w') as file:
    writer = csv.writer(file)
    headers = ['nome', 'sobrenome', 'email']
    writer.writerow(headers)
    writer.writerow(['Guilherme', 'Da Costa', 'guilhermedc93@gmail.com'])

with open('escrita3.csv', 'r') as file:
    reader = csv.DictReader(file)
    convertido = [item for item in reader]
    with open('escrita3.json', 'w') as jsonFile:
      json.dump(convertido, jsonFile, indent=2)


"""
csv.read
gera um "array de arrays" onde cada linha está contida dentro de um array de string pertencente a um array maior

csv.DictReader
gera um array de dicionarios, onde os itens do cabeçalho viram a chave e o conteudo das linhas viram o valor

json.load
passa a estrutura json EXATA para um dicionario python

json.loads
a diferença dele pro load (sem s) é que gera uma estrutura exata de uma STRING json par um dicionario python
ex de string json "{"nome": "Guilherme", "sobrenome": "da Costa", "email": "guilherme@mail.com"}"
obs.: note que todo o json está dentro de uma string

json.dump
gera o arquivo json para poder salvarmos, lembrando que ele deve salvar no arquivo que está sendo aberto no OPEN

json.dumps
converte a estrutura python (lista, dictionary, para uma STRING json)
ex de string json "{"nome": "Guilherme", "sobrenome": "da Costa", "email": "guilherme@mail.com"}"

DICAS

ESCREVER NO CSV
para escrevermos no arquivo csv, devemos fazer uma lista com as strings dentro, iterar e usar o metodo writerow
para escrever cada linha
como usado na linha 7 ou 8
"""