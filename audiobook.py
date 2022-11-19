import pyttsx3
import PyPDF2

book = open('Kohlbergian_Analysis_of_the_Moral_Reasoning_in_Lin.pdf', 'rb') # rb - read-only in binary format
pdfREader = PyPDF2.PdfFileReader(book) #reads the PDF file linked
pages = pdfREader.numPages #counts the number of pages of the PDF file linked
print(pages)
speaker = pyttsx3.init() #initialize
page = pdfREader.getPage(3) # 0 indexing
text = page.extractText() #will extract the text from the chosen page
speaker.say(text)
speaker.runAndWait()