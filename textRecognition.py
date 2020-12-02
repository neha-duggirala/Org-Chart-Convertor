# TODO Azure OCR API
import numpy as np
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd =  r'C:\Program Files\Tesseract-OCR\tesseract.exe'
print("Packages imported:",np.__version__,cv2.__version__,np.__path__)
def img2text(im):
    config = ('-l eng --oem 1 --psm 3')
    # # pytessercat
    text = pytesseract.image_to_string(im, config=config)
    print(text)
    text = text.split('\n')
    return text
