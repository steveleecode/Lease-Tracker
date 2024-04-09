import tkinter as tk
import tkinter.font as font
from tkinter import *
from bs4 import BeautifulSoup
from tkcalendar import Calendar
from datetime import datetime, timedelta


#Input Format: MM/DD/YY
def daysLeft(calendar):
    old_date = datetime.strptime(calendar.get_date(), "%m/%d/%y")
    current_date = datetime.now()

    # Calculate the difference between the current date and the specific date
    days_since = (current_date - old_date).days

    # Print the number of days since the specific date
    return days_since
    
    
        




def main_gui():
    
    # Create the main application window
    root = tk.Tk()
    root.title("Lease Tracker")  # Set the title of the window
    root.size()
    root.geometry("600x400")
    root.resizable(False, False)

    title = font.Font(size=25)
    body = font.Font(size=12)
    trackFont = font.Font(size=9)
    errorFont = font.Font(size=9, weight='bold')

    # Create a label widget
    label = tk.Label(root, text="Lease Tracker", font=title)
    label.pack(anchor='center')  # Use pack() method to add the label to the window

    lf = tk.LabelFrame(root)
    lf.pack(fill="both", expand="yes", padx=100, pady=25)
    
    # Add Calendar
    cal = Calendar(lf, selectmode = 'day',
               year = 2024, month = 3,
               day = 20)
 
    cal.pack(pady = 20)
    
    L_current_mil = Label(lf, text = "Current Miles on Odometer: ")
    L_current_mil.place(relx = 0.15, rely = 0.72)
    
    current_mil = Entry(lf)
    current_mil.place(relx = 0.55, rely = 0.72)
    
        
    
    LmilLeft = tk.Label(lf)
    LmilOverUnder = tk.Label(lf)
    
    def button_click():
        milesPerDay = 10000/365
        mpd_rounded = round(milesPerDay, 2)  # Round to 2 decimal places
        
        milLeft = daysLeft(cal) * mpd_rounded

        LmilLeft.config(text=("You should have " + str(milLeft) + " miles."))
        LmilLeft.place(relx=0.31, rely=0.85)
        
        milOverUnder = round(milLeft - int(current_mil.get()), 2)

        LmilOverUnder.config(text=((f"You are over by {str(abs(milOverUnder))} miles." ) if milOverUnder <= 0 else (f"You are under by {str(milOverUnder)} miles.")))
        LmilOverUnder.place(relx=0.31, rely=0.92)
        

    button = tk.Button(lf, text="Begin Tracking", command=button_click)
    button.place(relx = 0.5, rely = 0.01, anchor=CENTER)  # Add the button to the window

    # Run the Tkinter event loop
    root.mainloop()
    

if __name__ == "__main__":
    main_gui()