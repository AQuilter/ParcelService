# Author: Ally Quilter
# Student ID: 010186766

import datetime
import prompts
import truck
from distance import nearest_neighbor_algorithm
from package import load_package_data
from hashtable import HashTable

# Manually loading the trucks
truck1_packages = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
truck2_packages = [3, 6, 12, 17, 18, 22, 23, 24, 26, 27, 35, 36, 38, 39, 25]
truck3_packages = [2, 4, 5, 7, 8, 9, 10, 11, 28, 32, 33, 21]
hub = "4001 South 700 East"

# Initialize truck objects
truck1 = truck.Truck(1, 18, 16, 0.0, hub, truck1_packages, datetime.timedelta(hours=8))
truck2 = truck.Truck(2, 18, 16, 0.0, hub, truck2_packages, datetime.timedelta(hours=9, minutes=5))
truck3 = truck.Truck(3, 18, 16, 0.0, hub, truck3_packages, datetime.timedelta(hours=10, minutes=20))

# Retrieving hash map data
package_hash_map = load_package_data()

# Calling algorithm for each truck. Truck3 is waiting until 10:21 so package #9 can have the corrected address,
# and to ensure truck1 has already finished delivering its packages.
nearest_neighbor_algorithm(truck1, package_hash_map)
nearest_neighbor_algorithm(truck2, package_hash_map)
truck3.departure_time = datetime.timedelta(hours=10, minutes=21)
nearest_neighbor_algorithm(truck3, package_hash_map)

# Summing up & displaying total milage across all trucks.
total_mileage = truck1.mileage + truck2.mileage + truck3.mileage

prompt = prompts.Prompts()
prompt.intro(total_mileage)

while True:
    try:
        time_input = input("Please enter a time (HH:MM:SS) to view status of packages: ")
        (h, m, s) = time_input.split(":")
        convert_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

        print(truck1.package_status_by_truck(package_hash_map, convert_time))
        print(truck2.package_status_by_truck(package_hash_map, convert_time))
        print(truck3.package_status_by_truck(package_hash_map, convert_time))
        break
    except ValueError:
        print("Invalid input. Please enter a time (HH:MM:SS).\n")
