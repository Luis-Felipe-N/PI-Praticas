import numpy as np
from PIL import Image


class Reducao():
    def vizinho_mais_proximo(self, imagem):
      # Pegando altura atual
      altura, largura = imagem.shape[:2]
      nova_altura, nova_largura = round(altura / 2), round(largura / 2)

      # Criando a matrix da nova imagem
      nova_imagem = np.zeros((nova_altura, nova_largura, imagem.shape[2]), dtype=np.uint8)
      print(imagem.shape) #ver na documentação a funão shape
      for y in range(nova_altura):
          # print('[Y INDEX]', y)
          for x in range(nova_largura):
            # print('[X INDEX]', x)              
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

            pixel = (pixel_01[2] + pixel_02[2] + pixel_03[2] + pixel_04[2]) / 4
            nova_imagem[y, x] = round(pixel)
              
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
    
    def bilinear(self, imagem):
      pass


# Transformando a imageme em uma matrix
arquivo_imagem = Image.open('imagens/img-02.jpg')
matrix_imagem = np.array(arquivo_imagem)

reducao = Reducao()
ampliar = Ampliacao()

#Para redução por vizinhos mais proximo.

resultado = reducao.vizinho_mais_proximo(matrix_imagem)
resultado_imagem = Image.fromarray(resultado)
resultado_imagem.save('resultado_reducao_vizinhos.jpg')

#Para redução por vizinhos mais proximo.

resultado = reducao.bilinear(matrix_imagem)
resultado_imagem = Image.fromarray(resultado)
resultado_imagem.save('resultado_reducao_bilinear.jpg')

#Para ampliação por vizinhos mais proximo.

resultado = ampliar.vizinho_mais_proximo(matrix_imagem)
resultado_imagem = Image.fromarray(resultado)
resultado_imagem.save('resultado_ampliacao_vizinhos.jpg')

#Para ampliaçao por bilinear.

resultado = ampliar.bilinear(matrix_imagem)
resultado_imagem = Image.fromarray(resultado)
resultado_imagem.save('resultado_ampliacao_bilinear.jpg')