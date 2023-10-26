import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def erode(img, mascara):
    imagem_shape = img.shape
    mascara_shape = mascara.shape
    mascara_centro = (mascara_shape[0] // 2, mascara_shape[1] // 2)
    erosao_image = np.zeros((imagem_shape[0] + mascara_shape[0] - 1, imagem_shape[1] + mascara_shape[1] - 1))
    
    x_append = np.zeros((img.shape[0], mascara_shape[1] - 1))
    img = np.append(img, x_append, axis=1)

    y_append = np.zeros((mascara_shape[0] - 1, img.shape[1]))
    img = np.append(img, y_append, axis=0)

    for i in range(imagem_shape[0]):
        for j in range(imagem_shape[1]):
            i_ = i + mascara.shape[0]
            j_ = j + mascara.shape[1]
            x,y = i + mascara_centro[0], j + mascara_centro[1]
            tmp = np.zeros((mascara_shape[0],mascara_shape[1]))
            if np.all(img[i:i_, j:j_]!=0):
                tmp = img[i:i_,j:j_] - mascara[0:mascara.shape[0], 0:mascara.shape[1]]
                erosao_image[x,y] = tmp.min()
    
    return erosao_image[:imagem_shape[0], :imagem_shape[1]]/255.0

def dilate(img, mascara):
  mascara_altura, mascara_largura = mascara.shape
  mascara_centro = (mascara_altura // 2, mascara_largura // 2)

  # Cria uma matriz vazia com mais espaco para dilatacao
  altura, largura = img.shape
  dilatacao_image = np.zeros((altura + mascara_altura - 1, largura + mascara_largura - 1))

  # Ajusta o tamanho da imagem adicionando mais espaco a direita
  x_append = np.zeros((altura, mascara_largura - 1))
  img = np.append(img, x_append, axis=1)

  # Ajusta o tamanho da imagem adicionando mais espaco para baixo
  y_append = np.zeros((mascara_altura - 1, largura))
  img = np.append(img, y_append, axis=0)
  
  # Altura
  for i in range(altura):
    # Largura
    for j in range(largura):
      i_ = i + mascara_altura
      j_ = j + mascara_largura
      tmp = np.zeros((mascara_altura,mascara_largura))

      if (img[ i + mascara_centro[0], j + mascara_centro[0] ] != 0):
        # Somando a submatriz da imagem de entrada com a mascara
        tmp = img[i:i_,j:j_] + mascara[0:mascara.shape[0], 0:mascara.shape[1]]

        # Percorre a região onde a mascara é aplicado na imagem de saída
        for m in range(i,i_):
          for n in range(j,j_):
            # Somando o pixel da imagem de entrada com o pixel da mascara
            new_value = img[i + mascara_centro[0], j + mascara_centro[0]] + mascara[mascara_centro[0], mascara_centro[1]]
            if(dilatacao_image[m, n] < new_value):
              dilatacao_image[m, n] = new_value
        dilatacao_image[i+mascara_centro[0],j+mascara_centro[1]] = tmp.max()
  return dilatacao_image[:altura, :largura]/255.0

def gradient(img, mascara):
    return dilate(img,mascara) - erode(img,mascara)

mascara = np.array([[0, 1, 0],
                   [1, 1, 1],
                   [0, 1, 0]], dtype=np.uint8)


input_image = plt.imread('imagens/a.png')

if len(input_image.shape) == 3:
    input_image = np.mean(input_image, axis=2)

mascara = np.array([[0, 1, 0],
                   [1, 1, 1],
                   [0, 1, 0]])


imagem_erodida = erode(input_image, mascara)
plt.imsave("imagem_erodida.png", imagem_erodida, cmap='gray')

imagem_dilatada = dilate(input_image, mascara)
plt.imsave("imagem_dilatada.png", imagem_dilatada, cmap='gray')

gradient_image = gradient(input_image, mascara)
plt.imsave("gradient_image.png", gradient_image, cmap='gray')