__author__ = 'Mark'
from Tkinter import Tk
import tkFileDialog
import sys

def pickaudiofile():
    FilePicker = Tk()
    FilePicker.withdraw()  # we don't want a full GUI, so keep the root window from appearing
    FilePicker.focus_force()
    filename = tkFileDialog.askopenfilename(filetypes = [('Wav files', '.wav')])

    # Assert file selected
    if filename == "":
        print("File select canceled.")
        sys.exit(0)

    FilePicker.destroy()  # Destory our TKinter instance

    return filename

def pickvideofile():
    FilePicker = Tk()
    FilePicker.withdraw()  # we don't want a full GUI, so keep the root window from appearing
    FilePicker.lift()
    FilePicker.focus_force()
    filename = tkFileDialog.askopenfilename(filetypes = [('MOV files', '.mov')])

    # Assert file selected
    if filename == "":
        print("File select canceled.")
        sys.exit(0)

    FilePicker.destroy()  # Destory our TKinter instance

    return filename

def getsavefilename():
    FilePicker = Tk()
    FilePicker.withdraw() # we don't want a full GUI, so keep the root window from appearing
    FilePicker.lift()
    FilePicker.focus_force()
    filename = tkFileDialog.asksaveasfilename(defaultextension=".wav")

    if filename == "":
        print("File select canceled.")
        sys.exit(0)

    FilePicker.destroy()  # Destory our TKinter instance

    return filename