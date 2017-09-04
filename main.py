import PyPDF2
def main():
    pdfFileObj = open('meetingminutes.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pdfReader.numPages
        # check if its "SERVES + Integer" // Bad solution probably
        # if so, go back 2 lines to get name (immer 2 im vorraus checken?)
        # get whole recipe list
        # compare matching with given ingredients
        # return recipe if 3/4 ingredients are in your fridge


    ins.close()
