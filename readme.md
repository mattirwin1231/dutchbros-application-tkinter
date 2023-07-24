# Dutch Bros Mobile Ordering and Pickup Application

## Application Description
The Dutch Bros application allows users to
place drink orders right from the app rather
than having to walk up to the window. The app
allows users to view the drink menu, add menu
items to their order to calculate the total, and
enter in their vehicle information when arriving
for curbside pickup.

### Application GUI Pages
* Mobile Order Details ```(order_frame)```
* Vehicle Information Entry ```(car_frame)```

## Install Required Libraries

```shell
$ pip3 install PILLOW
$ pip3 install pytest
```

## To Run the Program
Click the green triangle run icon in the top-right corner of the PyCharm window
or click the green run icon next to the shell below:
```shell
$ python3 project1_backend.py
```

## Functionality
### Order Menu
On the first GUI page, several tkinter widgets are 
utilized in order to create a drink ordering system. 
The user first checks off which drinks they want to 
order and then type in their name to associate the
drink order with a name. Once the user presses the
submit button, the order total is calculated and then
shown to the user. Along with that, the transaction
data is also written to a .csv and .txt file.

### Vehicle Info
This function clears the current frame of the
ordering window and replaces it with the frame
for entering in vehicle information. This function
allows for a button to be clicked by the user to
switch from the menu page to the vehicle page. 

### Order Pickup Vehicle Information
The second GUI page contains a function that allows
for users to enter their name, their vehicle type (ranging
from 1 to 3), as well as their license plate number. This
information is used to tell the Dutch Bro's location
that the customer is in the parking lot and their 
order is ready to be delivered. This function takes this 
information and appends it to a json file. This way you
can see the different names along with their vehicle information.
Along with appending to a json file, success or error
messages are also displayed to the user for feedback.

### Return to menu
Similarly to the vehicle info function, the return to menu
button clears the vehicle information frame of the GUI and 
replaces it with the menu. This allows the user to go
back and forth between the two GUI pages. 

### Clear
This function allows the user to clear all the 
selected or input values in all GUI entry and checkbox
fields. This is useful when needing to quickly delete
what was typed in.

### Exit
The application will exit when the Exit button is clicked. 

## Data Files
### orders.csv
This contains transaction data in the following format. 

| Name    | Time                | Order Contents | Price |
|---------|---------------------|----------------|-------|
| Matthew | 2023-04-25 21:50:37 | 1,2,3,4        | 17.50 |
| Jackson | 2023-04-25 21:50:37 | 2,6,8          | 10.50 |

### orders.txt
This contains transaction data in the following format.
* ``"Name" ordered "Order Contents" for "Total Price" at "Time"``

### vehicle_registry.json
```json
{"Matthew": {"vehicle_type": 1, "plate_number": "XYZ-123"}}
```

## Class
### VehicleRegistry
#### Variables
Class Variables
1. registry: dictionary
2. vehicle: dictionary

Each Vehicles Instance has the following instance variables:
1. name: private, string data type
2. vehicle_type: private, integer data type
3. plate_number: private, string data type
4. name getter
5. name setter
6. vehicle_type getter
7. vehicle_type setter
8. plate_number getter
9. plate_number setter

#### Methods
The VehicleRegistry class has the following methods:

* The @classmethod add_vehicle
* The dunder "init" method
* The main() method

### GUI (Methods and Variables)
The GUI is not defined as a class however there
are several methods that use variables in order
to carry out certain essential functions.

#### Variables
1. checkvar(1-8): public, integer data type
2. name: public, string data type
3. name2: public, string data type
4. vehicle_type: public, string data type
5. plate_number: public, string data type
6. result: public, string data type
7. output: public, string data type
8. orders: public, list
9. cost: public, float data type

#### Methods
The GUI has the following methods:

* The close method which exits the window
* The menu method with switches from vehicle window to menu window
* The vehicle method with switches from menu window to vehicle window
* The submit_entry method which submits entered data to ```project1_backend.py```
* The button_click method which processes the menu and writes txt and csv files
* The clear_checkboxes method which clears all entry fields

## Auto Testing
Run the following command to test the test_vehicle.py file. This will run 3 test
cases. The first two test cases will pass, the third will not.

```shell
$ pip3 install pytest
$ pytest -v
```