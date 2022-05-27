class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def add_left_child(self, node):
        self.left_child = node

    def add_right_child(self, node):
        self.right_child = node

    @staticmethod
    def get_deepest_node(root_node):
        from queue import Queue
        q = Queue()
        q.put(root_node)
        while not(q.empty()):
            node = q.get()
            if node.left_child is not None:
                q.put(node.left_child)
            if node.right_child is not None:
                q.put(node.right_child)
        return node

    def delete_deepest_node(self, root_node, delete_node_1):
        from queue import Queue
        q = Queue()
        q.put(root_node)
        while not (q.empty()):
            node = q.get()
            if node.left_child == delete_node_1:
                node.left_child = None
            elif node.right_child == delete_node_1:
                node.right_child = None
                return
            else:
                if node.left_child is not None:
                    q.put(node.left_child)
                if node.right_child is not None:
                    q.put(node.right_child)

    def delete_node(self, root_node, node):
        from queue import Queue
        q = Queue()
        q.put(root_node)
        while not q.empty():
            root_1 = q.get()
            if root_1 == node:
                dnode = self.get_deepest_node(root_node)
                root_1.value = dnode.value
                self.delete_deepest_node(root_node, dnode)
                return
            if root_1.left_child is not None:
                q.put(root_1.left_child)
            if root_1.right_child is not None:
                q.put(root_1.right_child)
        return "Failed to delete node"

    w


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

root.level_order_traversal(root)
root.delete_node(root, mul_6)
print()
root.level_order_traversal(root)
