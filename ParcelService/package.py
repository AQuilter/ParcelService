import csv

from hashtable import HashTable


class Package:
    # CONSTRUCTOR
    def __init__(self, id, address, city, state, zip_code, deadline, weight, notes, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.departure_time = None
        self.delivery_time = None

    # String override for formatting
    def __str__(self):
        return f"Package ID: {self.id}... Address: {self.address}... City: {self.city}... State: {self.state}... " \
               f"Zip Code: {self.zip_code}... Deadline: {self.deadline}... Weight: {self.weight}... " \
               f"Notes: {self.notes}... Status: {self.status}"

    # Takes a given time and checks whether a pacakge has been delivered
    # or not, depending on the time given
    def update_package_status(self, time):
        if self.delivery_time < time:
            self.status = "Delivered"
        elif self.departure_time > time:
            self.status = "At hub"
        else:
            self.status = "En route"


# Initializing hash table
package_hash_table = HashTable()


# Reads in data from package.csv and creates package objects,
# then inserts package objects into hash table (package_hash_table).
def load_package_data():
    # package_list = []

    with open('CSV/Packages.csv') as packages:
        packageCSV = csv.reader(packages, delimiter=',')
        # packageCSV = list(packageCSV)
        # next(packageCSV)
        for package in packageCSV:
            id = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zip = package[4]
            deadline = package[5]
            weight = package[6]
            notes = package[7]
            status = "At hub"

            new_package = Package(id, address, city, state, zip, deadline, weight, notes, status)
            package_hash_table.insert(id, new_package)

        return package_hash_table
