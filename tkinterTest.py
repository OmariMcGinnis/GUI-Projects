from tkinter import *

top = Tk()
playlist = []

def printList():
    print(playlist)

def exportPlaylist():
    with open("playlist.txt", "w") as f:
        for song in playlist:
            f.write("%s\n" % song)

def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()
        
def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUIs")
    LMain.grid(column = 0, row = 1)
    
    E1Main = Button(text = "Week 1", bg = "white", command = week1)
    E1Main.grid(column = 0, row = 2)
    
    E2Main = Button(text = "Week 2", bg = "white", command = week2)
    E2Main.grid(column = 0, row = 3)
    
    E3Main = Button(text = "Week 3", bg = "white")
    E3Main.grid(column = 0, row = 4)
    
def week1():
    
    def addSong():
        playlist.append(E1.get())
        E1.delete(0, END)

    clearWindow()
    #This is a label widget
    L1 = Label(top, text="Playlist Generator")
    L1.grid(column= 0, row= 1)

    #This is a Text Entry widget
    E1 = Entry(top, bd = 5)
    E1.grid(column = 0, row = 2)

    #This is a Button widget
    B1 = Button(text = "Add to Playlist", bg = "light blue", command = addSong)
    B1.grid(column = 1, row = 2)

    B2 = Button(text = "Print List", bg = "light blue", command = printList)
    B2.grid(column = 0, row = 3)

    B3 = Button(text = "Export Playlist", bg = "white", command = exportPlaylist)
    B3.grid(column = 1, row = 3)

    Bclear = Button(text = "Main Menu", bg = "white", command = mainMenu)
    Bclear.grid(column = 1, row = 4)

def week2():
    clearWindow()

    L1W2 = Label(top, text = "Dice Roller App")
    L1W2.grid(column = 2, row = 1)
    
    L2W2 = Label(top, text = "# of Sides")
    L2W2.grid(column = 1, row = 2)
    
    L3W2 = Label(top, text = "# of Rolls")
    L3W2.grid(column = 3, row = 2)
    
    E1W2 = Entry(top, bd = 5)
    E1W2.grid(column = 1, row = 3)
    
    E2W2 = Entry(top, bd = 5)
    E2W2.grid(column = 3, row = 3)

    B1W2 = Button(text = "Roll Dice", bg = "light yellow")
    B1W2.grid(column = 2, row = 4)





    
    
if __name__ == "__main__":
    mainMenu()
    top.mainloop()
