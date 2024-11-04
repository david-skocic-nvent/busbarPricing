from Parsers import GroundParser
from threadingDriver.DriverController import DriverController
from drivers import GroundBarDriver
from constants import *
import time
import csv

# parse the input file
parser = GroundParser(GROUNDBAR_INPUT, GROUNDBAR_INTERMEDIATE)
parser.read_part_numbers()
parser.parse_all()
parser.write_csv()

controller = DriverController()
controller.make_drivers(1,GroundBarDriver,args=('usd',))

# Find all completed part numbers in the outputfile
completed_part_numbers = set()
try:
    with open(controller.drivers[0].outputpath, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            completed_part_numbers.add(row[0])
except FileNotFoundError:
    pass

# add all uncompleted part numbers to a list of tuples to pass into the driver controller
time.sleep(2)
tuple_list = []
with open(GROUNDBAR_INTERMEDIATE,newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['part number'] not in completed_part_numbers:
            tuple_list.append((row,))
controller.run_tests('run_test_case', tuple_list)