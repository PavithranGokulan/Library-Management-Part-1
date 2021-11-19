from tkinter import *

main= Tk()
main.title("Tkinter")
main.geometry("500x300")
main.resizable(height=False,width=False)
main.configure(bg="#D4080C")
main.iconbitmap(r"C:/Users/pavig/OneDrive/Pictures/thalapathy.jfif")

#Label
label=Label(text="Pavithran",bg="#D4080C",font=("Brush Script MT",32),relief="solid",bd=5)
label.pack(pady=20)

#Getting entries
entry=Entry(width=25,font=("Baskerville Old Face",10),bg="#FFFFFF",fg="#000000",relief="sunken",bd=3,justify="center",show="#")
entry.pack(pady=20)

#Creating Buttons
def btn():
    print("Working Good!!!")
button=Button(text="tk",height=2,width=10,command=btn)
button.pack(pady=20)
main.mainloop()
