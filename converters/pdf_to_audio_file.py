# https://twitter.com/python_spaces/status/1584541970059624449?t=QHSQC4-956k4-KDcQ5_-Gg&s=09
import pyttsx3
import pdfplumber as pp

engine = pyttsx3.init()

all_data = ''

with pp.open('test.pdf') as book:
	for page_no, page in enumerate(book.pages, start=1):
		data = page.extract_text()
		all_data += data

engine.save_to_file(all_data, 'audio_book.mp3')
engine.runAndWait()
engine.stop()
