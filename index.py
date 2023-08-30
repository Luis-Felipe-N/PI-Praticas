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
      
      for y in range(0, nova_altura):
        for x in range(0, nova_largura):
            pixel_01 = imagem[y * 2, x * 2]
            pixel_02 = imagem[y * 2, x * 2 + 1]
            pixel_03 = imagem[y * 2 + 1, x * 2]
            pixel_04 = imagem[y * 2 + 1, x * 2 + 1]
            

            pixel = (pixel_01[2] + pixel_02[2] + pixel_03[2] + pixel_04[2]) / 4
            nova_imagem[y, x] = round(pixel)
            
    # return nova_imagem
              
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
tamanho = 128

# for a in matrix_imagem:
#     print(a)
# print(matrix_imagem)
reducao = Reducao()
ampliar = Ampliacao()

resultado_vizinho_mais_proximo = reducao.vizinho_mais_proximo(matrix_imagem)

# # Realize a interpolação por vizinho mais próximo

# # Realize a interpolação bilinear
# # bilinear_result = bilinear_interpolation(image, new_size)

nearest_neighbor_pil = Image.fromarray(resultado_vizinho_mais_proximo)
# # bilinear_pil = Image.fromarray(bilinear_result)

# # Salve as imagens resultantes
nearest_neighbor_pil.save('nearest_neighbor_result.jpg')
# # bilinear_pil.save('bilinear_result.jpg')