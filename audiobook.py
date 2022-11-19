import pyttsx3
import PyPDF2

book = open('Kohlbergian_Analysis_of_the_Moral_Reasoning_in_Lin.pdf', 'rb') # rb - read-only in binary format
pdfREader = PyPDF2.PdfFileReader(book) #reads the PDF file linked
pages = pdfREader.numPages #counts the number of pages of the PDF file linked
print(pages)

speaker = pyttsx3.init() #initialize
rate = speaker.getProperty('rate')
speaker.setProperty('rate', 180) #adjusted the speed of reading since its default 200 is too fast
print(rate)

for num in range(2, 3): #freely choose the range of pages you want to recall or read aloud
    page = pdfREader.getPage(2) # 0 indexing; can remove the for loop and just choose a single page as a parameter
    text = page.extractText() #will extract the text from the chosen page
    speaker.say(text)
    speaker.runAndWait()