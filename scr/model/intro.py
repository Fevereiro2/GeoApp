import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER
import asyncio

class IntroWindow:
    def __init__(self, app, on_intro_complete):
        """
        Inicializa a janela de introdução.
        :param app: Instância do aplicativo Toga.
        :param on_intro_complete: Função de callback após a introdução.
        """
        self.app = app
        self.on_intro_complete = on_intro_complete
        self.intro_window = None

    async def show_async(self):
        """
        Mostra a janela de introdução de forma assíncrona.
        """
        # Criando a janela de introdução
        self.intro_window = toga.Window(title="Carregando...")
        self.app.main_window = self.intro_window

        # Elementos da introdução
        gif_image = toga.Image("../img/certificate.gif")  # Substitua pelo caminho do seu GIF
        gif_view = toga.ImageView(gif_image, style=Pack(padding=10))
        message = toga.Label("Carregando Jogo de Geografia...", style=Pack(padding=10))

        self.intro_window.content = toga.Box(
            children=[gif_view, message],
            style=Pack(direction=COLUMN, alignment=CENTER, padding=20)
        )
        self.intro_window.show()

        # Aguardar o tempo de exibição da introdução
        await self.close_after_delay()

    async def close_after_delay(self):
        """
        Aguarda alguns segundos antes de fechar a introdução e iniciar o jogo.
        """
        await asyncio.sleep(5)  # Exibição de 5 segundos (ajuste conforme necessário)
        self.intro_window.close()  # Fecha a janela de introdução
        self.on_intro_complete()  # Chama a função de callback para iniciar o jogo
