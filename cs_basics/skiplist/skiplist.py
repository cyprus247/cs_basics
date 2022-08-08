import random


class Node:
    def __init__(self, key, level):
        self.key = key

        # list to hold references to node of different level
        self.next = [None] * (level + 1)


class SkipList:
    """ Skiplist class
        :parameter max_lvl Maximum level for this skip list
        :parameter p float between 0.1 and 1
    """
    def __init__(self, max_lvl: int, p: float):
        self.MAXLVL = max_lvl

        # P is the fraction of the nodes with level
        # i references also having level i+1 references
        self.P = p

        # create header node and initialize key to -1
        self.header = self.create_node(self.MAXLVL, -1)

        # current level of skip list
        self.level = 0

    # create  new node
    def create_node(self, lvl, key):
        n = Node(key, lvl)
        return n

    # create random level for node
    def random_level(self):
        lvl = 0
        while random.random() < self.P and lvl < self.MAXLVL:
            lvl += 1
        return lvl

    # insert given key in skip list
    def insert_element(self, key):
        # create update array and initialize it
        update = [None] * (self.MAXLVL + 1)
        current = self.header

        """
        start from highest level of skip list
        move the current reference forward while key 
        is greater than key of node next to current
        Otherwise inserted current in update and 
        move one level down and continue search
        """
        for i in range(self.level, -1, -1):
            while current.next[i] and current.next[i].key < key:
                current = current.next[i]
            update[i] = current

        """ 
        reached level 0 and forward reference to 
        right, which is desired position to 
        insert key.
        """
        current = current.next[0]

        """
        if current is NULL that means we have reached
           to end of the level or current's key is not equal
           to key to insert that means we have to insert
           node between update[0] and current node
       """
        if current == None or current.key != key:
            # Generate a random level for node
            rlevel = self.random_level()

            """
            If random level is greater than list's current
            level (node with highest level inserted in 
            list so far), initialize update value with reference
            to header for further use
            """
            if rlevel > self.level:
                for i in range(self.level + 1, rlevel + 1):
                    update[i] = self.header
                self.level = rlevel

            # create new node with random level generated
            n = self.create_node(rlevel, key)

            # insert node by rearranging references
            for i in range(rlevel + 1):
                n.next[i] = update[i].next[i]
                update[i].next[i] = n

            print("Successfully inserted key {}".format(key))

    def delete_element(self, search_key):

        # create update array and initialize it
        update = [None] * (self.MAXLVL + 1)
        current = self.header

        """
        start from highest level of skip list
        move the current reference forward while key 
        is greater than key of node next to current
        Otherwise inserted current in update and 
        move one level down and continue search
        """
        for i in range(self.level, -1, -1):
            while current.next[i] and current.next[i].key < search_key:
                current = current.next[i]
            update[i] = current

        """ 
        reached level 0 and advance reference to 
        right, which is possibly our desired node
        """
        current = current.next[0]

        # If current node is target node
        if current != None and current.key == search_key:

            """
            start from lowest level and rearrange references
            just like we do in singly linked list
            to remove target node
            """
            for i in range(self.level + 1):

                """
                If at level i, next node is not target
                node, break the loop, no need to move
                further level
                """
                if update[i].next[i] != current:
                    break
                update[i].next[i] = current.next[i]

            # Remove levels having no elements
            while self.level > 0 and self.header.next[self.level] == None:
                self.level -= 1
            print("Successfully deleted {}".format(search_key))

    def search_element(self, key):
        current = self.header

        """
        start from highest level of skip list
        move the current reference forward while key 
        is greater than key of node next to current
        Otherwise inserted current in update and 
        move one level down and continue search
        """
        for i in range(self.level, -1, -1):
            while current.next[i] and current.next[i].key < key:
                current = current.next[i]

        # reached level 0 and advance reference to
        # right, which is possibly our desired node
        current = current.next[0]

        # If current node have key equal to
        # search key, we have found our target node
        if current and current.key == key:
            print("Found key ", key)
        else:
            print(f'could not find {key}')

    # Display skip list level wise
    def display_list(self):
        print("\n*****Skip List******")
        head = self.header
        for lvl in range(self.level , 0, -1):
            print("Level {}: ".format(lvl), end=" ")
            node = head.next[lvl]
            while node is not None:
                print(node.key, end=" ")
                node = node.next[lvl]
            print("")


# test above code

if __name__ == '__main__':

    lst = SkipList(5, 0.5)
    lst.insert_element(3)
    lst.insert_element(6)
    lst.insert_element(7)
    lst.insert_element(9)
    lst.insert_element(12)
    lst.insert_element(19)
    lst.insert_element(17)
    lst.insert_element(26)
    lst.insert_element(21)
    lst.insert_element(25)
    lst.display_list()

    # Search for node 19
    lst.search_element(19)
    lst.search_element(55)

    # Delete node 19
    lst.delete_element(19)
    lst.display_list()

