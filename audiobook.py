import pyttsx3
import PyPDF2

book = open('Kohlbergian_Analysis_of_the_Moral_Reasoning_in_Lin.pdf', 'rb') # rb - read-only in binary format
pdfREader = PyPDF2.PdfFileReader(book) #reads the PDF file linked
pdfREader.numPages #counts the number of pages of the PDF file linked
print(pages)
speaker = pyttsx3.init() #initialize
speaker.say('Hey, can you hear me?')
speaker.runAndWait()