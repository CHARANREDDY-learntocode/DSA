class BinaryTreeNode:
    def __init__(self, value):
        self.__value = value
        self.__left_child = None
        self.__right_child = None

    def add_left_child(self, node):
        self.__left_child = node

    def add_right_child(self, node):
        self.__right_child = node

    def search(self, value):
        from queue import Queue
        q = Queue()
        q.put(self)
        while not(q.empty()):
            node = q.get()
            if node.__value == value:
                print("Found")
                return value
            if node.__left_child is not None:
                q.put(node.__left_child)
            if node.__right_child is not None:
                q.put(node.__right_child)


root = BinaryTreeNode(50)

mul_9 = BinaryTreeNode(45)
mul_8 = BinaryTreeNode(40)
root.add_left_child(mul_9)
root.add_right_child(mul_8)

mul_7 = BinaryTreeNode(35)
mul_6 = BinaryTreeNode(30)
mul_9.add_right_child(mul_6)
mul_9.add_left_child(mul_7)

mul_5 = BinaryTreeNode(25)
mul_4 = BinaryTreeNode(20)
mul_8.add_left_child(mul_5)
mul_8.add_right_child(mul_4)

print(root.search(250))