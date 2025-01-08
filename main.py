import cv2
import numpy as np
import easyocr

image_file_name = "colocar_imagem(_precisa_estar_na_pasta)"
image = cv2.imread(image_file_name)

if image is None:
    print("Erro ao carregar a imagem.")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sharpen_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpened = cv2.filter2D(gray, -1, sharpen_kernel)
    _, thresh = cv2.threshold(sharpened, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    reader = easyocr.Reader(['pt'], gpu=False)
    results = reader.readtext(thresh, detail=0)
    print("Texto detectado:")
    for line in results:
        print(line)