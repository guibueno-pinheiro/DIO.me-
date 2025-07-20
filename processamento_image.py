from PIL import Image

def abrir_imagem(caminho_arquivo):
    """
    Abre uma imagem e retorna o objeto PIL Image.
    """
    return Image.open(caminho_arquivo)

def salvar_imagem(imagem, caminho_arquivo):
    """
    Salva o objeto PIL Image em disco.
    """
    imagem.save(caminho_arquivo)

def aplicar_filtro_preto_branco(imagem):
    """
    Converte uma imagem para preto e branco (grayscale).
    """
    return imagem.convert('L')

def redimensionar_imagem(imagem, largura, altura):
    """
    Redimensiona a imagem para a largura e altura especificados.
    """
    return imagem.resize((largura, altura))

def main():
    caminho_entrada = "minha_foto.jpg"    # Altere para o caminho da sua imagem
    caminho_saida_pb = "minha_foto_pb.jpg"
    caminho_saida_redim = "minha_foto_redim.jpg"

    # Abrir imagem
    img = abrir_imagem(caminho_entrada)

    # Aplicar filtro preto e branco
    img_pb = aplicar_filtro_preto_branco(img)
    salvar_imagem(img_pb, caminho_saida_pb)
    print(f"Imagem salva em preto e branco: {caminho_saida_pb}")

    # Redimensionar imagem (exemplo 200x200)
    img_redim = redimensionar_imagem(img, 200, 200)
    salvar_imagem(img_redim, caminho_saida_redim)
    print(f"Imagem salva redimensionada para 200x200: {caminho_saida_redim}")

if __name__ == "__main__":
    main()
