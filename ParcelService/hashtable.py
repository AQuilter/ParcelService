class HashTable:
    # CONSTRUCTOR
    def __init__(self, capacity=30):
        self.table = []
        for i in range(capacity):
            self.table.append([])

    # Uses a given key and value to insert an item into the hash table
    def insert(self, key, value):
        bucket_index = hash(key) % len(self.table)
        bucket_list = self.table[bucket_index]

        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = value
                return True

        key_value = [key, value]
        bucket_list.append(key_value)
        return True

    # Uses a given key to search for an item within the hash table
    def search(self, key):
        bucket_index = hash(key) % len(self.table)
        bucket_list = self.table[bucket_index]

        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
        return None

    # Uses a given key to delete an item from the hash table
    def delete(self, key):
        bucket_index = hash(key) % len(self.table)
        bucket_list = self.table[bucket_index]

        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove(kv)
                return

    # Formatted way to print contents of the hash table
    def print_contents(self):
        for index, bucket in enumerate(self.table):
            formatted_bucket = [f"[{str(value)}]" for key, value in bucket]
            print(f"{formatted_bucket}")

