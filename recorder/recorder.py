img1 = Image.open("MAnav.jpg")
img1 = ImageTk.PhotoImage(img1)
l1 = Label(win,image=img1)
l1.image = img1  # keep a reference to the image
l1.place(x=20,y=20,height=200,width=460)

sec = Entry (win,font=(20))
sec.place( x = 150,y = 230, height=50, width=200 )

l2 = Label(win,text="Time in Sec", font=("Time New Roman",20), bg = "blue")
l2.place(x = 100 ,y = 290, height=50, width=300)

b = Button(win,text="Path", font=("Time New Roman",20), command= file_path)
b.place(x = 150,y = 350, height=50, width=200)

img2 = Image.open("poswa.png")
img2 = ImageTk.PhotoImage(img2)
start = Button(win,image=img2, command = save_file)
start.place(x=200,y = 410, height=100,width=100)

win.mainloop()
















#def savefile(sec):
#  print("start")
#  rece = sounddevice.rec(int(sec*44100), samplerate=44100, channels=2)
#  sounddevice.wait()
#  write("demo.wav", 44100, rece)
#  print("end")
  
#savefile(10)