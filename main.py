'''
from PyPDF2 import PdfReader

reader = PdfReader("Test2.pdf")
page = reader.pages[0]
print(len(reader.pages))
main_text = page.extract_text()
print(main_text)

main_text_list = main_text.split('AUTHORITY')
text_part_1 = main_text_list[3].split(':')
text_part_2 = main_text_list[4]
unz = text_part_1[2][:15:1].replace('\n', '')
cn = text_part_1[1].split('(')[0].replace('\n', '')
print(cn)
print(unz)
fio = main_text_list[5].split(')')
fio = fio[1].split('(')[0].replace('\n', '')
print(fio)

'''
import pytesseract.pytesseract
from pdf2image import convert_from_path
from pytesseract import image_to_string
from PIL import Image

pytesseract.pytesseract.tesseract_cmd= r'C:\Users\l\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


def convert_pdf_to_img(pdf_file):
    return convert_from_path(pdf_file)


def convent_image_to_text(file):
    text = image_to_string(file)
    return text


def get_text_from_any_pdf(pdf_file):
    images = convert_pdf_to_img(pdf_file)
    final_text = ''
    for pg, img in enumerate(images):

        final_text += convent_image_to_text(img)
        #print('Page n"{}".format(pg))
        #print(convent_image_to_text(img))

    return final_text

path_to_pdf = 'Test2.pdf'

main_text = get_text_from_any_pdf(path_to_pdf)