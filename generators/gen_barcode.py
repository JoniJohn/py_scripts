import barcode
from barcode import Code128

def generate_barcode(data):
	code = Code128(data)
	code.save("barcode")
	print("Barcode Generated.")

barcodeStr = input("Please enter barcode string: ")

generate_barcode(barcodeStr)
