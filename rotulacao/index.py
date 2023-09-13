from PIL import Image

def rotular_imagem(imagem_binaria):
    largura, altura = imagem_binaria.size
    print(largura, altura)
    rotulo = 0
    imagem_rotulada = Image.new('L', (largura, altura), 0)
    for y in range(altura):
        for x in range(largura):
            pixel = imagem_binaria.getpixel((x, y))
            # Se p = 0, move-se para o próximo pixel
            if pixel != 0:
                # Se p = 1, analisa-se s e r
                vizinho_esquerda = imagem_rotulada.getpixel((x-1, y)) if x > 0 else 0
                vizinho_acima = imagem_rotulada.getpixel((x, y-1)) if y > 0 else 0
                if vizinho_esquerda == 0 and vizinho_acima == 0:
                    # Se r e s forem 0, assinala-se um novo label para p e anota-se que esse label já foi usado
                    rotulo += 1
                    imagem_rotulada.putpixel((x, y), rotulo)
                elif vizinho_esquerda != 0 and vizinho_acima != 0:
                    # Se r ou s for 1, assinala-se label correspondente a p
                    imagem_rotulada.putpixel((x, y), min(vizinho_esquerda, vizinho_acima))
                else:
                    # Se r ou s for 1, assinala-se label correspondente a p
                    imagem_rotulada.putpixel((x, y), max(vizinho_esquerda, vizinho_acima))
    return imagem_rotulada



# Transformando a imageme em uma matrix
arquivo_imagem = Image.open('../imagens/img-03.jpg')
imagem_cinza = arquivo_imagem.convert('L')

# Defina o limite (threshold)
limite = 128

# Crie uma imagem binária com base no limite
imagem_binaria = imagem_cinza.point(lambda p: p > limite and 255)

resultado_interpolacao = rotular_imagem(imagem_binaria)
resultado_interpolacao.save('imagem_binaria.jpg')