# python3

import sys

class Queue:
	def __init__(self):
		self.container = []

	def add(self, element):
		self.container.append(element)

	def get(self):
		return self.container.pop(0)

	def empty(self):
		return len(self.container) == 0

class Node:
	def __init__(self, parent, value):
		self.value = value
		self.parent = parent
		self.childrens = []

	def addChildren(self, node):
		self.childrens.append(node)


class Tree:
	def read(self):
		self.root = -1
		self.n = int(sys.stdin.readline())

		elements = list(map(int, sys.stdin.readline().split())) # 4 -1 4 1 1

		self.nodes = self.buildTree(elements)

	def buildTree(self, elements):
		# create nodes
		nodes = [0] * self.n

		for index in range(self.n):
			parent = elements[index]
			value = index;

			if parent == -1:
				self.root = index

			nodes[index] = Node(parent, value)

		for index in range(self.n):
			parent = nodes[index].parent

			if parent != -1:
				nodes[parent].addChildren(nodes[index])

		return nodes

	def compute_height(self):
		# default, add tree root to queue
		currentLevelTreeQueue = Queue()
		currentLevelTreeQueue.add(self.nodes[self.root])

		levelQueuesArray = [currentLevelTreeQueue];
		level = 0;

		while len(levelQueuesArray) != 0:
			# get current level queue
			currentLevelNodes = levelQueuesArray.pop(0);
			level = level + 1;

			# create an queue for a next level
			nextLevelTree = Queue();
			hasNextLevel = False

			while not currentLevelNodes.empty():
				currentNode = currentLevelNodes.get()

				for index in range(len(currentNode.childrens)):
					nextLevelTree.add(currentNode.childrens[index])
					hasNextLevel = True

			if hasNextLevel:
					levelQueuesArray.append(nextLevelTree);

		print(level);


if __name__ == "__main__":
  tree = Tree()
  tree.read()
  tree.compute_height()