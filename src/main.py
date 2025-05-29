from tree.bintree import Tree


tree=Tree()

for value in [20, 10, 30, 5, 15, 25, 35]:
    tree.insert(value)



print(tree)
node=tree.search(15)

tree.remove(25)
tree.remove(20)
print(tree)

print(f'parent: {node.parent}')
