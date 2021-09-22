from tkinter import *
from gtts import gTTS  # common writing
from playsound import playsound  # common writing

root = Tk()
root.geometry('350x300')
root.configure(bg='black')
root.title("Text to Speech Project")

msg = StringVar()

Label(root,
      fg='ghost white',
      bg='black',
      font='Times 20 normal',  # bold, normal, underline, italic
      text='Text to Speech').pack(side=TOP)
Label(root,
      fg='ghost white',
      bg='black',
      font='Times 12 italic',
      text='Isac E Perez',
      width=20).place(x=245, y=270)

Label(root,
      fg='ghost white',
      bg='black',
      font='Times 14 italic',
      text='Enter your text here: ').place(x=20, y=60)

text_entry = Entry(root,
                   fg='ghost white',
                   bg='navy',
                   font='Times 14 italic',
                   textvariable=msg,
                   width=20)
text_entry.place(x=20, y=100)


def TtS():
    message = text_entry.get()
    speech = gTTS(message, lang='en')  # text is the sentence or text to be read
    # speech stores the converted voice from the text
    speech.save('Isac.mp3')  # saves the file
    playsound('Isac.mp3')  # used to play the sound


def Exit():
    root.destroy()


def Reset():
    msg.set("")

Button(root,
       fg='black',
       font='Times 14 italic',
       text='Play',
       command=TtS,
       width=4).place(x=25, y=140)

Button(root,
       fg='black',
       font='Times 14 italic',
       text='Exit',
       command=Exit,
       width=4).place(x=100, y=140)

Button(root,
       fg='black',
       font='Times 14 italic',
       text='Reset',
       command=Reset,
       width=6).place(x=175, y=140)

root.mainloop()
