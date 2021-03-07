import pyttsx3
import PyPDF2
book = open('dancewithdragons.pdf', 'rb')
readpdf = PyPDF2.PdfFileReader(book)
pages = readpdf.numPages
print(pages)
Voice = pyttsx3.init()
Voice.setProperty('rate', 148)
for num in range(21, pages):
     page = readpdf.getPage(21)
     text = page.extractText()
     Voice.say(text)
     Voice.runAndWait()