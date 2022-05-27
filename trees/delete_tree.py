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

    def get_data(self):
        return self.__data

    @staticmethod
    def delete_tree(root_node):
        root_node.__right_child = None
        root_node.__left_child = None
        root_node.__data = None

    @staticmethod
    def level_order_traversal(node):
        from queue import Queue
        q = Queue()
        q.put(node)
        while not (q.empty()):
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
root.level_order_traversal(root)
root.delete_tree(root)
print()
root.level_order_traversal(root)
