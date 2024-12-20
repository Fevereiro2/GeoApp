import sys
import asyncio
import toga
from toga.style import Pack
from toga.style.pack import ROW, RIGHT, COLUMN

from scr.model.game import GeoQuizApp
from scr.model.data import carregar_paises_e_capitais  # Função para carregar países e capitais


class GeoQuizAppWithCustomBar(GeoQuizApp):
    def __init__(self, paises_capitais):
        super().__init__(paises_capitais)

    def startup(self):
        """Inicia o aplicativo mostrando a janela principal com barra personalizada."""
        self.main_window = toga.MainWindow(title="GeoQuiz App", size=(400, 400), resizable=False)



        # Obter o layout principal do jogo
        main_content = self.show_main_window()

        # Combinar barra personalizada e conteúdo principal
        layout = toga.Box(children=[main_content], style=Pack(direction=COLUMN))
        self.main_window.content = layout
        self.main_window.show()

    def show_main_window(self):
        """Retorna o layout principal do jogo."""
        # Botões principais
        iniciar_button = toga.Button(
            "Iniciar Jogo 🎮",
            on_press=self.iniciar_jogo,
            style=Pack(padding=(10, 20), font_size=16),
        )
        adicionar_button = toga.Button(
            "Adicionar País ➕",
            on_press=self.adicionar_pais,
            style=Pack(padding=(10, 20), font_size=16),
        )


        # Rótulo de boas-vindas
        self.resultado_label = toga.Label(
            "Bem-vindo ao GeoQuiz App! 🌟",
            style=Pack(padding=20, font_size=18, text_align="center"),
        )

        # Layout principal
        layout_box = toga.Box(
            children=[self.resultado_label, iniciar_button, adicionar_button],
            style=Pack(direction=COLUMN, alignment="center", padding=20),
        )
        return layout_box


def main():
    """Função principal para executar o aplicativo."""
    nome_ficheiro = "paises_capitais.txt"
    paises_capitais = carregar_paises_e_capitais(nome_ficheiro)

    # Configuração do event loop para Windows, se necessário
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # Inicialização do aplicativo
    app = GeoQuizAppWithCustomBar(paises_capitais)
    app.main_loop()


if __name__ == "__main__":
    main()
