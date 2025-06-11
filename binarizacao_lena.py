import cv2

# Carrega a imagem original (em cores)
imagem_colorida = cv2.imread('lena.png')

# Converte para tons de cinza
imagem_cinza = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)

# Aplica a binarização com um limiar (threshold) de 128
_, imagem_binaria = cv2.threshold(imagem_cinza, 128, 255, cv2.THRESH_BINARY)

# Exibe as imagens
cv2.imshow('Imagem Original', imagem_colorida)
cv2.imshow('Imagem em Cinza', imagem_cinza)
cv2.imshow('Imagem Binária', imagem_binaria)

cv2.waitKey(0)
cv2.destroyAllWindows()
