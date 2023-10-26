import numpy as np
from PIL import Image

import numpy as np

def apply_laplacian_filter(image, kernel):
    # Converte a imagem e o kernel para arrays numpy
    image = np.array(image)
    kernel = np.array(kernel)
    
    # Cria uma nova imagem com as mesmas dimensões da imagem original
    new_image = np.zeros(image.shape)
    
     # Percorre cada pixel da imagem
    for i in range(image.shape[0]):
      for j in range(image.shape[1]):
        # Cria uma matriz de vizinhança para o pixel
        # neighborhood = image[max(0, i-1):min(i+2, image.shape[0]), max(0, j-1):min(j+2, image.shape[1])]
        
        # Garante que a vizinhança e o kernel tenham a mesma forma
        neighborhood = np.pad(neighborhood, ((0, kernel.shape[0] - neighborhood.shape[0]), (0, kernel.shape[1] - neighborhood.shape[1])), 'constant')
        # if neighborhood.shape != kernel.shape:
        
        # Convolve a matriz de vizinhança com o kernel
        convolution = np.sum(neighborhood * kernel)
        
        # Atribui o resultado da convolução ao pixel correspondente na nova imagem
        new_image[i, j] = convolution
    
    return new_image

# Transformando a imageme em uma matrix
imagem_01 = Image.open('../imagens/img-01.jpg')

# laplacian_3x3 = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
# laplacian_5x5 = np.array([[-1, -1, -1, -1, -1], [-1, 1, 1, 1, -1], [-1, 1, 1, 1, -1], [-1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]])
# laplacian_1st_derivative_3x3 = np.array([[1, 0, -1], [0, 0, 0], [-1, 0, 1]])
laplacian_2nd_derivative_3x3 = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])

# Aplica o filtro Laplaciano com diferentes kernels
# image_laplacian_3x3 = apply_laplacian_filter(imagem_01, laplacian_3x3)
# image_laplacian_5x5 = apply_laplacian_filter(imagem_01, laplacian_5x5)
# image_laplacian_1st_derivative_3x3 = apply_laplacian_filter(imagem_01, laplacian_1st_derivative_3x3)
image_laplacian_2nd_derivative_3x3 = apply_laplacian_filter(imagem_01, laplacian_2nd_derivative_3x3)

resultado_imagem_espelhamento = Image.fromarray(image_laplacian_2nd_derivative_3x3)
if resultado_imagem_espelhamento.mode != 'RGB':
    resultado_imagem_espelhamento = resultado_imagem_espelhamento.convert('RGB')

resultado_imagem_espelhamento.save('imagem_espelhamento.jpg')