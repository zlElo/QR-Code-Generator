import qrcode
import customtkinter
from tkinter import filedialog
from tkinter import *

def LinkQR():
    def btnClickFunction():
        # creating the variable for the QR code
        qr = qrcode.QRCode(
            version = 1,
            box_size = 15,
            border = 10
            )

        # adding a link
        daten = tInputLink.get()
        qr.add_data(daten)
        qr.make(fit=True)

        # adding the color
        img = qr.make_image(fill_color = comboFarbe.get(), back_color = comboOneBackround.get())
        file = filedialog.asksaveasfilename(
        filetypes=[("png file", ".png")],
        defaultextension=".png")
        img.save(file)
        app.destroy()
        
        

    app = customtkinter.CTk()
    app.iconbitmap('icon.ico')

    # This is the section of code which creates the main window
    app.geometry('175x297')
    app.title('Link-QR-Code')


    # This is the section of code which creates the a label
    customtkinter.CTkLabel(app, text='Link:').place(x=17, y=17)


    # This is the section of code which creates a text input box
    tInputLink=customtkinter.CTkEntry(app)
    tInputLink.place(x=17, y=45)


    # This is the section of code which creates the a label
    customtkinter.CTkLabel(app, text='Farbe:').place(x=17, y=85)


    # This is the section of code which creates a combo box
    comboFarbe= customtkinter.CTkComboBox(app, values=['black', 'green', 'blue', 'purple', 'red'])
    comboFarbe.place(x=17, y=114)


    # This is the section of code which creates the a label
    customtkinter.CTkLabel(app, text='Hintergrundfarbe: ').place(x=17, y=163)


    # This is the section of code which creates a combo box
    comboOneBackround= customtkinter.CTkComboBox(app, values=['white', 'slategray', 'cadetblue', 'powderblue', 'yellow'])
    comboOneBackround.place(x=17, y=192)


    # This is the section of code which creates a button
    customtkinter.CTkButton(app, text='Speichern', command=btnClickFunction).place(x=17, y=245)

    
    app.mainloop()