from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

ARQUIVO_EXCEL = "confirmacoes.xlsx"

def salvar_dados(nome, telefone):
    dados = {"Nome": [nome], "Telefone": [telefone], "Presença Confirmada": ["Sim"]}
    df_novo = pd.DataFrame(dados)
    
    if os.path.exists(ARQUIVO_EXCEL):
        df_existente = pd.read_excel(ARQUIVO_EXCEL)
        df_final = pd.concat([df_existente, df_novo], ignore_index=True)
    else:
        df_final = df_novo
    
    df_final.to_excel(ARQUIVO_EXCEL, index=False)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form["nome"]
        telefone = request.form["telefone"]
        try:
            salvar_dados(nome, telefone)
        except Exception as e:
            return f"Ocorreu um erro ao salvar os dados: {e}", 500
        return render_template("confirmacao.html")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)

import os

@app.route("/")
def index():
    if os.path.exists("templates/index.html"):
        print("Arquivo index.html encontrado!")
    else:
        print("Arquivo index.html NÃO encontrado!")
    return render_template("index.html")



