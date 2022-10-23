class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return "<Node: (%s, %s), next: %s>" % (self.key, self.value, self.next != None)

    def __repr__(self):
        return str(self)


class HashTable:
    def __init__(self):
        self.capacity = 47
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        """
        This function computes the hashcode of a given key
        :param key: string, the key that is hashed
        :return: the hash as the absolute value of the remainder of the division of the hash code of the key to the capacity of the table
        """
        hashsum = abs(hash(key) % self.capacity)
        return hashsum

    def insert(self, key, value):
        """
        This function adds an element of the type (key, value) to the hash table
        :param key: string, the key to be added
        :param value: string, the value to be added to the corresponding key
        :return: -
        """
        index = self.hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(key, value)
            self.size += 1
            return
        prev = node
        while node is not None:
            prev = node
            if prev.key == key:
                return
            node = node.next
        self.size += 1
        prev.next = Node(key, value)

    def find(self, key):
        """
        This function finds the key in the hash table, if it exists
        :param key: string, the key that is searched for
        :return: None, if the key does not exist
                 The value of the key and it's index in the bucket
        """
        index = self.hash(key)
        node = self.buckets[index]
        i = 0
        while node is not None and node.key != key:
            node = node.next
            i += 1
        if node is None:
            return None
        else:
            return node.value, i

    def remove(self, key):
        """
        This function deletes a node from the hash table based on the given key
        :param key: string, the key to be deleted
        :return: None, if the key does not exist
                 The value of the node that is deleted
        """
        index = self.hash(key)
        node = self.buckets[index]
        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            if prev is None:
                self.buckets[index] = node.next
            else:
                prev.next = prev.next.next
            return result
