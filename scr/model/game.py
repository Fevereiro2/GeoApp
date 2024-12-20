import random
import asyncio
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER, JUSTIFY, ROW, RIGHT

from .data import carregar_paises_e_capitais, guardar_paises_e_capitais  # Importação relativa


class GeoQuizApp(toga.App):
    def __init__(self, paises_capitais):
        super().__init__("Jogo de Geografia", "org.example.geografia")
        self.paises_capitais = paises_capitais

    def startup(self):
        """Inicia o aplicativo mostrando a janela principal."""
        self.show_main_window()

    def show_main_window(self):
        """Exibe a janela principal do jogo."""
        self.main_window = toga.MainWindow(title="🌍 GeoQuiz App")

        # Botões principais
        iniciar_button = toga.Button(
            "Iniciar Jogo 🎮",
            on_press=self.iniciar_jogo,
            style=Pack(padding=(10, 0), font_size=16),
        )
        adicionar_button = toga.Button(
            "Adicionar País ➕",
            on_press=self.adicionar_pais,
            style=Pack(padding=(10, 0), font_size=16),
        )


        # Rótulo de boas-vindas
        self.resultado_label = toga.Label(
            "Bem-vindo ao GeoQuiz App! 🌟",
            style=Pack(padding=(20, 0), font_size=18, text_align=CENTER),
        )

        # Layout principal
        layout_box = toga.Box(
            children=[
                self.resultado_label,
                iniciar_button,
                adicionar_button,

            ],
            style=Pack(direction=COLUMN, alignment=CENTER, padding=20),
        )

        # Atribuindo conteúdo à janela principal
        self.main_window.content = layout_box
        self.main_window.show()


    def close(self):
        """Fecha a aplicação corretamente."""
        self.main_window.close()

    async def iniciar_jogo(self, widget):
        """Inicia o jogo de perguntas sobre capitais."""
        if not self.paises_capitais:
            self.resultado_label.text = "⚠️ Adicione países antes de jogar!"
            return

        perguntas = random.sample(list(self.paises_capitais.items()), min(5, len(self.paises_capitais)))
        acertos = 0

        for pais, capital_certa in perguntas:
            resposta = await self.dialog_input(f"Qual é a capital de {pais}?")
            if resposta and resposta.lower() == capital_certa.lower():
                acertos += 1

        self.resultado_label.text = f"🎉 Você acertou {acertos} de {len(perguntas)} perguntas!"

    async def adicionar_pais(self, widget):
        """Adiciona um novo país e sua capital."""
        pais = await self.dialog_input("🌍 Digite o nome do país:")
        if not pais or pais in self.paises_capitais:
            self.resultado_label.text = "⚠️ País já existente ou entrada inválida."
            return

        capital = await self.dialog_input(f"🏙️ Digite a capital de {pais}:")
        if not capital:
            self.resultado_label.text = "⚠️ Entrada inválida para a capital."
            return

        self.paises_capitais[pais] = capital
        guardar_paises_e_capitais("paises_capitais.txt", self.paises_capitais)
        self.resultado_label.text = f"✅ {pais} e sua capital {capital} foram adicionados!"

    async def dialog_input(self, message):
        """Mostra um diálogo de entrada de texto."""
        response = []

        def confirm(widget):
            response.append(dialog.value)
            input_window.close()

        # Layout do diálogo
        dialog = toga.TextInput(style=Pack(padding=(10, 0), width=200))
        input_window = toga.Window(title="📥 Entrada")
        input_window.content = toga.Box(
            children=[
                toga.Label(message, style=Pack(padding=(10, 0), font_size=14, text_align=JUSTIFY)),
                dialog,
                toga.Button("Confirmar ✅", on_press=confirm, style=Pack(padding=(10, 5))),
            ],
            style=Pack(direction=COLUMN, alignment=CENTER, padding=20),
        )
        input_window.show()

        while not response:
            await asyncio.sleep(0.1)

        return response[0] if response else None
