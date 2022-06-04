# make sure to install the modules before usig it.
import pyttsx3
import PyPDF2

speaker = pyttsx3.init()
book = open("YourFile.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(book)
pages = pdf_reader.numPages
print(pages)


# you can give it a range or page to start
for text in range(3, pages):
    page = pdf_reader.getPage(text)
    text = page.extractText()

    speaker.say(text)
    speaker.runAndWait()
