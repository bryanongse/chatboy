import tkinter as tk
from tkinter import *
import os
from tkinter import filedialog
#from newspaper import Article
import random
def send(event=None):
    usr_input = message.get()
    usr_input = usr_input.lower()
    textcon.insert(END, f'User: {usr_input}'+'\n','usr')
    if usr_input in exit_list:
        textcon.config(fg='yellow')
        textcon.insert(END,"Bot:Ok bye! Chat with you later\n")
        return root.destroy()
    else:
        textcon.config(fg='yellow')
        if greet_res(usr_input) != None:
            lab=f"Bot: {greet_res(usr_input)}"+'\n'
            textcon.insert(END,lab)
        else:
            lab = f"Bot: {bot_ress(usr_input)}"+'\n'
            textcon.insert(END, lab)


root=tk.Tk()
filename="Untitled.txt"
root.title(f"Chat Bot - Untitled.txt")
root.geometry('500x400')

root.resizable(False, False)
main_menu=Menu(root)
file_menu=Menu(root)
edit_menu=Menu(root)
root.config(menu=main_menu)
message=tk.StringVar()
chat_win=Frame(root,bd=1,bg='black',width=50,height=8)
chat_win.place(x=6,y=6,height=300,width=480)
textcon=tk.Text(chat_win,bd=1,bg='black',width=50,height=8)
textcon.pack(fill="both",expand=True)
mes_win=Entry(root,width=30,xscrollcommand=True,textvariable=message)
mes_win.place(x=6,y=310,height=60,width=366)
mes_win.focus()
textcon.config(fg='yellow')
textcon.tag_config('usr',foreground='white')
textcon.insert(END,"Bot: This is your chat bot to assist you about Machine Learning!\n\n")
mssg=mes_win.get()
button=Button(root,text='Send',bg='yellow',activebackground='orange',command=send,width=12,height=5,font=('Arial'))
button.place(x=376,y=310,height=60,width=110)
scrollbar=tk.Scrollbar(textcon)
scrollbar.pack(fill='y')
scrollbar.place(relheight = 1,relx = 1)
scrollbar.config(command = textcon.yview)
root.mainloop()