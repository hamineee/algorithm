class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"
    
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append_val(self, x):
        if not isinstance(x, Node):
                x = Node(x)
        if self.head == None:
            self.head = x
        else:
            self.tail.next = x
        self.tail = x
        
    def __str__(self):
        to_print = ""
        curr = self.head
        while curr is not None:
            to_print += str(curr.data) + "->"
            curr = curr.next
        if to_print:
            return "[" + to_print[:-2] + "]"
        return "[]"
    
    def add_to_start(self, x):
        if not isinstance(x, Node):
            x = Node(x)
        x.next = self.head
        self.head = x
        
    def search_val(self, x):
        bucket = []
        curr = self.head
        while curr is not None:
            bucket.append(curr)
            curr = curr.next
        found_node = False
        for index,node in enumerate(bucket):
            if x == node.data:
                found_node = True
                break
        if found_node:
            return f'{x} found index {index}'
        else:
            return f'No node found with {x}'

    def search_val(self,x):
        curr = self.head
        found_node = False
        while curr is not None:
            if curr.data == x:
                found_node = True
                return curr
            else:
                curr = curr.next 
        if found_node == False:
            return f'{x} not found in the list'
        
            
    def remove_val_by_index(self, x):
        bucket = []
        curr = self.head
        while curr is not None:
            bucket.append(curr)
            curr = curr.next
        found_index = False
        for index,node in enumerate(bucket):
            if x == index:
                found_index = True
                break    
        if found_index:
            bucket.remove(bucket[index])
        else:
            return f'No node found with index{x}'


    def length(self):
        bucket = []
        curr = self.head
        while curr is not None:
            bucket.append(curr)
            curr = curr.next
        return len(bucket)

    def reverse_list_recur(self, current, previous):
        self.head = current
        

Node1 = Node(7)
Node2 = Node(1)
my_lst = LinkedList()

my_lst.append_val(5)
my_lst.append_val(9)
my_lst.append_val(3)
my_lst.append_val(Node1)
my_lst.append_val(Node2)

print(my_lst)
print(my_lst.search_val(6))
print(my_lst.search_val(7))
my_lst.add_to_start(10)
print(my_lst)
print(my_lst.length())
