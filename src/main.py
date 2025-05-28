from tree.bintree import Tree


tree=Tree()

for value in [20, 10, 30, 5, 15, 25, 35]:
    tree.insert(value)



print(tree)
node=tree.search(15)
tree.print_tree()

print(f'parent: {node.parent}')
print(f'{tree.sucessor(20)}')
