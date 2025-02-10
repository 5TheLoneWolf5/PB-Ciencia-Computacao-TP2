#!/bin/python3

class DNode:
	def __init__(self, data):
		self.data = data
		self.prev = None
		self.next = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.last = None

	def insert_start(self, value):
		new_node = DNode(value)

		if self.head is None:
			self.last = new_node
		else:
			self.head.prev = new_node

		new_node.next = self.head
		self.head = new_node

	def insert_end(self, value):
		new_node = DNode(value)

		if self.head is None:
			self.last = new_node
		else:
			self.last.next = new_node
			new_node.prev = self.last

		self.last = new_node

	def delete_by_pos(self, pos):
		# Function finds nodes based on the value and deletes them.
		
		if self.head is None:
			print("Não existem dados nessa Lista Duplamente Encadeada.")
			return
		current = self.head

		for i in range(1, pos):
			if current is None:
				print("Posição não encontrada.")
				return
			current = current.next

		if current is None:
			return

		if current.prev is not None:
			current.prev.next = current.next
		
		if current.next is not None:
			current.next.prev = current.prev

		if self.head == current:
			self.head = current.next

	def traverse_forward(self):
		current = self.head

		while current is not None:
			print(current.data, end=" ")
			current = current.next
		print()

	def traverse_backward(self):
		current = self.last

		while current is not None:
			print(current.data, end=" ")
			current = current.prev
		print()

	def insertion_sort(self):
		if not self.head:
			print("Não existem dados nessa Lista Duplamente Encadeada.")
			return

		sorted_head = None
		current = self.head

		while current:
			next_node = current.next

			if not sorted_head or sorted_head.data >= current.data:
				current.next = sorted_head
				if sorted_head:
					sorted_head.prev = current
				sorted_head = current
				sorted_head.prev = None
			else:
				current_sorted = sorted_head

				while (current_sorted.next and current_sorted.next.data < current.data):
					current_sorted = current_sorted.next
				current.next = current_sorted.next

				if current_sorted.next:
					current_sorted.next.prev = current

				current_sorted.next = current
				current.prev = current_sorted

			current = next_node

		self.head = sorted_head

	def merge(self, new_doubly_head):

		if self.head is None:
			self.last = new_doubly_head
		else:
			self.last.next = new_doubly_head
			new_doubly_head.prev = self.last
		self.last = new_doubly_head

if __name__ == "__main__":
	linked_list = DoublyLinkedList()
	linked_list.insert_end(2)
	linked_list.insert_start(3)
	linked_list.insert_start(1)
	linked_list.insert_start(3)
	linked_list.insert_start(2)
	linked_list.traverse_forward()
	linked_list.traverse_backward()
	linked_list.delete_by_pos(2)
	linked_list.traverse_forward()
	linked_list.traverse_backward()

	print()

	linked_list_2 = DoublyLinkedList()

	linked_list_2.insert_end(5)
	linked_list_2.insert_start(4)
	linked_list_2.insert_start(3)
	linked_list_2.insert_start(4)
	linked_list_2.insert_start(2)
	linked_list_2.insert_end(4)
	linked_list_2.insert_end(10)
	linked_list_2.traverse_forward()
	linked_list_2.traverse_backward()
	linked_list_2.delete_by_pos(4)
	linked_list_2.traverse_forward()
	linked_list_2.traverse_backward()
	linked_list_2.insertion_sort()
	print("Lista duplamente encadeada ordenada (forward):", end=" ")
	linked_list_2.traverse_forward()
	print("Lista duplamente encadeada ordenada (backward):", end=" ")
	linked_list_2.traverse_backward()

	linked_list.merge(linked_list_2.head)
	linked_list.traverse_forward()