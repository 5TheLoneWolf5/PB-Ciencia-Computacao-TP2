#!/bin/python3

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.root = None

	def insert_start(self, value):
		new_node = Node(value)

		if self.root is None:
			self.root = new_node
			return self.root

		new_node.next = self.root
		self.root = new_node
		return self.root

	def insert_end(self, value):
		new_node = Node(value)

		if self.root is None:
			self.root = new_node
			return self.root

		current = self.root
		while current.next is not None:
			current = current.next

		current.next = new_node

		return self.root

	def delete_val(self, value):
		# Function finds nodes based on the value and delete them.
		
		if self.root is None:
			print("Não existem dados nessa Lista Encadeada.")
			return

		found = False

		while self.root is not None and self.root.data == value:
			self.root = self.root.next
			found = True

		current = self.root

		while current is not None and current.next is not None: # "is not value" -> if one wants to stop at first find.
			if current.next.data == value:
				found = True
				follow = current.next
				if current.next.next is not None:
					current.next = follow.next
				else:
					current.next = None
			else:
				current = current.next
		if found == True:
			print(f"Valor(es) {value} encontrado(s) e removido(s) da lista encadeada.")
		else:
			print(f"Valor {value} não encontrado.")

	def find_pos_by_value(self, value):
		# First find.

		if self.root is None:
			print("Não existem dados nessa Lista Encadeada.")
			return

		pos = 1

		if self.root.data == value:
			return pos

		current = self.root
		found = False

		while current.data != value and current.next is not None:
			pos += 1
			if current.next.data == value:
				found = True
			current = current.next

		if found == False:
			return -1
		
		return pos

	def traverse(self):
		current = self.root

		while current is not None:
			print(current.data, end=" ")
			current = current.next

	def reverse(self):
		current = self.root
		prev = None

		while current is not None:
			next_node = current.next
			current.next = prev
			prev = current
			current = next_node

		self.root = prev

if __name__ == "__main__":
	linked_list = LinkedList()

	linked_list.insert_end(2)
	linked_list.insert_start(3)
	linked_list.insert_start(1)
	linked_list.insert_start(4)
	linked_list.insert_start(3)
	linked_list.insert_start(3)
	linked_list.insert_start(5)
	linked_list.delete_val(1)

	linked_list.traverse()

	linked_list.reverse()

	print("\nLista invertida:", end=" ")

	linked_list.traverse()

	print()

	linked_list_2 = LinkedList()

	linked_list_2.insert_end(5)
	linked_list_2.insert_start(4)
	linked_list_2.insert_start(4)
	linked_list_2.insert_start(4)
	linked_list_2.insert_start(2)
	linked_list_2.insert_start(6)
	linked_list_2.delete_val(2)

	linked_list_2.traverse()

	linked_list_2.reverse()

	print("\nLista invertida:", end=" ")

	linked_list_2.traverse()

	print()

	to_find = 6

	find_pos_5 = linked_list_2.find_pos_by_value(to_find)

	# Buscando na posição invertida.

	if find_pos_5 != -1:
		print(f"Valor {to_find} encontrado na posição: {find_pos_5}.")
	else:
		print(f"Valor {to_find} não encontrado.")