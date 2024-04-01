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
    lf.pack(fill="both", expand="yes", padx=100, pady=50)
    
    # Add Calendar
    cal = Calendar(lf, selectmode = 'day',
               year = 2020, month = 5,
               day = 22)
 
    cal.pack(pady = 20)
    
        
    
    milLeft = tk.Label(lf)
    
    def button_click():
        milLeft.config(text=("You should have " + str(daysLeft(cal) * (10000/360)) + " miles."))
        milLeft.place(relx=0.2, rely=0.9)
        

    button = tk.Button(lf, text="Begin Tracking", command=button_click)
    button.place(relx = 0.5, rely = 0.01, anchor=CENTER)  # Add the button to the window

    # Run the Tkinter event loop
    root.mainloop()
    

if __name__ == "__main__":
    main_gui()