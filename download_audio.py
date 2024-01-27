# download_audio.py
from pytube import YouTube

def baixar_apenas_audio(url, local):
    try:
        video = YouTube(url)
        stream = video.streams.filter(only_audio=True).first()

        # Baixa o arquivo de áudio
        stream.download(output_path=local)

        return True, 'Áudio baixado com sucesso'

    except Exception as e:
        return False, f'Erro: {str(e)}'
