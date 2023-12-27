import csv
import datetime
import enum

# Reads in the distance.csv data.
with open('CSV/distances.csv') as csv_file1:
    distances_csv = csv.reader(csv_file1, delimiter=',')
    distances_csv = list(distances_csv)

# Reads in the address.csv data.
with open('CSV/address.csv') as csv_file2:
    address_name_csv = csv.reader(csv_file2, delimiter=',')
    address_name_csv = list(address_name_csv)

    # Finds the distance between two given addresses, using the distances.csv file.
    def distance_in_between(x, y):
        distance = distances_csv[x][y]
        if distance == '':
            distance = distances_csv[y][x]

        return float(distance)

    # Takes an address (string) and returns the address' number (int).
    def extract_address(address):
        for row in address_name_csv:
            if address in row[2]:
                return int(row[0])

    # Implements the nearest neighbor algorithm to determine the delivery order of packages for a truck.
    # It iteratively selects the nearest undelivered package based on distance, updates the truck's information,
    # and assigns delivery times until all packages are delivered.
    def nearest_neighbor_algorithm(truck, package_hash_map):
        not_delivered = []

        # Add all packages from the truck to not_delivered
        for packageId in truck.packages:
            package = package_hash_map.search(packageId)
            not_delivered.append(package)
            # package.status = "En Route"

        # Clear the truck's packages list, since it will be repopulated in the algorithm later on.
        truck.packages.clear()

        while len(not_delivered) > 0:
            next_address = 100  # Some large arbitrary number
            next_package = None

            for package in not_delivered:
                # Calculate the distance between the current location of the truck and the address of the package
                distance_to_package = distance_in_between(extract_address(truck.current_location),
                                                          extract_address(package.address))

                # Check if the distance is <= to the current value of next_address
                if distance_to_package <= next_address:
                    next_address = distance_to_package
                    next_package = package

            # Add the ID of the package back to the truck's packages list
            truck.packages.append(next_package.id)
            # Remove package from not_delivered
            not_delivered.remove(next_package)

            # Update truck information (mileage, location, time)
            truck.mileage += next_address
            truck.current_location = next_package.address
            truck.time += datetime.timedelta(hours=next_address/18)

            # Update package delivery and departure times
            next_package.delivery_time = truck.time
            next_package.departure_time = truck.departure_time

