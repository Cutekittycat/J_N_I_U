from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root=Tk()
root.geometry("800x900")
clock_image1 = ImageTk.PhotoImage(Image.open ("india.jpg"))
clock_image2 = ImageTk.PhotoImage(Image.open ("NZ.gif"))
clock_image3 = ImageTk.PhotoImage(Image.open ("usa.jpg"))
clock_image4 = ImageTk.PhotoImage(Image.open ("japan.jpg"))


india_label = Label(root,text="India")
india_label.place(relx=0.25,rely=0.20,anchor=CENTER)

india_clock=Label(root)
india_clock["image"]=clock_image1
india_clock.place(relx=0.25,rely=0.21,anchor=CENTER)

india_time=Label(root)
india_time.place(relx=0.25,rely=0.4,anchor=CENTER)

nz_label = Label(root,text="New Zealand")
nz_label.place(relx=0.75,rely=0.02,anchor=CENTER)

nz_clock=Label(root)
nz_clock["image"]=clock_image2
nz_clock.place(relx=0.75,rely=0.21,anchor=CENTER)

nz_time=Label(root)
nz_time.place(relx=0.75,rely=0.4,anchor=CENTER)

usa_label = Label(root,text="USA")
usa_label.place(relx=0.25,rely=0.5,anchor=CENTER)

usa_clock=Label(root)
usa_clock["image"]=clock_image3
usa_clock.place(relx=0.25,rely=0.69,anchor=CENTER)

usa_time=Label(root)
usa_time.place(relx=0.25,rely=0.88,anchor=CENTER)

japan_label = Label(root,text="Japan")
japan_label.place(relx=0.75,rely=0.5,anchor=CENTER)

japan_clock=Label(root)
japan_clock["image"]=clock_image4
japan_clock.place(relx=0.75,rely=0.69,anchor=CENTER)

japan_time=Label(root)
japan_time.place(relx=0.75,rely=0.88,anchor=CENTER)

class India():
    def times(self):
        home=pytz.timezone('Asia/Kolkata')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        india_time["text"]="Time : "+ current_time
        india_time.after(200,self.times)
        
class NewZealand():
    def times(self):
        home=pytz.timezone('Pacific/Auckland')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        nz_time["text"]="Time : "+ current_time
        nz_time.after(200,self.times)
        
class USA():
    def times(self):
        home=pytz.timezone('US/Central')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        usa_time["text"]="Time : "+ current_time
        usa_time.after(200,self.times)
        
class Japan():
    def times(self):
        home=pytz.timezone('Japan')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        japan_time["text"]="Time : "+ current_time
        japan_time.after(200,self.times)

obj_india=India()
obj_newzealand=NewZealand()
obj_usa=USA()
obj_japan=Japan()

india_btn=Button(root,text="Show Time",command=obj_india.times)
india_btn.place(relx=0.25,rely=0.44,anchor=CENTER)

nz_btn=Button(root,text="Show Time",command=obj_newzealand.times)
nz_btn.place(relx=0.75,rely=0.44,anchor=CENTER)

usa_btn=Button(root,text="Show Time",command=obj_usa.times)
usa_btn.place(relx=0.25,rely=0.92,anchor=CENTER)

japan_btn=Button(root,text="Show Time",command=obj_japan.times)
japan_btn.place(relx=0.75,rely=0.92,anchor=CENTER)
root.mainloop()