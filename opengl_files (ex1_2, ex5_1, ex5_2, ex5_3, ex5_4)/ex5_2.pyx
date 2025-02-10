cimport cython
import cython
from cython.parallel import parallel, prange

cdef class Node:
	cdef public int value
	cdef public Node left
	cdef public Node right

	def __init__(self, int value):
		self.value = value
		self.left = None
		self.right = None

cdef bint _search_subtree(Node node, int target, int level) nogil:
	if node is None:
		return False
	if node.value == target:
		return True

	cdef bint left_found = False
	cdef bint right_found = False

	if level > 0:
		with parallel():
			left_found = _search_subtree(node.left, target, level - 1)
			right_found = _search_subtree(node.right, target, level - 1)
			return left_found or right_found

	return _search_subtree(node.left, target, level - 1) or _search_subtree(node.right, target, level - 1)

def search_subtree(Node root, int target):
	max_depth = 6
	return _search_subtree(root, target, max_depth)