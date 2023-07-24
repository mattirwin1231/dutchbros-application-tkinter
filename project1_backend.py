# Project1 - mbirwin - T/TH @ Noon

import csv
import json
from os import path
import datetime
from time import *
import project1_GUI

class VehicleRegistry:
    registry = {}

    def __init__(self, name, vehicle_type, plate_number):
        self._name = name
        self._vehicle_type = vehicle_type
        self._plate_number = plate_number

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def vehicle_type(self):
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, vehicle_type):
        self._vehicle_type = vehicle_type

    @property
    def plate_number(self):
        return self._plate_number

    @plate_number.setter
    def plate_number(self, plate_number):
        self._plate_number = plate_number

    @classmethod
    def add_vehicle(cls, name, vehicle_type, plate_number):
        vehicle = {'vehicle_type': vehicle_type, 'plate_number': plate_number}
        if name in cls.registry:
            print('Car already registered.')
            project1_GUI.output.set('Car already waiting in line!')
        else:
            cls.registry[name] = vehicle
            print(VehicleRegistry.registry)
            project1_GUI.output.set('Success! Order will be delivered soon.')

            try:
                with open('vehicle_registry.json', 'r') as f:
                    data= json.load(f)
            except FileNotFoundError:
                data = dict()

            data[name] = vehicle
            with open('vehicle_registry.json', 'w') as f:
                json.dump(data, f)

def main():
    project1_GUI.win.resizable(False, False)
    project1_GUI.win.mainloop()


if __name__ == '__main__':
    main()