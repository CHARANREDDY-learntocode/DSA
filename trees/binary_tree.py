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


root = BinaryTreeNode("Root")
hot_drinks = BinaryTreeNode("Hot Drinks")
cold_drinks = BinaryTreeNode("Cold Drinks")
root.add_left_child(hot_drinks)
root.add_right_child(cold_drinks)
