from methods_of_hash import *
class HashTableO:
    def __init__(self, size=0):
        self.size = size
        self.data = [None] * self.size
        self.value = [None] * self.size


    def put(self, key, data, num_method, zond_type):

        hash_value = type_of_hash(num_method, key, len(self.data))

        stop = True
        step = 1
        if self.data[hash_value] is None:
            self.data[hash_value] = key
            self.value[hash_value] = data
        else:
            nextdata = self.rehash(hash_value, len(self.data), zond_type, step)
            step += 1
            while self.data[nextdata] is not None and stop:
                nextdata = self.rehash(hash_value, len(self.data), zond_type, step)
                step += 1
                if hash_value == nextdata:
                    if zond_type == 1:
                        stop = False
                    else:
                        for i in range(len(self.data)):
                            if self.data[i] is None:
                                stop = True
                                break
                            else:
                                stop = False

            if self.data[nextdata] is None and self.data[nextdata] != key:
                self.data[nextdata] = key
                self.value[nextdata] = data
            else:
                # n = input()
                print('Array is overflowing', hash_value, nextdata)


    def rehash(self, oldhash, size, zond_type, step):
        if zond_type == 1:
            return (oldhash+step) % size
        else:
            return (oldhash+(step*step)) % size


    def get(self, key, num_method, zond_type):

        startdata = type_of_hash(num_method, key, len(self.data))

        step = 1
        position = startdata

        if self.data[position] == key:
            return self.value[position]

        else:
            while self.data[position] is not None and self.data[position] != key:
                position = self.rehash(startdata, len(self.data), zond_type, step)
                step += 1
                if position == startdata:
                    if zond_type == 1:
                        return False
                    else:
                        for i in range(len(self.data)):
                            if self.data[i] is None:
                                break
                            else:
                                return False
            if self.data[position] is not None and self.data[position] == key:
                return self.value[position]
        return False

    def dell(self, key, num_method, zond_type):
        if self.get(key, num_method, zond_type) == 'Value was not found':
            return 'Delete Error'

        startdata = type_of_hash(num_method, key, len(self.data))

        position = startdata
        stop = True
        step = 1
        if self.data[position] == key:
            self.data[position] = None
            self.value[position] = None
        else:
            while self.data[position] is not None and self.data[position] != key and stop:
                position = self.rehash(startdata, len(self.data), zond_type, step)
                step += 1
                if position == startdata:
                    if zond_type == 1:
                        return False
                    else:
                        for i in range(len(self.data)):
                            if self.data[i] is None:
                                break
                            else:
                                return False

            if self.data[position] is not None and self.data[position] == key:
                self.data[position] = None
                self.value[position] = None
                return 'The element was successfully deleted'
            else:
                return 'Value was not found'

    def show(self):
        print(f'Hash table size: {self.size}')
        for i in range(self.size):
            print(i, '- Key: ', self.data[i], ',', 'Value: ', self.value[i])

    def delete_all(self):
        self.size = 0
        self.data = [None] * self.size
        self.value = [None] * self.size



