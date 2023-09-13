class Node(object):
    """
    This is for a singly linked list
    """

    # creation of nodes
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_data(self):
        return self.value

    def set_data(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

class LinkedList(object):
    """
    docstring
    """
    def __init__(self, head=None):
        self.head = head
        self.count = 0
        
    def get_count(self):
        return self.count
    
    def insert(self,data):
        # TODO insert a new node
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count+= 1
        
    def find(self,value):
        item = self.head
        while item != None:
          if item.get_data() == value:
              return item
          else:
              item = item.get_next()
        
    def deleteAt(self,idx):
        if idx > self.count -1:
            return
        
        if idx == 0:
            self.head = self.head.get_next()
    
        else:
            tempIdx = 0
            node = self.head
            while (tempIdx < idx -1):
                node = node.get_next()
                tempIdx += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1
            
    def dump_list(self):
        tempnode = self.head
        while (tempnode is not None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()
            
            
            
# create a linked list and insert some items
itemlist = LinkedList()
itemlist.insert(38)
itemlist.insert(49)
itemlist.insert(13)
itemlist.insert(15)
itemlist.dump_list()
# print(itemlist)
# exercise the list
# print("Item count: ", itemlist.get_count())
# print("Finding item: ", itemlist.find(13))
# print("Finding item: ", itemlist.find(78))

# delete an item
itemlist.deleteAt(3)
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(38))
itemlist.dump_list()