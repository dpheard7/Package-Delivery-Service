class ChainingHashTable:

    def __init__(self, initial_capacity=40):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def insert(self, key, item):
        package = hash(key) % len(self.table)
        package_list = self.table[package]

        for kv in package_list:
            if kv[0] == key:
                kv[1] = item
                return True

        value = [key, item]
        package_list.append(value)
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
