import numpy as np
from PIL import Image


class Reducao():
    
    def vizinho_mais_proximo(self, imagem):
      # Pegando altura atual
      altura, largura = imagem.shape[:2]
      nova_altura, nova_largura = round(altura / 2), round(largura / 2)

      # Criando a matrix da nova imagem
      nova_imagem = np.zeros((nova_altura, nova_largura, imagem.shape[2]), dtype=np.uint8)

      for y in range(nova_altura):
          for x in range(nova_largura):       
            nova_imagem[y, x] = imagem[y * 2 , x * 2]
              
      return nova_imagem
    
    def bilinear(self, imagem):
      # Pegando altura atual
      altura, largura = imagem.shape[:2]

      # Tamanho e altura final da imagem
      nova_altura, nova_largura = round(altura / 2), round(largura / 2)

      # Criando a matrix da nova imagem
      nova_imagem = np.zeros((nova_altura, nova_largura, imagem.shape[2]), dtype=np.uint8)
      
      for y in range(nova_altura):
        for x in range(nova_largura):
            pixel_01 = imagem[y * 2, x * 2]
            pixel_02 = imagem[y * 2, x * 2 + 1]
            pixel_03 = imagem[y * 2 + 1, x * 2]
            pixel_04 = imagem[y * 2 + 1, x * 2 + 1]

            pixel = []
            for p in range(imagem.shape[2]):
              print((pixel_01[p] + pixel_02[p] + pixel_03[p] + pixel_04[p]) / 4)
              pixel.append(round((pixel_01[p] + pixel_02[p] + pixel_03[p] + pixel_04[p]) / 4))
            print(pixel)
            nova_imagem[y, x] = pixel
              
      return nova_imagem 

class Ampliacao():
    
    def vizinho_mais_proximo(self, imagem):
      altura, largura = imagem.shape[:2]
      nova_altura, nova_largura = altura * 2, largura * 2

      nova_imagem = np.zeros((nova_altura, nova_largura, imagem.shape[2]), dtype=np.uint8)
      
      for y in range(0, nova_altura, 2):
          for x in range(0, nova_largura, 2):
              pixel = imagem[y // 2, x // 2]
              nova_imagem[y, x] = pixel
              nova_imagem[y + 1, x] = pixel
              nova_imagem[y, x + 1] = pixel
              nova_imagem[y + 1, x + 1] = pixel
              
      return nova_imagem

# Transformando a imageme em uma matrix
arquivo_imagem = Image.open('imagens/img-02.jpg')
matrix_imagem = np.array(arquivo_imagem)

reducao = Reducao()
ampliar = Ampliacao()

resultado_interpolacao = reducao.bilinear(matrix_imagem)
resultado_imagem = Image.fromarray(resultado_interpolacao)

# # Salve as imagens resultantes
resultado_imagem.save('resultado.jpg')