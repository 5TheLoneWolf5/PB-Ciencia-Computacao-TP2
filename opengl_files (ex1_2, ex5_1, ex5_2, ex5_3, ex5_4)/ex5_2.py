#!/bin/python3

# class Node:
# 	def __init__(self, value):
# 		self.value = value
# 		self.left = None
# 		self.right = None

# def parallel_search(root, target):
# 	from multiprocessing import Process, Value

# 	def search_subtree(node, target, found):
# 		if node is None or found.value:
# 			return
# 		if node.value == target:
# 			found.value = True
# 			return
# 		search_subtree(node.left, target, found)
# 		search_subtree(node.right, target, found)

# 	found = Value('b', False)
# 	left_proc = Process(target=search_subtree, args=(root.left, target, found))
# 	right_proc = Process(target=search_subtree, args=(root.right, target, found))

# 	left_proc.start()
# 	right_proc.start()
# 	left_proc.join()
# 	right_proc.join()

# 	return found.value

# root = Node(15)
# root.left = Node(16)
# root.right = Node(9)
# root.left.left = Node(5)
# root.left.right = Node(8)

# if __name__ == "__main__":
# 	print(f"Encontrado: {parallel_search(root, 7)}")

import timeit

def time_tree_search(instructions):
	item = 1
	iterator = 32

	while not item > iterator:
		timeTaken = timeit.timeit(instructions, setup=f"""
from ex5_2 import Node, search_subtree\n\
import random\n\
\n\
def add_nodes(current, depth):\n\
	if depth == 0: # Chegou no limite de profundidade (de item à 0, voltar para cima).\n\
		return\n\
	depth -= 1\n\
	current.left = Node(random.randint(1, 1000))\n\
	add_nodes(current.left, depth)\n\
	current.right = Node(random.randint(1, 1000))\n\
	add_nodes(current.right, depth)\n\
root = Node(random.randint(1, 1000))\n\
if {item} > 1:\n\
		add_nodes(root, {item} // 2)
""", number=10)
		print(f"Tempo (AVG): {timeTaken} - {item}x o tamanho.")
		item = item * 2
	print()

if __name__ == "__main__":
	time_tree_search(
"random_num = random.randint(1, 1000)\n\
if search_subtree(root, random_num):\n\
		print(f'Valor {random_num} encontrado!')\n\
else:\n\
	print(f'Valor {random_num} não encontrado!')")