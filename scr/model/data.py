# data.py
import os  # Adicionando a importação do módulo os

def carregar_paises_e_capitais(nome_ficheiro):
    """Carrega a lista de países e capitais a partir de um ficheiro."""
    paises_capitais = {}
    caminho_arquivo = os.path.join(os.getcwd(), nome_ficheiro)  # Usando o diretório atual
    print(f"Carregando o arquivo de {caminho_arquivo}")  # Verifique o caminho
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                pais, capital = linha.strip().split(";")
                paises_capitais[pais] = capital
    except FileNotFoundError:
        print(f"Ficheiro {nome_ficheiro} não encontrado. Um novo ficheiro será criado ao adicionar países.")
    return paises_capitais

def guardar_paises_e_capitais(nome_ficheiro, paises_capitais):
    """Guarda a lista de países e capitais num ficheiro."""
    caminho_arquivo = os.path.join(os.getcwd(), nome_ficheiro)  # Usando o diretório atual
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        for pais, capital in paises_capitais.items():
            f.write(f"{pais};{capital}\n")
