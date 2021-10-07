class ChainingHashTable:

    def __init__(self, initial_capacity=40):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def get_key(self, key):
        bucket = int(key) % len(self.table)
        return bucket

    def insert(self, key, value):

        bucket = hash(key) % len(self.table)
        package_list = self.table[bucket]

        for kv in package_list:
            if kv[0] == key:
                kv[1] = value
                return True
            else:
                self.table.append([key, value])

        key_value = [key, value]
        package_list.append(key_value)
        return True

    def search(self, key):
        package = hash(key) % len(self.table)
        package_list = self.table(package)

        if key in package_list:
            value_index = package_list.index(key)
            return package_list[value_index]
        else:
            print("Invalid key.")
            return None

    def remove(self, key):
        package = hash(key) % len(self.table)
        package_list = self.table[package]

        if key in package_list:
            package_list.remove(key)

    @classmethod
    def set(cls, param, new_package):
        pass
