import customtkinter
from barcode import EAN13
from tkinter import filedialog



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
    app.geometry('175x150')
    app.title('Wifi-QR-Code')


    # This is the section of code which creates the a label
    customtkinter.CTkLabel(app, text='12 stellige Nummer:').place(x=17, y=23)


    # This is the section of code which creates a text input box
    tInputNummer=customtkinter.CTkEntry(app)
    tInputNummer.place(x=17, y=54)

    # This is the section of code which creates a button
    customtkinter.CTkButton(app, text='Speichern', command=btnClickFunctionSpeichern).place(x=17, y=90)

    app.mainloop()