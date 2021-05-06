from tkinter import *

top = Tk()
playlist = []

def addSong():
    playlist.append(E1.get())
    E1.delete(0, END)

def printList():
    print(playlist)

def exportPlaylist():
    with open("playlist.txt", "w") as f:
        for song in playlist:
            f.write("%s\n" % song)

#This is a label widget
L1 = Label(top, text="Playlist Generator")
L1.grid(column= 0, row= 1)

#This is a Text Entry widget
E1 = Entry(top, bd = 5)
E1.grid(column = 0, row = 2)

#This is a Button widget
B1 = Button(text="Add to Playlist", bg = "light blue", command = addSong)
B1.grid(column = 1, row = 2)

B2 = Button(text = "Print List", bg = "light blue", command = printList)
B2.grid(column = 0, row = 3)

B3 = Button(text= "Export Playlist", bg = "white", command = exportPlaylist)
B3.grid(column = 1, row = 3)



top.mainloop()
