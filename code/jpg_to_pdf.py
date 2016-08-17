#this program converts a set of jpgs in a directory to pdfs, and links them into one pdf
import os
import PyPDF2
import img2pdf

path = ""
filename = ""
merger = PyPDF2.PdfFileMerger()

def convertToPdf(f):
	try:
		pdf_bytes = img2pdf.convert(path + "/" + f)
	except:
		print("couldn't convert file " + f)
		return
	tempPath = "page.pdf"
	pagew = open(tempPath,"wb")
	pagew.write(pdf_bytes)
	pagew.close()
	pager = PyPDF2.PdfFileReader(open(tempPath,"rb"))
	a = pager.getPage(0)
	merger.append(pager)
	

def createCombinedPdf():
	with open(filename, "wb") as outputStream:
		try:
			merger.write(outputStream)
		except:
			print("Error: PDF generation failed")

def getDir():
	global path 
	while True:
		path = input("Enter path to directory (without trailing \"/\") where all of your image files are stored: ")
		if os.path.isdir(path): break
		else: print("Directory not found. Reenter path.")
	global filename 
	filename = input("Enter the directory where you want the final pdf to be saved: ")

def main():
	getDir()
	for f in os.listdir(path):
		convertToPdf(f)	
	createCombinedPdf()
	os.remove("page.pdf")

main()
