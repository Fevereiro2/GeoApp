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

        # Criação da barra personalizada
        self.custom_bar = self.create_custom_bar()

        # Obter o layout principal do jogo
        main_content = self.show_main_window()

        # Combinar barra personalizada e conteúdo principal
        layout = toga.Box(children=[self.custom_bar, main_content], style=Pack(direction=COLUMN))
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
        location_button = toga.Button(
            "GeoQuiz 🗺️",
            on_press=self.geoquizz,
            style=Pack(padding=(10, 20), font_size=16),
        )

        # Rótulo de boas-vindas
        self.resultado_label = toga.Label(
            "Bem-vindo ao GeoQuiz App! 🌟",
            style=Pack(padding=20, font_size=18, text_align="center"),
        )

        # Layout principal
        layout_box = toga.Box(
            children=[self.resultado_label, iniciar_button, adicionar_button, location_button],
            style=Pack(direction=COLUMN, alignment="center", padding=20),
        )
        return layout_box

    def create_custom_bar(self):
        """Cria uma barra de título personalizada."""
        close_button = toga.Button("❌", on_press=self.close_app, style=Pack(padding=5, width=30))
        minimize_button = toga.Button("➖", on_press=self.minimize_app, style=Pack(padding=5, width=30))
        maximize_button = toga.Button("🗖", on_press=self.maximize_app, style=Pack(padding=5, width=30))

        bar = toga.Box(
            children=[toga.Label("GeoQuiz App", style=Pack(padding=10)), minimize_button, maximize_button, close_button],
            style=Pack(direction=ROW, padding=5, alignment=RIGHT),
        )
        return bar

    def close_app(self, widget):
        """Fecha o aplicativo."""
        self.main_window.close()

    def minimize_app(self, widget):
        """Simula a minimização do aplicativo."""
        # Oculta a janela principal, simulando a minimização
        self.main_window

    def maximize_app(self, widget):
        """Alterna entre maximizar e restaurar a janela."""
        # Armazena o estado atual da janela para alternar entre maximizar e restaurar
        if hasattr(self, "is_maximized") and self.is_maximized:
            # Restaurar o tamanho original
            self.main_window.size = (400, 400)  # Defina o tamanho original
            self.is_maximized = False
        else:
            # Maximizar
            self.main_window.size = (800, 600)  # Defina um tamanho maior para simular maximização
            self.is_maximized = True


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
