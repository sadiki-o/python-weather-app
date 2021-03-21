import requests
from tkinter import *
import json
from PIL import ImageTk, Image  
import os

#root 
app = Tk()
a_height = 450
a_width = 800
app.title("Weather app")
app.geometry(f"{800}x{450}")


def search():
    #json key
    api_key = "6162e8e5b11a60cff9a204c1ba036e05"
    #api request link
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_entry.get()}&appid={api_key}"
    #json respond
    json_data = requests.get(url).json()
    #image path
    path = f"{os.path.dirname(os.path.realpath(__file__))}\weather_icons\{json_data['weather'][0]['icon']}@2x.png"
    #change image
    stgImg = PhotoImage(file=path)
    img.configure(image=stgImg)
    img.image = stgImg
    #update location
    location_lbl['text'] = f"Location : {city_entry.get()}  {json_data['sys']['country']}"
    #update temp
    temp_lbl['text'] = f"Temperature : {round(json_data['main']['temp'] - 273.15, 2)}°C"
    #update weather
    weather_lbl['text'] = f"Weather state : {json_data['weather'][0]['main']}\n {json_data['weather'][0]['description']}"
    #update max, min, humidity
    max_lbl['text'] = f"Max temperature : {round(json_data['main']['temp_max'] - 273.15, 2)}°C"
    min_lbl['text'] = f"Min temperature : {round(json_data['main']['temp_min'] - 273.15, 2)}°C"
    hum_lbl['text'] = f"Humidity : {json_data['main']['temp_min']}"
    




#city field
city_entry = Entry(app, text='', width=40)
city_entry.pack()

#search Button
search_btn = Button(app, text='Search Weather', width=12, command=search, bg="yellow", fg="black")
#binding key to a button function
app.bind('<Return>', (lambda event: search()))
search_btn.pack()

#location field
location_lbl = Label(app, text='', font=('bold', 20))
location_lbl.pack()

#image Field
img = Label(app, image=None)
img.pack()

#temperature field
temp_lbl = Label(app, text='', font=('bold', 15))
temp_lbl.pack()

#weather field
weather_lbl = Label(app, text='', font=('bold', 15))
weather_lbl.pack()

#max temp
max_lbl = Label(app, text='', font=('bold', 15))
max_lbl.pack()

#min temp
min_lbl = Label(app, text='', font=('bold', 15))
min_lbl.pack()

#humidity
hum_lbl = Label(app, text='', font=('bold', 15))
hum_lbl.pack()


#start app
app.mainloop()