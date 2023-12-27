class Truck:

    # CONSTRUCTOR
    def __init__(self, id, speed, capacity, mileage, current_location, packages, departure_time):
        self.id = id
        self.speed = speed
        self.capacity = capacity
        self.mileage = mileage
        self.current_location = current_location
        # self.next_location = next_location
        self.packages = packages
        self.departure_time = departure_time
        self.time = departure_time

    # String format override
    def __str__(self):
        return (f"Truck ID: {self.id}, Speed: {self.speed}, Milage: {self.mileage:.1f}, "
                f"Location: {self.current_location}, Packages: {self.packages}, Departure Time: {self.departure_time}")

    # Method iterates through a list of package ID's, retrieves the
    # corresponding package object, then sorts them into lists depending on whether
    # they have been delivered or not by the given time.
    def package_status_by_truck(self, package_hash_map, convert_time):
        delivered = []
        en_route = []
        at_hub = []
        for package_id in self.packages:
            package = package_hash_map.search(package_id)
            package.update_package_status(convert_time)
            if package.status == "Delivered":
                delivered.append((package.id, str(package.delivery_time)))
            elif package.status == "En route":
                en_route.append(package.id)
            else:
                at_hub.append(package.id)

        formatted_line = (f"-----------\n"
                          f"CURRENT TIME: {convert_time}\n"
                          f"TRUCK #{self.id}\n"
                          f"Delivered: {delivered} \n"
                          f"En route: {en_route}\n"
                          f"At hub: {at_hub}")
        return formatted_line

