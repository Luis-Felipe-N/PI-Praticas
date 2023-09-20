import numpy as np
from PIL import Image


def adicao(imagem_01, imagem_02):
  _largura_01, _altura_01 = imagem_01.shape[:2]
  _largura_02, _altura_02 = imagem_02.shape[:2]

  largura = _largura_01 if _largura_01 > _largura_02 else _largura_02
  altura = _altura_01 if _altura_01 > _altura_02 else _altura_02

  nova_imagem = np.zeros((altura, largura, 3), dtype=np.uint8)

  for y in range(altura):
    for x in range(largura):
        try:
          if (x < _largura_01 and y < _altura_01) and (x < _largura_02 and y < _altura_02):
            print(_largura_01, _altura_01)
            print(x, y)
            p1 = imagem_01[y, x]
            p2 = imagem_02[y, x]
            nova_imagem[y, x] = (p2 + p1) / 2
        except:
          ...

  return nova_imagem



# Transformando a imageme em uma matrix
imagem_01 = Image.open('../imagens/img-01.jpg')
imagem_02 = Image.open('../imagens/img-02.jpg')

adicao_imagem = adicao(np.array(imagem_01), np.array(imagem_02))
resultado_adicao_imagem = Image.fromarray(adicao_imagem)
resultado_adicao_imagem.save('imagem_somada.jpg')