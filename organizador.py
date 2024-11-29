
import os
import shutil

def organizar_pasta(diretorio):
    tipos_arquivos = {
        "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
        "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
        "Vídeos": [".mp4", ".mkv", ".avi"],
        "Áudios": [".mp3", ".wav"],
        "Compactados": [".zip", ".rar"],
        "Outros": []
    }

    if not os.path.exists(diretorio):
        print("O diretório especificado não existe.")
        return

    for pasta in tipos_arquivos.keys():
        caminho_pasta = os.path.join(diretorio, pasta)
        if not os.path.exists(caminho_pasta):
            os.makedirs(caminho_pasta)

    for arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, arquivo)
        if os.path.isfile(caminho_arquivo):
            movido = False
            for pasta, extensoes in tipos_arquivos.items():
                if any(arquivo.lower().endswith(ext) for ext in extensoes):
                    shutil.move(caminho_arquivo, os.path.join(diretorio, pasta))
                    movido = True
                    break
            if not movido:
                shutil.move(caminho_arquivo, os.path.join(diretorio, "Outros"))

    print(f"Arquivos organizados no diretório: {diretorio}")

if __name__ == "__main__":
    caminho = input("Digite o caminho da pasta a ser organizada: ")
    organizar_pasta(caminho)
