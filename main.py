import cv2
import numpy as np
import easyocr

image_file_name = r"C:\Users\Dell\Downloads\Atas\Atas.py\segredinho.jpeg"
image = cv2.imread(image_file_name)

if image is None:
    print("Erro ao carregar a imagem.")
else:
    bright_image = cv2.convertScaleAbs(image, alpha=1.5, beta=50)
    image_resized = cv2.resize(bright_image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    smoothed = cv2.GaussianBlur(image_resized, (5, 5), 0)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sharpen_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpened = cv2.filter2D(gray, -1, sharpen_kernel)
    _, thresh = cv2.threshold(sharpened, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    adaptive_thresh = cv2.adaptiveThreshold(
    sharpened, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    reader = easyocr.Reader(['pt'], gpu=False)
    results = reader.readtext(thresh, detail=0)
    print("Texto detectado:")
    for line in results:
        print(line)
        