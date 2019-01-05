# # # # # # # # # # # # #
#						#
#						#
#						#
#		Pi Radio		#
#		By				#
#		Jackson			#
#		Hoggard			#
#	    (c)2018			#
#						#
#						#
#						#
# # # # # # # # # # # # #

import os
from Tkinter import *
import PIL.Image, PIL.ImageTk

# os.system("clear")


class Window:
    def __init__(self, master, title, labelText, commandText, command):
        self.master = master
        master.title(title)
        
        image = PhotoImage(file='/home/pi/fm_transmitter/raspi.png')

        self.label = Label(master, text=labelText)
        self.label.pack()

        self.button = Button(master, text=commandText, command=lambda : self.command(command))
        self.button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def command(self, command):
        os.system(command)

## Main Menu
root = Tk()
main = Window(root, "Pi Radio", "Pi Radio", "Shuffle Play", "sudo python ./PiRadio.py")
root.mainloop()
## End of Main Menu
