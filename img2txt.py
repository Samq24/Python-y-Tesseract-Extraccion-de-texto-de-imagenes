import cv2
import pytesseract
from docx import Document
import imghdr
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

folder_path = r'C:\Users\samae\OneDrive\Documentos\Pyblog'

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    image_type = imghdr.what(file_path)
    if image_type in ['jpeg', 'png', 'jpg']: 
        image = cv2.imread(file_path)

        text = pytesseract.image_to_string(image)

        output_docx = os.path.splitext(filename)[0] + '.docx'
        doc = Document()
        doc.add_paragraph(text)
        doc.save(output_docx)
        print(f'Texto de {filename} guardado en {output_docx}')

        output_txt = os.path.splitext(filename)[0] + '.txt'
        with open(output_txt, 'w', encoding='utf-8') as archivo:
            archivo.write(text)
        print(f'Texto de {filename} guardado en {output_txt}')
    else:
        print(f'El archivo {filename} no es una imagen válida (JPEG o PNG).')
