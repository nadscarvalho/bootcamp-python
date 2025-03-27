contatos = {"nadine@gmail.com": {"nome": "Nadine", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["nadine@gmail.com"] = {"nome": "Nads"}

print(contatos["nadine@gmail.com"])

print(copia["nadine@gmail.com"])