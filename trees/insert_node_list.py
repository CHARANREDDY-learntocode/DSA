class BinaryTree:
    def __init__(self, size: int):
        self.custom_list = [None] * size
        print(self.custom_list)
        self.last_used_index = 0
        self.max_size = size

    def insert_node(self, value):
        if self.max_size == self.last_used_index + 1:
            raise Exception("tree is full")
        self.custom_list[self.last_used_index + 1] = value
        self.last_used_index += 1

    def search_node(self, node_value):
        for index, value in enumerate(self.custom_list):
            if value == node_value:
                return index

    def pre_order_traversal(self, index=1):
        if index > self.last_used_index:
            return
        print(self.custom_list[index])
        self.pre_order_traversal(index*2)
        self.pre_order_traversal(index*2+1)

    def post_order_traversal(self, index=1):
        if index > self.last_used_index:
            return
        self.post_order_traversal(index * 2)
        self.post_order_traversal(index*2+1)
        print(self.custom_list[index])

    def level_order_traversal(self):
        print("\n".join(self.custom_list[1:self.last_used_index+1]))

    def inorder_traversal(self, index=1):
        if index > self.last_used_index:
            return
        self.inorder_traversal(index*2)
        print(self.custom_list[index])
        self.inorder_traversal(index*2 + 1)


tree = BinaryTree(15)
tree.insert_node("Drinks")
tree.insert_node("Cold Drinks")
tree.insert_node("Hot Drinks")
tree.insert_node("alcoholic")
tree.insert_node("non-alcoholic")
tree.insert_node("Coffee")
tree.insert_node("Tea")

print(f"Found at {tree.search_node('Cold Drinks')}")
tree.pre_order_traversal()
print("*********************************************")
tree.post_order_traversal()
print("*********************************************")
tree.level_order_traversal()
print("*********************************************")
tree.inorder_traversal()

