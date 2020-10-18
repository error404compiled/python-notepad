from tkinter import *
from tkinter.messagebox import showinfo 
from tkinter.filedialog import askopenfilename , asksaveasfilename
import os
def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0 , END)
def openfile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files" , "*.*"), ("Text Documents" , "*.txt")])
    if file == "" :
        file = None
    else :
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0 , END)
        f = open(file , "r")
        TextArea.insert(1.0 , f.read())
        f.close()
    
def savefile():
    global file
    if file == None :
        file = asksaveasfilename(initialfile = "Untitled.txt" ,defaultextension=".txt", filetypes=[("All Files" , "*.*"), ("Text Documents" , "*.txt")])
        if file == "" :
            file = None

        else :
            f = open(file , "w")
            f.write(TextArea.get(1.0 , END))
            f.close()

            root.title(os.path,basename(file) + " - Notepad")
    else :
          f = open(file , "w")
          f.write(TextArea.get(1.0 , END))
          f.close()
            
def quitapp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad" , "Notepad with Archit")

if __name__ == '__main__' :
    #basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.geometry("644x788")

    # add textArea
    TextArea = Text(root , font="lucida 13")
    file = None
    TextArea.pack(expand =True , fill=BOTH)
    
    # creat a menu bar
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar , tearoff = 0)
    # to open a new file
    FileMenu.add_command(label="New" , command = newfile)
    # to open already existing file
    FileMenu.add_command(label="Open" , command = openfile)
    # to save the current file
    FileMenu.add_command(label="Save " , command = savefile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit" , command = quitapp)
    MenuBar.add_cascade(label = "File" , menu = FileMenu)
    # edit menu starts
    EditMenu = Menu(MenuBar , tearoff=0)
    # to give a future of cut , copy , paste
    EditMenu.add_command(label="Cut" , command = cut)
    EditMenu.add_command(label="Copy" , command = copy)
    EditMenu.add_command(label="Paste" , command = paste)
    MenuBar.add_cascade(label="Edit" , menu = EditMenu)
    # to make a help menu
    HelpMenu = Menu(MenuBar , tearoff=0)
    HelpMenu.add_command(label = "About Notepad" , command=about)
    MenuBar.add_cascade(label="Help" , menu = HelpMenu)
    
    
    
    

    root.config(menu=MenuBar)
    # adding a scroll bar
    scroll = Scrollbar(TextArea)
    scroll.pack(side = RIGHT , fill=Y)
    scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand = scroll.set)
    
    

    root.mainloop()
