#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

from datetime import datetime
import requests
import pytz

# Initialize Tkinter window
root = Tk()
root.title("Weather App")
root.geometry("800x500+200+100")
root.resizable(False, False)

# Function to get weather data
def getWeather():
    city = textfield.get().strip()

    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    try:
        # Geolocation using Nominatim with user-agent
        geolocator = Nominatim(user_agent="your_weather_app")  
        location = geolocator.geocode(city)

        if location is None:
            messagebox.showerror("Error", "City not found. Please try again.")
            return

        # Get timezone
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        if result is None:
            messagebox.showerror("Error", "Could not determine timezone.")
            return

        # Get current time
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")

        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # OpenWeatherMap API request
        api_key = "7d81863a78b4cbd85e74ddd3add78b1c"  # Replace with your actual API key
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        response = requests.get(api_url)
        json_data = response.json()

        if response.status_code != 200:
            messagebox.showerror("Error", f"Weather API Error: {json_data.get('message', 'Unknown error')}")
            return

        # Extract weather data
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)  # Convert Kelvin to Celsius
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        # Update UI labels
        t.config(text=f"{temp}°C")
        c.config(text=f"{condition} | FEELS LIKE {temp}°C")
        w.config(text=f"{wind} m/s")
        h.config(text=f"{humidity}%")
        d.config(text=description)
        p.config(text=f"{pressure} hPa")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Network error: {e}")

# UI Components

# Search Box
Search_image = PhotoImage(file="Copy of search.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = PhotoImage(file="Copy of search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

# Logo
Logo_image = PhotoImage(file="Copy of logo.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=100)

# Bottom Box
Frame_image = PhotoImage(file="Copy of box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# Time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

# Labels
label1 = Label(root, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label4.place(x=610, y=400)

# Weather Data Labels
w = Label(root, text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)

h = Label(root, text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=250, y=430)

d = Label(root, text="...", font=("arial", 15, "bold"), bg="#1ab5ef")
d.place(x=450, y=430)

p = Label(root, text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=610, y=430)

# Temperature Display
t = Label(root, font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)

c = Label(root, font=("arial", 15, "bold"))
c.place(x=400, y=250)

# Run the application
root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




