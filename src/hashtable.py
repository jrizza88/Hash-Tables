# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count_entries = 0  # current number of items, used to set index of added values

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash 

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

        
    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # pass

        # index via hash method
        idx = self._hash_mod(key)
        print('idx', idx)
        # head = self.storage[idx]  # stores idx into variable called head
        # head = LinkedPair(key, value)
        # # if head is None:
        # #     head = LinkedPair(key, value)
        # #     print(head)
        # #     self.count_entries += 1

        if self.storage[idx] is None:
            self.storage[idx] = LinkedPair(key, value)
            print(self.storage[idx])
            self.count_entries += 1
        else:
        # if self.storage[idx] is not None:
        #     head.next = self.storage[idx]
        #     print('self.storage[idx]', self.storage[idx])
        #     print('head.next', head.next)
        #     self.count_entries += 1
        # self.storage[idx] = head
            current = self.storage[idx]
            if current.key == key:
                current.value = value
                print('value', value)
                return
            while current.next is not None:
                # if next is none, make the current.next the LinkedPair
                current = current.next
                print(current)
                if current.key == key:
                    current.value = value
                    print('value2', value)
                    return
            # if current.next is None:
            current.next = LinkedPair(key, value)
            self.count_entries += 1
            # return
        # else:
            
        #     # linked list 
        #     current = self.storage[idx]
        #     if current.key == key:
        #         current.value = value
        #         print('value', value)
        #         return key
        #     while current.next is not None:
        #         # if next is none, make the current.next the LinkedPair
        #         current = current.next
        #         print(current)
        #         if current.key == key:
        #             current.value = value
        #             print('value2', value)
        #             return value
        #     # if current.next is None:
        #         current.next = LinkedPair(key, value)
        #         self.count_entries += 1
        #         return current.next




    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        #pass
        idx = self._hash_mod(key)
        
        current = self.storage[idx]
        if current is None:
            return current
        if current.key == key:
            self.storage[idx] = current.next
            return
        new_node = current.next
        while new_node is not None:
            if current.next.key == key:
                current.key = new_node.key
                return
            new_node.next = None
    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
      
        idx = self._hash_mod(key)
        current = self.storage[idx]
        while current is not None:
        # if next is none, make the current.next the LinkedPair
        
            print(current)
            if current.key == key:
                print('value2', current.value)
                return current.value
            current = current.next
        return None
            


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
