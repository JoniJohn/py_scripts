import PyPDF2 as pdf
import pyttsx3 as pyt

path = open('test.pdf', 'rb')

pdfReader = pdf.PdfFileReader(path)

speak = pyt.init()

for pageNo in range(pdfReader.numPages):
	text = pdfReader.getPage(pageNo).extractText()
	speak.say(text)
	speak.runAndWait()

speak.stop()
