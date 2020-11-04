import pyttsx3
speaker = pyttsx3.init()
speaker.setProperty('rate', 170)

speaker.say('hey booos i can talk do you see!')
rate = speaker.getProperty('rate')

speaker.runAndWait()
print(rate)
# import pyttsx3
# import PyPDF2
# book = open('vanet.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(book)
# pages = pdfReader.numPages

# speaker = pyttsx3.init()

# rate = speaker.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        #printing current voice rate
# speaker.setProperty('rate', 100) 
# for num in range(7, pages):
#     page = pdfReader.getPage(num)
#     text = page.extractText()
#     speaker.say(text)
#     speaker.runAndWait()
