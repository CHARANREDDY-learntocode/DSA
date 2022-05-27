class TreeNode:
    def __init__(self, data: any, childs=None):
        self.__data = data
        self.__childs = childs or []

    def __str__(self, level=0):
        if not level:
            expr = str(self.__data) + "\n"
        else:
            expr = "   " * (level-1) + "-"*(level-(level-1))+ str(self.__data) + "\n"
        for child in self.__childs:
            expr += child.__str__(level+1)
        return expr

    def add_child(self, children):
        if isinstance(self, TreeNode):
            return self.__childs.append(children)
        raise Exception


root = TreeNode("DRINKS")
hot_drinks = TreeNode("HOT DRINKS")
cold_drinks = TreeNode("COLD DRINKS")
root.add_child(hot_drinks)
root.add_child(cold_drinks)

tea = TreeNode("TEA")
coffee = TreeNode("COFFEE")
alcoholic = TreeNode("ALCOHOLIC")
non_alcoholic = TreeNode("NON-ALCOHOLIC")
hot_drinks.add_child(tea)
hot_drinks.add_child(coffee)
cold_drinks.add_child(alcoholic)
cold_drinks.add_child(non_alcoholic)

fresh_juice = TreeNode("FRESH JUICE")
beverages = TreeNode("BEVERAGES")
beer = TreeNode("BEER")
wine = TreeNode("WINE")
alcoholic.add_child(beer)
alcoholic.add_child(wine)
non_alcoholic.add_child(fresh_juice)
non_alcoholic.add_child(beverages)


print(root)



