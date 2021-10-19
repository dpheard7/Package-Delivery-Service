
class ChainingHashTable:
    """
    Model for hash table used to store package objects for further retrieval. Generates a unique key based on the package ID.
    Time: O(N) due to insert function's proportionality to objects inserted.
    Space: O(N)
    """

    # Initializes hash table and sets initial capacity
    def __init__(self, initial_capacity=40):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Hashes key based on package ID and modulo operator against size of table
    def get_key(self, key):
        bucket = int(key) % len(self.table)
        return bucket

    # Inserts package
    # O(N)
    def insert(self, key, value):
        key_value = [key, value]
        package = self.get_key(key)
        package_list = self.table[package]
        for kv in package_list:
            if kv[0] == key:
                kv[1] = key_value

                return True
        package_list.append(key_value)
        return True

    # Searches for package
    def search(self, key):
        package = self.get_key(key)
        package_list = self.table[package]
        # print(f"package list: {package_list}")

        for pack in package_list:
            # print(f"search key: {key}")

            if pack[0] == key:
                return pack[1]
            else:
                print(f"Package ID {key} not found.\n"
                      f"Please try again.")

    # Removes package from hash table
    def remove(self, key):
        package = hash(key) % len(self.table)
        package_list = self.table[package]

        if key in package_list:
            package_list.remove(key)

    # Sets new package object
    @classmethod
    def set(cls, param, new_package):
        pass
