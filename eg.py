from Tkinter import *
root = Tk()

    #size of the window
root.geometry("800x800")

root.configure(background='peachpuff')
quitButton1 = Button( text="EXIT", width=25, bg="light blue",font="Times 20 bold")
        # placing the button on my window
quitButton1.place(x=250, y=400)
quitButton = Button(text="RESTART",bg="light blue",width=25,font="Times 20 bold")
label = Label(root, text="Your final score is", fg="black",width=25,bg="#FB0E4E",height=10,font="times 25 bold")
label1 = Label(root, text="WELL PLAYED ^__^",width=20,height=2, fg="black",bg="light blue",font="Times 45 bold")
label1.place(x=30,y=10)
label.place(x=150,y=200)

quitButton.place(x=200, y=600)
quitButton1.place(x=200, y=690)

root.mainloop()