from methods_of_hash import *
class Node:
    def __init__(self, data=None, value=None):
        self.data = data
        self.value = value
        self.next = None

class HashTableC:
    def __init__(self, size=0):
        self.data = [Node() for i in range(size)]
        self.size = size

    def put(self, key, value, num_method):

        hash_value = type_of_hash(num_method, key, self.size)

        if self.data[hash_value].data is None:
            self.data[hash_value].data = key
            self.data[hash_value].value = value
        else:
            temp = Node(key, value)
            p = self.data[hash_value]
            while p.next is not None:
                p = p.next
            p.next = temp

    def get(self, key, num_method):

        hash_value = type_of_hash(num_method, key, self.size)

        if self.data[hash_value].data == key:
            return self.data[hash_value].value
        else:
            p = self.data[hash_value]
            while p is not None and p.data != key:
                p = p.next

            if p is not None and p.data == key:
                return self.data[hash_value].value
        return False

    def delete(self, key, num_method):
        if not self.get(key, num_method):
            return 'Key was not found'

        hash_value = type_of_hash(num_method, key, self.size)

        if self.data[hash_value].data == key:
            self.data[hash_value].data = None
            self.data[hash_value].value = None

        else:
            p = self.data[hash_value]
            pre = None
            while p is not None and p.data != key:
                pre = p
                p = p.next

            if p.data == key:
                pre.next = p.next
            else:
                return 'Delete Error'
        return 'The element was successfully deleted'

    def show(self):
        print(f'Hash table size: {self.size}')
        for i in range(self.size):
            print(i, '-', self.data[i].data, ':', self.data[i].value)
            p = self.data[i]
            while p.next is not None:
                p = p.next
                print('node:', i, '-', p.data, ':', p.value)


    def delete_all(self):
        self.data = [Node() for i in range(0)]
        self.size = 0


