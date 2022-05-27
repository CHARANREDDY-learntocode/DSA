class AVLNode:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.height = 1

    def pre_order_traversal(self, root_node):
        if root_node is not None:
            print(root_node.value)
            self.pre_order_traversal(root_node.left_child)
            self.pre_order_traversal(root_node.right_child)

    def in_order_traversal(self, root_node):
        if root_node is not None:
            self.in_order_traversal(root_node.left_child)
            print(root_node.value)
            self.in_order_traversal(root_node.right_child)

    def post_order_traversal(self, root_node):
        if root_node is not None:
            self.post_order_traversal(root_node.left_child)
            self.post_order_traversal(root_node.right_child)
            print(root_node.value)

    def level_order_traversal(self, root_node):
        from queue import Queue
        if root_node is not None:
            q = Queue()
            q.put(root_node)
        while not(q.empty()):
            current_node = q.get()
            print(current_node.value)
            if current_node.left_child is not None:
                q.put(current_node.left_child)
            if current_node.right_child is not None:
                q.put(current_node.right_child)

    def search_node(self, root_node, value):
        if root_node is not None:
            if value > root_node.value:
                self.search_node(root_node.right_child, value)
            elif value < root_node.value:
                self.search_node(root_node.left_child, value)
            else:
                print("Node found")
                return root_node

    @staticmethod
    def get_height(root_node):
        if not root_node:
            return 0
        return root_node.height

    def right_rotate(self, unbalanced_node):
        new_root = unbalanced_node.left_child
        unbalanced_node.left_child = unbalanced_node.left_child.right_child
        new_root.right_child = unbalanced_node
        unbalanced_node.height = 1 + max(self.get_height(unbalanced_node.left_child) ,
                                         self.get_height(unbalanced_node.right_child))
        new_root.height = 1 + max(self.get_height(new_root.left_child), self.get_height(new_root.right_child))
        return new_root

    def left_rotate(self, unbalanced_node):
        new_root = unbalanced_node.right_child
        unbalanced_node.right_child = new_root.right_child.left_child
        new_root.left_child = unbalanced_node
        unbalanced_node.height = 1 + max(self.get_height(unbalanced_node.left_child),
                                         self.get_height(unbalanced_node.right_child))
        new_root.height = 1 + max(self.get_height(new_root.left_child), self.get_height(new_root.right_child))
        return new_root

    def get_balance(self, root_node):
        if not root_node:
            return 0
        return self.get_height(root_node.left_child) - self.get_height(root_node.right_child)

    def insert_node(self, root_node, value):
        if not root_node:
            return AVLNode(value)
        elif value < root_node.value:
            root_node.left_child = self.insert_node(root_node.left_child, value)
        else:
            root_node.right_child = self.insert_node(root_node.right_child, value)
        root_node.height = 1 + max(self.get_height(root_node.left_child), self.get_height(root_node.right_child))
        balance = self.get_balance(root_node)
        if balance > 1 and value < root_node.left_child.value:
            return self.right_rotate(root_node)
        if balance > 1 and value > root_node.left_child.value:
            root_node.left_child = self.left_rotate(root_node.left_child)
            return self.right_rotate(root_node)
        if balance < -1 and value > root_node.right_child.value:
            return self.left_rotate(root_node)
        if balance < -1 and value < root_node.right_child.value:
            root_node.right_child = self.right_rotate(root_node.right_child)
            return self.left_rotate(root_node)
        return root_node

    def get_min_value_node(self, root_node):
        if not root_node or root_node.left_child is None:
            return root_node
        return self.get_min_value_node(root_node.left_child)

    def delete_node(self, root_node, value):
        if not root_node:
            return
        if value > root_node.value:
            root_node.right_child = self.delete_node(root_node.right_child, value)
        elif value > root_node.value:
            root_node.left_child = self.delete_node(root_node.left_child, value)
        else:
            if root_node.left_child is None:
                temp = root_node.right_child
                root_node = None
                return temp
            if root_node.right_child is None:
                temp = root_node.left_child
                root_node = None
                return temp
            temp = self.get_min_value_node(root_node.right_child)
            root_node.value = temp.value
            root_node.right_child = self.delete_node(root_node.right_child, temp.value)
        balance = self.get_balance(root_node)
        if balance > 1 and self.get_balance(root_node.left_child) >= 0:
            return self.left_child(root_node)
        if balance < -1 and self.get_balance(root_node.right_child) <= 0:
            return self.right_rotate(root_node)
        if balance > 1 and self.get_balance(root_node.right_child) < 0:
            root_node.left_child = self.left_rotate(root_node.left_child)
            return self.right_rotate(root_node)
        if balance < -1 and self.get_balance(root_node.left_child) > 0:
            root_node.right_child = self.right_rotate(root_node.right_child)
            return self.right_rotate(root_node)
        return root_node

    def delete_tree(self, root_node):
        root_node.value = None
        root_node.left_child = None
        root_node.right_child  = None
        print("tree deleted successfully")


avl_tree = AVLNode(5)
avl_tree = avl_tree.insert_node(avl_tree, 10)
avl_tree = avl_tree.insert_node(avl_tree, 15)
avl_tree = avl_tree.insert_node(avl_tree, 20)
avl_tree = avl_tree.delete_node(avl_tree, 15)
avl_tree = avl_tree.delete_node(avl_tree, 5)
# avl_tree.pre_order_traversal(avl_tree)
# avl_tree.in_order_traversal(avl_tree)
# avl_tree.post_order_traversal(avl_tree)
avl_tree.level_order_traversal(avl_tree)
# avl_tree.search_node(avl_tree, 20)
avl_tree.delete_tree(avl_tree)
