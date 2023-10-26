import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def erode(img, kernel):
    imagem_shape = img.shape
    kernel_shape = kernel.shape
    kernel_centro = (kernel_shape[0] // 2, kernel_shape[1] // 2)
    erosao_image = np.zeros((imagem_shape[0] + kernel_shape[0] - 1, imagem_shape[1] + kernel_shape[1] - 1))
    
    x_append = np.zeros((img.shape[0], kernel_shape[1] - 1))
    img = np.append(img, x_append, axis=1)

    y_append = np.zeros((kernel_shape[0] - 1, img.shape[1]))
    img = np.append(img, y_append, axis=0)

    for i in range(imagem_shape[0]):
        for j in range(imagem_shape[1]):
            i_ = i + kernel.shape[0]
            j_ = j + kernel.shape[1]
            x,y = i + kernel_centro[0], j + kernel_centro[1]
            tmp = np.zeros((kernel_shape[0],kernel_shape[1]))
            if np.all(img[i:i_, j:j_]!=0):
                tmp = img[i:i_,j:j_] - kernel[0:kernel.shape[0], 0:kernel.shape[1]]
                erosao_image[x,y] = tmp.min()
    
    return erosao_image[:imagem_shape[0], :imagem_shape[1]]/255.0

def dilate(img, kernel):
    kernel_shape = kernel.shape
    kernel_centro = (kernel.shape[0] // 2, kernel.shape[1] // 2)
    dilatacao_image = np.zeros((img.shape[0] + kernel.shape[0] - 1, img.shape[1] + kernel.shape[1] - 1))
    imagem_shape = img.shape

    x_append = np.zeros((img.shape[0], kernel.shape[1] - 1))
    img = np.append(img, x_append, axis=1)

    y_append = np.zeros((kernel.shape[0] - 1, img.shape[1]))
    img = np.append(img, y_append, axis=0)

    for i in range(imagem_shape[0]):
        for j in range(imagem_shape[1]):
            i_ = i + kernel.shape[0]
            j_ = j + kernel.shape[1]
            tmp = np.zeros((kernel_shape[0],kernel_shape[1]))
            if (img[i+kernel_centro[0],j+kernel_centro[0]]!=0):
                tmp = img[i:i_,j:j_] + kernel[0:kernel.shape[0], 0:kernel.shape[1]]
                for m in range(i,i_):
                    for n in range(j,j_):
                        new_value = img[i+kernel_centro[0],j+kernel_centro[0]]+kernel[kernel_centro[0], kernel_centro[1]]
                        if(dilatacao_image[m, n] < new_value):
                            dilatacao_image[m, n] = new_value
                dilatacao_image[i+kernel_centro[0],j+kernel_centro[1]] = tmp.max()
    return dilatacao_image[:imagem_shape[0], :imagem_shape[1]]/255.0

def gradient(img, kernel):
    return dilate(img,kernel) - erode(img,kernel)

kernel = np.array([[0, 1, 0],
                   [1, 1, 1],
                   [0, 1, 0]], dtype=np.uint8)


input_image = plt.imread('imagens/l.png')

if len(input_image.shape) == 3:
    input_image = np.mean(input_image, axis=2)

kernel = np.array([[0, 1, 0],
                   [1, 1, 1],
                   [0, 1, 0]])


imagem_erodida = erode(input_image, kernel)
plt.imsave("imagem_erodida.png", imagem_erodida, cmap='gray')

imagem_dilatada = dilate(input_image, kernel)
plt.imsave("imagem_dilatada.png", imagem_dilatada, cmap='gray')

gradient_image = gradient(input_image, kernel)
plt.imsave("gradient_image.png", gradient_image, cmap='gray')