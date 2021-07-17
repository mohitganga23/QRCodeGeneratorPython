import pyqrcode
from pyqrcode import QRCode

#String which represents the QR Code
s = input("Enter the string : ");

#Generate the QR Code
url = pyqrcode.create(s)

#Name of the file 
filename = input("Save file as : ")

#Save the QR Code generated as png
url.png(filename + ".png", scale= 8)