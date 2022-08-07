from msilib.schema import Icon
import customtkinter
from linkqr import *
from textqr import *
from wifiqr import *
from barcode_ import *
from tkinter import *


# this is the function called when the button is clicked
def btnClickFunctionLink():
	LinkQR()


# this is the function called when the button is clicked
def btnClickFunctionText():
	TextQR()


# this is the function called when the button is clicked
def btnClickFunctionWifi():
	wifiQR()

def btnClickFunctionBar():
	generate_barcode()


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()

# This is the section of code which creates the main window
app.geometry('280x165')
app.title('QR-Code-Generator')


# This is the section of code which creates a button
customtkinter.CTkButton(app, text='Link QR-Code', command=btnClickFunctionLink, width=240).place(x=20, y=11)


# This is the section of code which creates a button
customtkinter.CTkButton(app, text='Text QR-Code', command=btnClickFunctionText, width=240).place(x=20, y=49)


# This is the section of code which creates a button
customtkinter.CTkButton(app, text='Wifi QR-Code', command=btnClickFunctionWifi, width=240).place(x=20, y=87)

# This is the section of code which creates a button
customtkinter.CTkButton(app, text='Barcode', command=btnClickFunctionBar, width=240).place(x=20, y=125)


app.mainloop()