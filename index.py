import numpy as np
from PIL import Image


class Reducao():
    def vizinho_mais_proximo(self, imagem):
        # Pegando altura atual
        altura, largura = imagem.shape[:2]
        nova_altura, nova_largura = round(altura / 2), round(largura / 2)

        # Criando a matrix da nova imagem
        nova_imagem = np.zeros(
            (nova_altura, nova_largura, imagem.shape[2]), dtype=np.uint8)
        for y in range(nova_altura):
            for x in range(nova_largura):
                nova_imagem[y, x] = imagem[y * 2, x * 2]

        return nova_imagem

    def bilinear(self, imagem):
        # Pegando altura atual
        altura, largura = imagem.shape[:2]

        # calcula a nova altura e largura da imagem. As novas dimensões têm o dobro do tamanho da imagem original
        nova_altura, nova_largura = round(altura / 2), round(largura / 2)

        #np.zeros cria um array preenchido com zeros com a forma especificada. O tipo de dados é especificado como np.uint8, o que significa que os valores dos pixels variarão de 0 a 255
        nova_imagem = np.zeros((nova_altura, nova_largura, imagem.shape[2]), dtype=np.uint8)
        #iterar sobre cada pixel na nova imagem
        for y in range(nova_altura):
            for x in range(nova_largura):
                #calculam as coordenadas correspondentes na imagem original para cada pixel da nova imagem
                src_x = x * (largura / nova_largura)
                src_y = y * (altura / nova_altura)
                x1, y1 = int(np.floor(src_x)), int(np.floor(src_y))
                x2, y2 = min(x1 + 1, largura - 1), min(y1 + 1, altura - 1)
                dx = src_x - x1
                dy = src_y - y1
                pixel1 = imagem[y1, x1]
                pixel2 = imagem[y1, x2]
                pixel3 = imagem[y2, x1]
                pixel4 = imagem[y2, x2]
                nova_imagem[y, x] = (1 - dx) * (1 - dy) * pixel1 + dx * (1 - dy) * pixel2 + (1 - dx) * dy * pixel3 + dx * dy * pixel4
        return nova_imagem


class Ampliacao():

    def vizinho_mais_proximo(self, imagem):
        altura, largura = imagem.shape[:2]
        nova_altura, nova_largura = altura * 2, largura * 2

        nova_imagem = np.zeros(
            (nova_altura, nova_largura, imagem.shape[2]), dtype=np.uint8)

        for y in range(0, nova_altura, 2):
            for x in range(0, nova_largura, 2):
                pixel = imagem[y // 2, x // 2]
                nova_imagem[y, x] = pixel
                nova_imagem[y + 1, x] = pixel
                nova_imagem[y, x + 1] = pixel
                nova_imagem[y + 1, x + 1] = pixel

        return nova_imagem

    def bilinear(self, imagem):
        altura, largura = imagem.shape[:2]
        nova_altura, nova_largura = round(altura * 2), round(largura * 2)
        nova_imagem = np.zeros(
            (nova_altura, nova_largura, imagem.shape[2]), dtype=np.uint8)

        for y in range(nova_altura):
            for x in range(nova_largura):
                src_x = x * (largura / nova_largura)
                src_y = y * (altura / nova_altura)

                x1, y1 = int(np.floor(src_x)), int(np.floor(src_y))
                x2, y2 = min(x1 + 1, largura - 1), min(y1 + 1, altura - 1)

                dx = src_x - x1
                dy = src_y - y1

                pixel1 = imagem[y1, x1]
                pixel2 = imagem[y1, x2]
                pixel3 = imagem[y2, x1]
                pixel4 = imagem[y2, x2]

                nova_imagem[y, x] = (1 - dx) * (1 - dy) * pixel1 + dx * \
                    (1 - dy) * pixel2 + (1 - dx) * \
                    dy * pixel3 + dx * dy * pixel4

        return nova_imagem


# Transformando a imageme em uma matrix
arquivo_imagem = Image.open('imagens/img-02.jpg')
matrix_imagem = np.array(arquivo_imagem)

reducao = Reducao()
ampliar = Ampliacao()

resultado_interpolacao = reducao.bilinear(matrix_imagem)
resultado_imagem = Image.fromarray(resultado_interpolacao)

resultado = reducao.vizinho_mais_proximo(matrix_imagem)
resultado_imagem = Image.fromarray(resultado)
resultado_imagem.save('resultado_reducao_vizinhos.jpg')

# Para redução por vizinhos mais proximo.

resultado = reducao.bilinear(matrix_imagem)
resultado_imagem = Image.fromarray(resultado)
resultado_imagem.save('resultado_reducao_bilinear.jpg')

# Para ampliação por vizinhos mais proximo.

resultado = ampliar.vizinho_mais_proximo(matrix_imagem)
resultado_imagem = Image.fromarray(resultado)
resultado_imagem.save('resultado_ampliacao_vizinhos.jpg')

# Para ampliaçao por bilinear
resultado = ampliar.bilinear(matrix_imagem)
resultado_imagem = Image.fromarray(resultado)
resultado_imagem.save('resultado_ampliacao_bilinear.jpg')
