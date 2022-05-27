class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def add_left_child(self, node):
        self.left_child = node

    def add_right_child(self, node):
        self.right_child = node

    def insert_node(self, root_node, new_node):
        from queue import Queue
        q = Queue()
        q.put(root_node)
        while not(q.empty()):
            node = q.get()
            if node.left_child is not None:
                q.put(node.left_child)
            else:
                node.left_child = new_node
                print(f"inserted as left child to {node.value}")
                return
            if node.right_child is not None:
                q.put(node.right_child)
            else:
                node.right_child = new_node
                print(f"inserted as right child to {node.value}")
                return

    @staticmethod
    def level_order_traversal(node):
        from queue import Queue
        q = Queue()
        q.put(node)
        while not (q.empty()):
            new_node = q.get()
            print(f"{new_node.value} -->", end="")
            if new_node.left_child is not None:
                q.put(new_node.left_child)
            if new_node.right_child is not None:
                q.put(new_node.right_child)


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

mul_1 = BinaryTreeNode(2500)

mul_4.insert_node(root, mul_1)
mul_4.level_order_traversal(root)

