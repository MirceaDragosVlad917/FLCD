from Hashtable import HashTable
import unittest


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable()

    def test_hash(self):
        self.assertEqual(self.ht.hash("hello"), self.ht.hash("hello"))
        self.assertTrue(self.ht.hash("hello") < self.ht.capacity)

    def test_insert(self):
        self.assertEqual(self.ht.size, 0)
        self.ht.insert("key", "value")
        self.assertEqual(self.ht.size, 1)
        self.ht.insert("key", "value2")
        self.assertEqual(self.ht.buckets[self.ht.hash("key")].value, "value")
        self.assertNotEqual(self.ht.size, 2)

    def test_find(self):
        self.assertEqual(self.ht.size, 0)
        obj = "find"
        self.ht.insert("key1", obj)
        value, position = self.ht.find("key1")
        self.assertEqual(obj, value)
        self.assertEqual(0, position)
        obj = "find2"
        self.ht.insert("key2", obj)
        value, position = self.ht.find("key2")
        self.assertEqual(obj, value)
        self.assertEqual(0, position)

    def test_remove(self):
        self.assertEqual(self.ht.size, 0)
        obj = "remove"
        self.ht.insert("key1", obj)
        self.assertEqual(1, self.ht.size)
        self.assertEqual(obj, self.ht.remove("key1"))
        self.assertEqual(0, self.ht.size)
        self.assertEqual(None, self.ht.remove("key2"))

    def test_capacity(self):
        for i in range(0, 1000):
            self.assertEqual(i, self.ht.size)
            self.ht.insert("key" + str(i), "value")
        self.assertEqual(self.ht.size, 1000)
