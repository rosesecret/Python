from tkinter import *
window = Tk()

window.geometry('700x300+250+150')
window.config(background='dark grey')
window.title('Cyber Security')



Canvas = Canvas (window ,width=800,height=400)
Canvas.pack()


img = PhotoImage(file="mylogo.png")
Canvas.create_image(0,0,image=img,anchor=NW)


myLabel1 = Label(window,width=5,font=('Times',12,'bold'),fg='black',text='المصطلح')
myLabel1.place(x=850,y=15)


المصطلح = Entry(window,width=20,font=('Times',12,'bold'),bg='light grey',fg='black',bd=4,justify='center')
المصطلح.place(x=650,y=15)



btn_submit = Button(window,width=5,font=('Times',12,'bold'),bd=4,text='تنفيذ',bg='light grey',fg='black',padx=3,pady=0)
btn_submit.place(x=740,y=55)

btn_submit = Button(window,width=5,font=('Times',12,'bold'),bd=4,text='مسح',bg='light grey',fg='black',padx=3,pady=0)
btn_submit.place(x=660,y=55)


window.mainloop()
