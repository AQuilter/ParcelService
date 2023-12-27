class Prompts:

    def intro(self, mileage):
        print("---" * 25)
        print("  " * 13 + "WGUPS ROUTING PROGRAM")
        print("---" * 25)
        print(f"Total mileage traveled by all trucks: {mileage:.1f}")


    def prompt_one(self):
        print("What would you like to do?:")
        # print("View status of ALL packages? (Enter 1)")
        # print("View status of an INDIVIDUAL package? (Enter 2)")
        print("View status of ALL packages at a specific TIME? (Enter 1)")
        answer = int(input("Input: "))
        return answer


# ---------- extra stuff for debuggin' (taken from main.py) ----

# -------- printing hash map -------
    # package_hash_map = load_package_data()
    # package_hash_map.print_contents()

    # for i in range(len(package_hash_map.table)):
    #     print((package_hash_map.search(i + 1)))

    # package_hash_map = load_package_data()
    # for package in package_hash_map:
    #     print(package)

    # print(package_hash_map.search(1))


#
#   first_input = prompt.prompt_one()
#   if first_input == 2:
#      print('WORKING')
#    else:
#       print("NOT WORKING")

# print all package status' at once (not sorted by truck)
    # for package_id in range(1, 41):
    #     package = package_hash_map.search(package_id)
    #     package.update_package_status(convert_time)
    #     print(f"{package.id}   {package.status}  {package.address}")
    #     # print(end='')