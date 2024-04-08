from tkinter import*
from tkinter import filedialog
#basic title and icon 
root=Tk()
root.title("Untitled - Notepad")
#root.wm_iconbitmap("C:\Users\Admin\Desktop\python\notepad.png")
root.geometry("500x500")
def new():
    win=Toplevel(root) #for new window
    win.geometry("400x400")
    win.title("New win")
    text_area_win=Text(win,height=400,width=400,bg="aliceblue")
    text_area_win.pack()
    Button(win,text="Exit",command=lambda:win.destroy()).pack()
def Newwin():
    pass
def open():
    f=filedialog.askopenfile()
    print(f.read())
  
def save():
    s=filedialog.asksaveasfile()
    t=text_area.get("0.0",END)
    s.write(t)
    
    
def saveas():
    pass
def Exit():
    root.destroy()
def undo():
    pass
def cut():
    text_area.event_generate("<<Cut>>")
def copy():
    text_area.event_generate("<<Copy>>")
def paste():
    text_area.event_generate("<<Paste>>")
def delete():
    pass
def world():
    pass
def font():
    pass
def zoom():
    pass
def status():
    pass
def viewhelp():
    pass
def sendfeedback():
    pass
def about():
    pass
#menubar
menubar=Menu(root)#main menu









#filemenu
Filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=Filemenu)
Filemenu.add_command(label="New",command=new)
Filemenu.add_command(label="Nwe Window",command=Newwin)
Filemenu.add_command(label="Open...",command=open)
Filemenu.add_command(label="Save",command=save)
Filemenu.add_command(label="Save As...",command=saveas)
Filemenu.add_command(label="Exit",command=Exit)
# edit ootion
editmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Undo",command=undo)
editmenu.add_command(label="Cut",command=cut)
editmenu.add_command(label="Copy",command=copy)
editmenu.add_command(label="Paste",command=paste)
editmenu.add_command(label="Delete",command=delete)
# formate option
formatemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Formate",menu=formatemenu)
formatemenu.add_command(label="World Wrap",command=world)
formatemenu.add_command(label="Font...",command=font)
#view menu
viewmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="View",menu=viewmenu)
viewmenu.add_command(label="Zoom",command=zoom)
viewmenu.add_command(label="Status bar",command=status)
#help menu
helpmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="View Help",command=viewhelp)
helpmenu.add_command(label="Send Feedback",command=sendfeedback)
helpmenu.add_command(label="About",command=about)
#for notepad text area
f=Frame(root)
f.pack()
s=Scrollbar(f)
s.pack(side="right",fill=Y)
text_area=Text(f,height=500,width=500,font=("Ebrima",30))
text_area.pack()
#end text area
root.config(menu=menubar)
root.mainloop()