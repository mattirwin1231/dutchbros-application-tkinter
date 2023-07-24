# Project1 - mbirwin - T/TH @ Noon

from os import path
from tkinter import *
from PIL import Image, ImageTk
import csv
import datetime
from time import *

import project1_backend

win = Tk()
win.title("Dutch Bros Mobile Ordering")
win.geometry('400x705')
win.columnconfigure(0, weight=1)  # content displayed in the center
win.config(bg='#156299')

checkvar1 = IntVar()
checkvar2 = IntVar()
checkvar3 = IntVar()
checkvar4 = IntVar()
checkvar5 = IntVar()
checkvar6 = IntVar()
checkvar7 = IntVar()
checkvar8 = IntVar()

checkvar1.set(0)
checkvar2.set(0)
checkvar3.set(0)
checkvar4.set(0)
checkvar5.set(0)
checkvar6.set(0)
checkvar7.set(0)
checkvar8.set(0)

name = StringVar()
name.set('')

name2 = StringVar()
name2.set('')

vehicle_type = StringVar()
vehicle_type.set('')

plate_number = StringVar()
plate_number.set('')

result = StringVar()
result.set('Please Press Submit to Order')

output = StringVar()
output.set('')

def close():
    win.destroy()


def vehicle():
    order_frame.grid_forget()
    car_frame.grid(columnspan=3)

def menu():
    car_frame.grid_forget()
    order_frame.grid(columnspan=3)


def submit_entry():
    output.set('')
    name1 = name2.get()
    try:
        vehicle_type1 = int(vehicle_type.get())
        if vehicle_type1 not in [1, 2, 3]:
            raise ValueError
    except (TypeError, ValueError):
        output.set('Error: Vehicle Type Must be 1-3')
        return
    plate_number1 = plate_number.get()
    project1_backend.VehicleRegistry.add_vehicle(name1, vehicle_type1, plate_number1)


# global variable
orders = []

def button_click():
    global orders

    if not path.isfile('orders.txt'):
        file = open('orders.txt', 'w')
        file.write('Coffee Ordering records: \n')
        file.close()

    if not path.isfile('orders.csv'):
        with open('orders.csv', 'w') as fp:
            data = csv.writer(fp)
            data.writerow(['Name', 'Time', 'Orders', 'Total Price'])

    orders = [checkvar1.get(), checkvar2.get(), checkvar3.get(), checkvar4.get(), checkvar5.get(), checkvar6.get(),
              checkvar7.get(), checkvar8.get()]

    orders = list(filter(None, orders))

    cost = len(orders) * 3.50

    with open("orders.txt", "a") as fp:
        now = datetime.datetime.now()
        order_string = ' '.join(str(order) for order in orders)
        fp.write(f'{name.get()} ordered {order_string} for ${cost:.2f} at {now}\n')

    with open('orders.csv', 'a') as f:
        writer = csv.writer(f)
        now = datetime.datetime.now()
        order_string1 = ' '.join(str(order) for order in orders)
        writer.writerow([name.get(), now.strftime('%Y-%m-%d %H:%M:%S'),
                         order_string1, f'{cost:.2f}'])

    name_parts = name.get().split()
    first_name = name_parts[0] if len(name_parts) > 0 else 'customer'
    result.set(f'Thank you {first_name}! Total cost is ${cost:.2f}')

    clear_checkboxes()

def clear_checkboxes():
    global orders

    c1.deselect()
    c2.deselect()
    c3.deselect()
    c4.deselect()
    c5.deselect()
    c6.deselect()
    c7.deselect()
    c8.deselect()
    name.set('')
    name2.set('')
    vehicle_type.set('')
    plate_number.set('')

    orders = set()


canvas = Canvas(win, width=330, height=160, highlightthickness=0, bg='#DA262E')
canvas.grid(columnspan=3, pady=20)

image = Image.open('coffee.png')
resize_image = image.resize((320, 150))
image = ImageTk.PhotoImage(resize_image)
image_label = Label(image=image, bg='#DA262E')
image_label.image = image
image_label.grid(column=0, row=0, columnspan=3, pady=25)

# First GUI Page frame
order_frame = Frame(win, width=400, height=800, bg='#156299')
order_frame.grid(columnspan=3)

# Create the greeting label
greeting_label = Label(order_frame, text="Welcome to Dutch Bros Coffee", font=("Verdana", 21), width=23, bg='white', fg='#156299')
greeting_label.grid(row=0, column=0, padx=10, pady=(5, 3), columnspan=3)

# Create the price label
price_label = Label(order_frame, text="Select Your Drink Type:", font=("Verdana", 14), width=36, bg='white', fg='#156299')
price_label.grid(row=1, column=0, padx=10, pady=(0, 3), columnspan=3)

price_label2 = Label(order_frame, text="All Drinks are $3.50", font=("Verdana Italic", 10), width=36, bg='#156299', fg='white')
price_label2.grid(row=3, column=0, padx=10, pady=0, columnspan=3)

# Create the checkbox frame
box1 = Frame(order_frame, bg='white', width=330, height=146, borderwidth=3, relief=RAISED)
box1.grid(row=2, column=0, columnspan=3, pady=(20, 0))
box1.grid_propagate(False)
box1.columnconfigure(0, weight=1)
box1.columnconfigure(1, weight=1)

# The 8 checkboxes
c1 = Checkbutton(box1, text="Iced Coffee", bg='#e3eeff', fg='#156299', bd=7, variable=checkvar1, font=("Verdana", 14), onvalue=1,
                 offvalue=0)
c1.grid(row=0, column=0, pady=0, sticky=EW)
c2 = Checkbutton(box1, text="Dutch Soda", bg='#e3eeff', fg='#156299', bd=7, variable=checkvar2, font=("Verdana", 14), onvalue=2,
                 offvalue=0)
c2.grid(row=1, column=0, pady=0, sticky=EW)
c3 = Checkbutton(box1, text="Dutch Rebel", bg='#e3eeff', fg='#156299', bd=7, variable=checkvar3, font=("Verdana", 14), onvalue=3,
                 offvalue=0)
c3.grid(row=2, column=0, pady=0, sticky=EW)
c4 = Checkbutton(box1, text="Iced Chai", bg='#e3eeff', fg='#156299', bd=7, variable=checkvar4, font=("Verdana", 14), onvalue=4,
                 offvalue=0)
c4.grid(row=3, column=0, pady=0, sticky=EW)
# 5-8
c5 = Checkbutton(box1, text="Hot Coffee", bg='#e3eeff', fg='#156299', bd=7, variable=checkvar5, font=("Verdana", 14), onvalue=5,
                 offvalue=0)
c5.grid(row=0, column=1, pady=0, sticky=EW)
c6 = Checkbutton(box1, text="Lemonade", bg='#e3eeff', fg='#156299', bd=7, variable=checkvar6, font=("Verdana", 14), onvalue=6,
                 offvalue=0)
c6.grid(row=1, column=1, pady=0, sticky=EW)
c7 = Checkbutton(box1, text="Smoothie", bg='#e3eeff', fg='#156299', bd=7, variable=checkvar7, font=("Verdana", 14), onvalue=7,
                 offvalue=0)
c7.grid(row=2, column=1, pady=0, sticky=EW)
c8 = Checkbutton(box1, text="Hot Chai", bg='#e3eeff', fg='#156299', bd=7, variable=checkvar8, font=("Verdana", 14), onvalue=8,
                 offvalue=0)
c8.grid(row=3, column=1, pady=0, sticky=EW)

name_label = Label(order_frame, text="Enter your name: ", font=("Verdana", 21), bg='white', fg="#156299", width=23)
name_label.grid(row=4, columnspan=3, column=0, padx=10, pady=10)

name_entry = Entry(order_frame, textvariable=name, justify=CENTER, font=('Verdana Bold', 20), width=21, fg="#156299")
name_entry.grid(row=5, column=0, columnspan=3, padx=30, pady=10)

results_label = Label(order_frame, fg='#DA262E', textvariable=result, font=("Verdana Bold", 12), bg='white', width=36)
results_label.grid(row=6, column=0, padx=30, pady=10, columnspan=3)

# Buttons
submit_button = Button(order_frame, command=button_click, font=("Verdana", 14), text='Submit Order', width=14, bg='white')
submit_button.grid(column=0, row=7, ipady=1, padx=(10, 0), pady=(15, 0), sticky=E)

clear_button = Button(order_frame, command=clear_checkboxes, font=("Verdana", 14), text='Clear', width=14, bg='white')
clear_button.grid(column=1, row=7, ipady=1, padx=(0, 10), pady=(15, 0), sticky=E)

vehicle_button = Button(order_frame, command=vehicle, font=("Verdana", 14), text='Vehicle Info', width=14, bg='white')
vehicle_button.grid(column=0, row=8, ipady=1, padx=(10, 0), pady=(10, 15), sticky=E)

exit_button = Button(order_frame, command=close, font=("Verdana", 14), text='Exit', width=14, bg='white')
exit_button.grid(column=1, row=8, ipady=1, padx=(0, 10), pady=(10, 15), sticky=E)

# 2nd GUI page for Curbside Pickup
car_frame = Frame(win, width=400, height=700, bg='#156299')
car_frame.grid(columnspan=3)

title_label2 = Label(car_frame, text="Order Pickup", font=("Verdana", 21), width=23, bg='white', fg='#156299')
title_label2.grid(row=0, column=0, padx=10, pady=(5, 3), columnspan=3)

name_label2 = Label(car_frame, text="Enter your name: ", font=("Verdana", 12), bg='white', fg="#156299", width=40)
name_label2.grid(row=1, columnspan=3, column=0, padx=10, pady=(35, 0))

name_entry2 = Entry(car_frame, textvariable=name2, justify=CENTER, font=('Verdana Bold', 20), width=21, fg="#156299")
name_entry2.grid(row=2, column=0, columnspan=3, padx=30, pady=10)

vehicle_label = Label(car_frame, text="Vehicle Type (1 for sedan, 2 for truck, 3 for other):", font=("Verdana", 12), width=40, bg='white', fg='#156299')
vehicle_label.grid(row=3, column=0, padx=10, pady=(15, 0), columnspan=3)

vehicle_entry = Entry(car_frame, textvariable=vehicle_type, justify=CENTER, font=('Verdana Bold', 20), width=21, fg="#156299")
vehicle_entry.grid(row=4, column=0, columnspan=3, padx=30, pady=10)

plate_label = Label(car_frame, text="Enter License Plate Number (XXX-XXX):", font=("Verdana", 12), width=40, bg='white', fg='#156299')
plate_label.grid(row=5, column=0, padx=10, pady=(15, 0), columnspan=3)

plate_entry = Entry(car_frame, textvariable=plate_number, justify=CENTER, font=('Verdana Bold', 20), width=21, fg="#156299")
plate_entry.grid(row=6, column=0, columnspan=3, padx=30, pady=10)

submit_button = Button(car_frame, command=submit_entry, font=("Verdana", 14), text='Submit Order', width=14, bg='white')
submit_button.grid(column=0, row=8, ipady=1, padx=(29, 0), pady=(15, 10), sticky=W)

clear_button = Button(car_frame, command=clear_checkboxes, font=("Verdana", 14), text='Clear', width=14, bg='white')
clear_button.grid(column=1, row=8, ipady=1, padx=(0, 29), pady=(15, 10), sticky=E)

output_label = Label(car_frame, fg='#DA262E', textvariable=output, font=("Verdana Bold", 12), bg='white', width=36)
output_label.grid(row=7, column=0, padx=30, pady=(15, 5), columnspan=3)

menu_button = Button(car_frame, command=menu, font=("Verdana", 14), text='Menu', width=14, bg='white')
menu_button.grid(column=0, row=9, ipady=1, padx=(29, 0), pady=(0, 15), sticky=W)

exit_button = Button(car_frame, command=close, font=("Verdana", 14), text='Exit', width=14, bg='white')
exit_button.grid(column=1, row=9, ipady=1, padx=(0, 29), pady=(0, 15), sticky=E)
