from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)
def getWeather():
    try:
        our_city = textfield.get()
        geolocator=Nominatim(user_agent="geoapiExercises")
        loca= geolocator.geocode(our_city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=loca.longitude, lat=loca.latitude)

        home=pytz.timezone(result)
        lcl_time=datetime.now(home)
        crrnt_time=lcl_time.strftime("%I:%M %p ")
        clock.config(text=crrnt_time)
        name.config(text="CURRENT WEATHER")

        #weather
        lat=loca.latitude
        long=loca.longitude
        api_key="YOUR_API_KEY"
        api=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={api_key}"
        data_json=requests.get(api).json()
        cond=data_json['weather'][0]['main']
        desc= data_json['weather'][0]['description']
        temp=int(data_json['main']['temp']-273.15)
        pr=data_json['main']['pressure']
        humid=data_json['main']['humidity']
        wind=data_json['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(cond,"|","FEELS","LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humid)
        d.config(text=desc)
        p.config(text=pr)
    except Exception as e:
        messagebox.showerror(("Weather App","Invalid Entry!!"))




#search box
Search_image=PhotoImage(file="images/search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

Search_icon=PhotoImage(file="images/search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=34)
#logo
logo_image=PhotoImage(file="images/logo.png")
logo=Label(image=logo_image)
logo.place(x=150,y=100)

#Bottom box
Frame_img=PhotoImage(file="images/box.png")
frame_myimage=Label(image=Frame_img)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#label
label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)
d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=450,y=430)
p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)







root.mainloop()


