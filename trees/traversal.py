class BinaryTreeNode:
    def __init__(self, data, right_child=None, left_child=None):
        self.__data = data
        self.__right_child = right_child
        self.__left_child = left_child

    def add_right_child(self, child):
        self.__right_child = child

    def add_left_child(self, child):
        self.__left_child = child

    def set_data(self, data):
        self.__data = data

    def preorder_traversal(self, node):
        if isinstance(node, BinaryTreeNode):
            print(f"{str(node.__data)} ->", end=" ")
            self.preorder_traversal(node.__left_child)
            self.preorder_traversal(node.__right_child)

    def inorder_traversal(self, node):
        if isinstance(node, BinaryTreeNode):
            self.inorder_traversal(node.__left_child)
            print(f"{node.__data} --> ", end="")
            self.inorder_traversal(node.__right_child)

    def post_order_traversal(self, node):
        if isinstance(node, BinaryTreeNode):
            self.post_order_traversal(node.__left_child)
            self.post_order_traversal(node.__right_child)
            print(f"{node.__data} --> ", end="")

    @staticmethod
    def level_order_traversal(node):
        from queue import Queue
        q = Queue()
        q.put(node)
        while not(q.empty()):
            new_node = q.get()
            print(f"{new_node.__data} -->", end="")
            if new_node.__left_child is not None:
                q.put(new_node.__left_child)
            if new_node.__right_child is not None:
                q.put(new_node.__right_child)


root = BinaryTreeNode("Root")
hot_drinks = BinaryTreeNode("Hot Drinks")
cold_drinks = BinaryTreeNode("Cold Drinks")
root.add_left_child(hot_drinks)
root.add_right_child(cold_drinks)
tea = BinaryTreeNode("Tea")
coffee = BinaryTreeNode("Coffee")
alcoholic = BinaryTreeNode("Alcoholic")
non_alcoholic = BinaryTreeNode("Non Alcoholic")
hot_drinks.add_left_child(tea)
hot_drinks.add_right_child(coffee)
cold_drinks.add_left_child(alcoholic)
cold_drinks.add_right_child(non_alcoholic)
print(f"PRE ORDER TRAVERSAL: ")
root.preorder_traversal(root)
print()
print("IN ORDER TRAVERSAL:")
root.inorder_traversal(root)
print()
print("POST ORDER TRAVERSAL:")
root.post_order_traversal(root)
print()
print("LEVEL ORDER TRAVERSAL:")
root.level_order_traversal(root)
