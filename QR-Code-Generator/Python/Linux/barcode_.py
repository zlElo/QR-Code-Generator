from re import M
import customtkinter
from barcode import EAN13
from tkinter import filedialog
from tkinter import *



def generate_barcode():
    def btnClickFunctionSpeichern():
        nummer = (f'{tInputNummer.get()}')
        barcode = EAN13(nummer)
        file = filedialog.asksaveasfilename(
        filetypes=[("svg file", ".svg")],
        defaultextension=".svg")
        barcode.save(f'{file}.svg')
        app.destroy()
        

    app = customtkinter.CTk()

    # This is the section of code which creates the main window
    app.geometry('280x150')
    app.title('Bar-Code')


    # This is the section of code which creates the a label
    label = customtkinter.CTkLabel(app, text='12 stellige Nummer:').place(x=65, y=23)


    # This is the section of code which creates a text input box
    tInputNummer=customtkinter.CTkEntry(app, width=240)
    tInputNummer.place(x=17, y=54)

    # This is the section of code which creates a button
    customtkinter.CTkButton(app, text='Speichern', command=btnClickFunctionSpeichern, width=240).place(x=17, y=90)
    
    
    app.mainloop()