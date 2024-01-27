# tkinter_ui.py

from tkinter import Tk, Label, Entry, Button, filedialog
from download_audio import baixar_apenas_audio

def interface():
    global entrada_url, label_status
    janela = Tk()
    janela.title("Baixar Áudio do Youtube")

    label_instrucao = Label(janela, text='Link do Vídeo:')
    label_instrucao.pack()

    entrada_url = Entry(janela, width=50)
    entrada_url.pack()

    botao_escolher_destino = Button(janela, text='Escolher Destino', command=escolher_destino)
    botao_escolher_destino.pack()

    botao_confirmar = Button(janela, text='Confirmar', command=iniciar_download)
    botao_confirmar.pack()

    label_status = Label(janela, text="")
    label_status.pack()

    janela.mainloop()

def escolher_destino():
    global label_status
    caminho_destino = filedialog.askdirectory()
    label_status["text"] = f"Destino escolhido: {caminho_destino}"

def iniciar_download():
    global entrada_url, label_status
    caminho_destino_escolhido = label_status["text"].replace("Destino escolhido: ", "")
    url_do_video = entrada_url.get()

    # Se nenhum destino foi escolhido, use o diretório atual como destino
    if not caminho_destino_escolhido:
        caminho_destino_escolhido = "."

    sucesso, mensagem = baixar_apenas_audio(url_do_video, caminho_destino_escolhido)

    if sucesso:
        label_status["text"] = mensagem
    else:
        label_status["text"] = mensagem
