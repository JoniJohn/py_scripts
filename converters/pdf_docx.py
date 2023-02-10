from pdf2docx import Converter


cv = Converter('test.pdf')

cv.convert('test.docx')

cv.close()
