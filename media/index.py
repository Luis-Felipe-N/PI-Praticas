import numpy as np
from PIL import Image

def media(imagem):
  largura, altura = imagem.shape[:2]

  # Cria uma nova imagem com as mesmas dimensões da imagem original
  new_imagem = np.zeros((largura, altura, 3), dtype=np.uint8)
  
  # Percorre cada pixel da imagemm
  for i in range(largura):
    for j in range(altura):
        # Cria uma matriz de vizinhança para o pixel
        neighborhood = imagem[max(0, i-1):min(i+2, largura), max(0, j-1):min(j+2, altura)]
        print('[PIXEL]', neighborhood)
        
        # Calcula a média dos pixels na matriz de vizinhança
        mean = np.mean(neighborhood)
        
        # Atribui a média ao pixel correspondente na nova imagem
        new_imagem[i, j] = mean

  return new_imagem

# Transformando a imageme em uma matrix
imagem_01 = Image.open('../imagens/img-02.jpg')

imagem_media = media(np.array(imagem_01))
resultado_imagem_media = Image.fromarray(imagem_media)
resultado_imagem_media.save('imagem_media.jpg')