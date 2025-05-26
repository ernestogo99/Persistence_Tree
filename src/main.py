from tree.bintree import Tree


tree=Tree()

tree.insert(1)
tree.insert(2)
tree.insert(3)
print(tree)
node=tree.search(2)
tree.print_tree()
print(node.parent)