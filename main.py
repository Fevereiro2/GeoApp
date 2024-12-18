# main.py
import sys
import os
import asyncio
from scr.model.game import GeoQuizApp
from scr.model.intro import IntroWindow  # Importação da introdução
from scr.model.data import carregar_paises_e_capitais

def menu():
    nome_ficheiro = "paises_capitais.txt"
    paises_capitais = carregar_paises_e_capitais(nome_ficheiro)

    if __name__ == "__main__":
        # Configuração do event loop para Windows, se necessário
        if sys.platform == "win32":
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


        # Criação da instância do GeoQuizApp
        app = GeoQuizApp(paises_capitais)

        # Chama o método startup que vai iniciar o aplicativo sem usar asyncio diretamente
        app.main_loop()

if __name__ == "__main__":
    menu()
