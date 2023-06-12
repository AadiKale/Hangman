import random
from tkinter import *
from tkinter import messagebox
import pyttsx3

speak = pyttsx3.init()


def hangman():
    global ws, st, ws1, n, temp, first
    first = word.get()
    box1.delete(0, END)
    if n > 0:
        if first in ws:
            for i in range(ws1):
                if ws[i] == first and st[i] == '*':
                    st.pop(i)
                    st.insert(i, ws[i])
                    xx = ''.join(st)
                    ws = list(ws)
                    ws.pop(i)
                    ws.insert(i, '*')
                    wordlabel.configure(text=xx)
                    if xx == temp:
                        result.configure(text='CONGRATULATION YOU WON!!!')
                        text1 = "CONGRATULATION YOU WON!!!"
                        speak.say(text1)
                        ask = messagebox.askyesno("Notification", "\nDo you wish to play again?")
                        if ask:
                            result.configure(text='')
                            word_choice()
                        else:
                            root.destroy()
                    else:
                        break
        else:
            n -= 1
            chances_left.configure(text='Chances Left= {}'.format(n))
    else:
        text2 = "SAD YOU LOST!"
        speak.say(text2)
        result.configure(text='SAD YOU LOST!')
        ask = messagebox.askyesno("Notification", "\nDo you wish to play again?")
        if ask:
            result.configure(text='')
            word_choice()
        else:
            root.destroy()
    speak.runAndWait()


def click(event):
    hangman()


wordlist = ['lion', 'tiger', 'horse', 'camel', 'cat', 'dog', 'sheep', 'mammoth', 'cow', 'buffalo', 'koala']
root = Tk()
root.geometry('800x500+300+100')
root.configure(bg='tomato2')
root.iconbitmap('HM.ico')
root.title('Hangman Game')

# Labels
introlabel = Label(root, text="Hey there Let's play Hangman", font=('Cambria', 30, 'bold'), bg='tomato2')
introlabel.place(x=150, y=0)

wordlabel = Label(root, text='', font=('Calibri Light', 45), bg='tomato2')
wordlabel.place(x=260, y=150)

infolabel = Label(root, text='Type: Animals', font=('Calibri Light', 20), bg='tomato2')
infolabel.place(x=260, y=70)

chances_left = Label(root, text='', font=('Calibri Light', 20), bg='tomato2')
chances_left.place(x=600, y=100)

result = Label(root, text='', font=('arial', 20), bg='tomato2')
result.place(x=250, y=420)

# Entry Box
word = StringVar()
box1 = Entry(root, font=('Arial', 20), relief=GROOVE, bd=3, bg='peachPuff', justify='center', fg='grey16',
             textvariable=word, width=20)
box1.focus_set()
box1.place(x=250, y=230)

# Button
btn = Button(root, text='SUBMIT', font=('Cambria', 20), bd=3, width=8, bg='peachPuff', relief=RAISED,
             activebackground='ivory4', activeforeground='white', command=hangman)
btn.place(x=320, y=300)
root.bind("<Return>", click)


# word select


def word_choice():
    global ws, st, ws1, n, temp
    ws = random.choice(wordlist)
    st = ["*" for i in ws]
    ws1 = len(ws)
    n = 6
    temp = ws
    chances_left.configure(text='Chances Left= {}'.format(n))
    wd = ''
    for i in st:
        wd += i + ' '
    wordlabel.configure(text=wd)


word_choice()
root.mainloop()
