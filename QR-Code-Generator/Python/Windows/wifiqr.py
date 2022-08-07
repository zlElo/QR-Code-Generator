import wifi_qrcode_generator as qr #Import the wifi qr code libary
import customtkinter
from tkinter import filedialog
from tkinter import *


def wifiQR():
    # this is the function called when the button is clicked
    def btnClickFunctionSpeichern():
        img = qr.wifi_qrcode(tInputWifiName.get(), False, tInputCrypt.get(), tInputPw.get())
        file = filedialog.asksaveasfilename(
        filetypes=[("png file", ".png")],
        defaultextension=".png")
        img.save(f'{file}.png')
        app.destroy()


    app = customtkinter.CTk()
    app.iconbitmap('icon.ico')

    # This is the section of code which creates the main window
    app.geometry('280x450')
    app.title('Wifi-QR-Code')


    # This is the section of code which creates the a label
    customtkinter.CTkLabel(app, text='WLAN Name:').place(x=65, y=23)


    # This is the section of code which creates a text input box
    tInputWifiName=customtkinter.CTkEntry(app, width=240)
    tInputWifiName.place(x=17, y=54)


    # This is the section of code which creates the a label
    customtkinter.CTkLabel(app, text='Verschlüsselung:').place(x=65, y=97)


    # This is the section of code which creates a text input box
    tInputCrypt=customtkinter.CTkEntry(app, width=240)
    tInputCrypt.place(x=17, y=126)


    # This is the section of code which creates the a label
    customtkinter.CTkLabel(app, text='WLAN Passwort:').place(x=65, y=160)


    # This is the section of code which creates a text input box
    tInputPw=customtkinter.CTkEntry(app, width=240)
    tInputPw.place(x=17, y=190)


    # This is the section of code which creates the a label
    customtkinter.CTkLabel(app, text='Farbe:').place(x=65, y=222)


    # This is the section of code which creates a combo box
    comboOneTwoPunch= customtkinter.CTkComboBox(app, values=['black', 'green', 'blue', 'purple', 'red'], width=240)
    comboOneTwoPunch.place(x=17, y=252)


    # This is the section of code which creates the a label
    customtkinter.CTkLabel(app, text='Hintergrundfarbe:').place(x=65, y=302)


    # This is the section of code which creates a combo box
    comboBackroundcolor= customtkinter.CTkComboBox(app, values=['white', 'slategray', 'cadetblue', 'powderblue', 'yellow'], width=240)
    comboBackroundcolor.place(x=17, y=335)


    # This is the section of code which creates a button
    customtkinter.CTkButton(app, text='Speichern', command=btnClickFunctionSpeichern, width=240).place(x=17, y=387)

    app.iconbitmap('icon.ico')
    app.mainloop()