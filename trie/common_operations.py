class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_string = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_string(self, string: str):
        current = self.root
        for i in string:
            ch = i
            node = self.root.children.get(ch)
            if not node:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.end_of_string = True
        print("Inserted Successfully")

    def search_string(self, string: str):
        current_node = self.root
        for i in string:
            node = current_node.children.get(i)
            if node is None:
                return False
            current_node = node
        if current_node.end_of_string:
            return True
        return False


trie = Trie()
trie.insert_string("Hello")
trie.insert_string("Hell")
print(trie.search_string("Hell"))
