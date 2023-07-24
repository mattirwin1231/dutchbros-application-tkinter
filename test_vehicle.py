from project1_backend import VehicleRegistry

class TestVehicle:
    def test_case(self):
        test = VehicleRegistry('Matthew', 1, 'CWU086')
        print('Testing Vehicle File')
        assert('Matthew', 1, 'CWU086') == (test.name, test.vehicle_type, test.plate_number)

    def test_case2(self):
        test1 = VehicleRegistry('Elva', 2, '123456')
        print('Testing Vehicle File')
        assert('Elva', 2, '123456') == (test1.name, test1.vehicle_type, test1.plate_number)

    def test_case3(self):
        test2 = VehicleRegistry('WalkUp', 3, 'NoCar')
        print('Testing Vehicle File')
        assert('WalkUp', 3, 'None') == (test2.name, test2.vehicle_type, test2.plate_number)