from tkinter import*
from PIL import Image, ImageTk
import speechtotext
import action
from texttospeech import texttospeech

root = Tk()
root.title("AI Assistant")
root.geometry("565x675")
root.resizable(False, False)
root.config(bg="#FFB38E")

#ask function
def ask():
    user_val = speechtotext.speechtotext()
    bot_val = action.Action(user_val)
    text.insert(END, 'User-->'+user_val+"\n")
    if bot_val is not None:
         text.insert(END, "Bot<--"+str(bot_val)+"\n")
         texttospeech(str(bot_val), rate=70)
    if bot_val == "ok sir":
        root.destroy()
#ask function
def delete():
    text.delete("1.0", "end")


#ask function
def send():
    send = entry.get()
    entry.delete(0, END) 
    bot = action.Action(send)
    text.insert(END, "User<--"+send+"\n")
    if bot != None:
         text.insert(END, "Bot<--"+str(bot)+"\n")
    if bot == "ok sir":
        root.destroy()

#create a frame
frame = LabelFrame(root, padx = 100, pady = 7, borderwidth = 8, relief= "raised")
# frame.config(bg="#6B6FAF")
frame.grid(row = 0, column = 1, padx = 55, pady = 10)

#textlabel

test_label = Label(frame, text="AI Assistant", font=("comic Sans ms", 14, "bold"), bd=5 , fg="#356696")
test_label.grid(row = 0, column = 0, padx = 20, pady = 10)

#img label
image = ImageTk.PhotoImage(Image.open("image/assistant.png"))
image_label = Label(frame, image=image)
image_label.grid(row = 1, column = 0, pady=20)

#add text widget

text = Text(root, font=("courier 10 bold"), bg="#FFFDCB")
text.grid(row=2, column=0)
text.place(x=100, y=400, width=375, height=100)

#entry widget

entry = Entry(root, justify=CENTER)
entry.place(x=100, y=510, width=375, height=30)

#button1

button1 = Button(root, text="ASK", bg="#FFFDCB", pady=16, padx=40, borderwidth=4, relief=GROOVE , command=ask)
button1.place(x=70, y=575)

button2 = Button(root, text="DELETE", bg="#FFFDCB", pady=16, padx=40, borderwidth=4, relief=GROOVE , command=delete)
button2.place(x=380, y=575)

button3 = Button(root, text="SEND", bg="#FFFDCB", pady=16, padx=40, borderwidth=4, relief=GROOVE , command=send)
button3.place(x=225 , y=575)
root.mainloop()