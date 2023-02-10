import aspose.words as aw

fileName = input("Please enter filename: ")

doc = aw.Document(fileName+".epub")

doc.save(fileName+".pdf")

print("File has been converted to "+fileName+".pdf")

