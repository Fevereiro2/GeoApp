import random
import asyncio
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER

def carregar_paises_e_capitais(nome_ficheiro):
    """Carrega a lista de países e capitais a partir de um ficheiro."""
    paises_capitais = {}
    try:
        with open(nome_ficheiro, "r", encoding="utf-8") as f:
            for linha in f:
                pais, capital = linha.strip().split(";")
                paises_capitais[pais] = capital
    except FileNotFoundError:
        print("Ficheiro não encontrado. Um novo ficheiro será criado ao adicionar países.")
    return paises_capitais

def guardar_paises_e_capitais(nome_ficheiro, paises_capitais):
    """Guarda a lista de países e capitais num ficheiro."""
    with open(nome_ficheiro, "w", encoding="utf-8") as f:
        for pais, capital in paises_capitais.items():
            f.write(f"{pais};{capital}\n")

class GeoQuizApp(toga.App):
    def __init__(self, paises_capitais):
        super().__init__("Jogo de Geografia", "org.example.geografia")
        self.paises_capitais = paises_capitais

    def startup(self):
        main_window = toga.MainWindow(title="Jogo de Geografia")
        self.main_window = main_window

        # Botões
        iniciar_button = toga.Button("Iniciar Jogo", on_press=self.iniciar_jogo, style=Pack(padding=10))
        adicionar_button = toga.Button("Adicionar País", on_press=self.adicionar_pais, style=Pack(padding=10))
        geoguesser_button = toga.Button

        self.resultado_label = toga.Label("Bem-vindo ao Jogo de Geografia!", style=Pack(padding=10))

        # Layout
        main_window.content = toga.Box(
            children=[self.resultado_label, iniciar_button, adicionar_button],
            style=Pack(direction=COLUMN, alignment=CENTER, padding=20)
        )
        main_window.show()

    async def iniciar_jogo(self, widget):
        if not self.paises_capitais:
            self.resultado_label.text = "Adicione países antes de jogar!"
            return

        perguntas = random.sample(list(self.paises_capitais.items()), min(5, len(self.paises_capitais)))
        acertos = 0

        for pais, capital_certa in perguntas:
            resposta = await self.dialog_input(f"Qual é a capital de {pais}?")
            if resposta and resposta.lower() == capital_certa.lower():
                acertos += 1

        self.resultado_label.text = f"Você acertou {acertos} de {len(perguntas)} perguntas."

    async def adicionar_pais(self, widget):
        pais = await self.dialog_input("Digite o nome do país:")
        if not pais or pais in self.paises_capitais:
            self.resultado_label.text = "País já existente ou entrada inválida."
            return

        capital = await self.dialog_input(f"Digite a capital de {pais}:")
        if not capital:
            self.resultado_label.text = "Entrada inválida para a capital."
            return

        self.paises_capitais[pais] = capital
        guardar_paises_e_capitais("paises_capitais.txt", self.paises_capitais)
        self.resultado_label.text = f"{pais} e sua capital {capital} foram adicionados!"

    async def dialog_input(self, message):
        """Exibe um diálogo de entrada de texto."""
        dialog = toga.TextInput(style=Pack(padding=5))
        response = []

        def confirm(widget):
            response.append(dialog.value)
            input_window.close()

        input_window = toga.Window(title="Entrada")
        input_window.content = toga.Box(
            children=[
                toga.Label(message, style=Pack(padding=(0, 0, 10, 0))),
                dialog,
                toga.Button("OK", on_press=confirm, style=Pack(padding=5))
            ],
            style=Pack(direction=COLUMN, alignment=CENTER, padding=10)
        )
        input_window.show()

        while not response:
            await asyncio.sleep(0.1)

        return response[0] if response else None

def menu():
    nome_ficheiro = "paises_capitais.txt"
    paises_capitais = carregar_paises_e_capitais(nome_ficheiro)

    if __name__ == "__main__":
        import sys
        if sys.platform == "win32":
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

        app = GeoQuizApp(paises_capitais)
        app.main_loop()

if __name__ == "__main__":
    menu()
