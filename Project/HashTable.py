class ChainingHashTable:

    def __init__(self, initial_capacity=40):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def get_key(self, key):
        bucket = int(key) % len(self.table)
        return bucket

    def insert(self, key, value):
        key_value = [key, value]
        package = self.get_key(key)
        package_list = self.table[package]
        for kv in package_list:
            if kv[0] == key:
                kv[1] = key_value

                return True
            # package_list.append(key_value)

        package_list.append(key_value)
        return True

    def search(self, key):
        package = self.get_key(key)
        package_list = self.table[package]
        # print(f"package list: {package_list}")

        for pack in package_list:
            print(f"search key: {key}")

            if pack[0] == key:
                return pack[1]
            else:
                print(f"Key {key} is invalid.")

        # for package in package_list:
        #     if package in package_list:
        #         value_index = package_list.index(key)
        #         return package[1]
        #     else:
        #         print(f"Key {key} is invalid.")
        #         return package

    def remove(self, key):
        package = hash(key) % len(self.table)
        package_list = self.table[package]

        if key in package_list:
            package_list.remove(key)

    @classmethod
    def set(cls, param, new_package):
        pass
