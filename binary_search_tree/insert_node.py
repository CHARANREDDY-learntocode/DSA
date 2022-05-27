class BSTNode:
    def __init__(self, value):
        self.value = value
        self.right_child = None
        self.left_child = None

    def insert_node(self, _root_node, value):
        if not _root_node.value:
            _root_node.value = value
        elif value <= _root_node.value:
            if _root_node.left_child is None:
                _root_node.left_child = BSTNode(value)
            else:
                self.insert_node(_root_node.left_child, value)
        else:
            if _root_node.right_child is None:
                _root_node.right_child = BSTNode(value)
            else:
                self.insert_node(_root_node.right_child, value)

    def pre_order_traversal(self, _root_node):
        if _root_node is None:
            return
        else:
            print(_root_node.value)
            self.pre_order_traversal(_root_node.left_child)
            self.pre_order_traversal(_root_node.right_child)

    def post_order_traversal(self, _root_node):
        if _root_node is None:
            return
        else:
            self.post_order_traversal(_root_node.left_child)
            self.post_order_traversal(_root_node.right_child)
            print(_root_node.value)

    def in_order_traversal(self, _root_node):
        if _root_node is None:
            return
        else:
            self.in_order_traversal(_root_node.left_child)
            print(_root_node.value)
            self.in_order_traversal(_root_node.right_child)

    def level_order_traversal(self, _root_node):
        from queue import Queue
        q = Queue()
        q.put(_root_node)
        if not _root_node:
            return
        while not(q.empty()):
            current_node = q.get()
            print(current_node.value)
            if current_node.left_child is not None:
                q.put(current_node.left_child)
            if current_node.right_child is not None:
                q.put(current_node.right_child)

    def search(self, _root_node, value):
        if not _root_node:
            return Exception("Not found")
        node = _root_node
        while node:
            if node.value == value:
                print(f"found at {node.value}")
                return node
            if value <= node.value:
                node = node.left_child
            else:
                node = node.right_child
        return "Not found"

    def min_node(self, _root_node):
        current = _root_node
        while current.left_child:
            current = current.left_child
        return current

    def delete_node(self, _root_node, value):
        if _root_node is None:
            return _root_node
        if value > _root_node.value:
            _root_node.right_child = self.delete_node(_root_node.right_child, value)
        elif value < _root_node.value:
            _root_node.left_child = self.delete_node(_root_node.left_child, value)
        else:
            if _root_node.left_child is None:
                temp = _root_node.right_child
                _root_node = None
                return temp
            if _root_node.right_child is None:
                temp = _root_node.left_child
                _root_node = None
                return temp
            temp = self.min_node(_root_node.right_child)
            _root_node.value = temp.value
            _root_node.right_child = self.delete_node(_root_node.right_child, value)
        return _root_node

    def delete_bst(self, root_node):
        root_node.value = None
        root_node.left_child = None
        root_node.right_child = None
        print("deleted successfully")


root_node = BSTNode(None)
for i in range(0, 11):
    root_node.insert_node(root_node, i)
# root_node.insert_node(root_node, 70)
# root_node.insert_node(root_node, 50)
# root_node.insert_node(root_node, 90)
# root_node.insert_node(root_node, 30)
# root_node.insert_node(root_node, 60)
# root_node.insert_node(root_node, 80)
# root_node.insert_node(root_node, 100)
# root_node.insert_node(root_node, 20)
# root_node.insert_node(root_node, 40)
print("PRE ORDER TRAVERSAL ****************")
root_node.pre_order_traversal(root_node)
print("POST ORDER TRAVERSAL ****************")
root_node.post_order_traversal(root_node)
print("IN ORDER TRAVERSAL ****************")
root_node.in_order_traversal(root_node)
print("LEVEL ORDER TRAVERSAL ****************")
root_node.level_order_traversal(root_node)
print("SEARCH ****************")
root_node.search(root_node, 80)
print("DELETE NODE *************************")
root_node.delete_node(root_node, 30)
print("PRE ORDER TRAVERSAL ****************")
root_node.pre_order_traversal(root_node)
print("DELETE BST ****************")
root_node.delete_bst(root_node)
print("PRE ORDER TRAVERSAL ****************")
root_node.pre_order_traversal(root_node)

