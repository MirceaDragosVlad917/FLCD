class HashTable:
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.data = [None for i in range(self.capacity)]

    def hash(self, value):
        """
        This function computes the hashcode of a given value
        :param value: integer, the value to be hashed
        :return: integer, the hash as the absolute value of the remainder of the division of the hash code of the value to the capacity of the table
        """
        hashsum = abs(hash(value) % self.capacity)
        return hashsum

    def insert(self, value):
        """
        This value adds a value to the hash table, based on its hash
        :param value: integer, the value to be added
        :return: False, if the value already exists in the hash table
                 The position where the value is added
        """
        position = self.hash(value)

        if self.data.__contains__(value):
            return False

        while self.data[position] is not None and self.data[position] != value:
            position = position + 1
            position = position % self.capacity

        self.data[position] = value
        self.size = self.size + 1
        return position

    def find(self, value):
        """
        This function finds the value in the hash table, if it exists
        :param value: integer, the value that is searched for
        :return: -1, if the value is not found
                 The position where the value is found in the hash table
        """
        position = self.hash(value)
        if self.data[position] == value:
            return position

        index = position + 1
        while self.data[index] != value and index != position:
            index += 1
            index %= self.capacity
        if index == position:
            return -1
        return index

    def __str__(self) -> str:
        print(self.data)
