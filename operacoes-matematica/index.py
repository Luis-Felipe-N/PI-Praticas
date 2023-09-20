import numpy as np
from PIL import Image


def adicao(imagem_01, imagem_02):
  _largura_01, _altura_01 = imagem_01.shape[:2]
  _largura_02, _altura_02 = imagem_02.shape[:2]

  largura = _largura_01 if _largura_01 > _largura_02 else _largura_02
  altura = _altura_01 if _altura_01 > _altura_02 else _altura_02

  nova_imagem = np.zeros((largura, altura, 3), dtype=np.uint8)

  for x in range(largura):
    for y in range(altura):
      try:
        if (x < _largura_01 and y < _altura_01) and (x < _largura_02 and y < _altura_02):
          
          p1 = imagem_01[x, y]
          p2 = imagem_02[x, y]
          nova_imagem[x, y] = (p2 + p1) / 2
      except:
        ...

  return nova_imagem

def subtracao(imagem_01, imagem_02):
  _largura_01, _altura_01 = imagem_01.shape[:2]
  _largura_02, _altura_02 = imagem_02.shape[:2]

  largura = _largura_01 if _largura_01 > _largura_02 else _largura_02
  altura = _altura_01 if _altura_01 > _altura_02 else _altura_02

  nova_imagem = np.zeros((largura, altura, 3), dtype=np.uint8)

  for x in range(largura):
    for y in range(altura):
      try:
        if (x < _largura_01 and y < _altura_01) and (x < _largura_02 and y < _altura_02):
          nova_imagem[x, y] = imagem_01[x, y] - imagem_02[x, y]
      except:
        ...

  return nova_imagem

def espelhamento(imagem):
  largura, altura = imagem.shape[:2]

  # Aplique o espelhamento horizontal
  imagem_espelhada = np.zeros((largura, altura, 3), dtype=np.uint8)

  for x in range(largura):
      for y in range(altura):
          pixel = imagem[x, y]
          imagem_espelhada[largura - x - 1, y] = pixel

  return imagem_espelhada



# Transformando a imageme em uma matrix
imagem_01 = Image.open('../imagens/img-01.jpg')
imagem_02 = Image.open('../imagens/img-02.jpg')

# adicao_imagem = adicao(np.array(imagem_01), np.array(imagem_02))
# resultado_adicao_imagem = Image.fromarray(adicao_imagem)
# resultado_adicao_imagem.save('imagem_somada.jpg')

# imagem_subtraida = subtracao(np.array(imagem_01), np.array(imagem_02))
# resultado_imagem_subtraida = Image.fromarray(imagem_subtraida)
# resultado_imagem_subtraida.save('imagem_subtraida.jpg')

imagem_espelhamento = espelhamento(np.array(imagem_01))
resultado_imagem_espelhamento = Image.fromarray(imagem_espelhamento)
resultado_imagem_espelhamento.save('imagem_espelhamento.jpg')