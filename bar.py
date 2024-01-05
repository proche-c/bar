from tkinter import *
from header import *
from body import *
from footer import *

root = Tk()
y = round((root.winfo_screenheight() - 1000) / 2)
x = round((root.winfo_screenwidth() - 600) / 2)
w = 1000
h = 600
root.geometry(str(w) + "x" + str(h) + "+" + str(x) + "+" + str(y))
root.resizable(0,0)
root.configure(bg='#525252')
root.title("")
header = Header(root)
body = Body(root)
footer = Footer(root)
root.mainloop()