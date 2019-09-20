import time

class BinarySearchTree:
  def __init__(self, value): # We're just using value, so key is value
    self.value = value
    self.left = None
    self.right = None

  # * `insert` adds the input value to the binary search tree, adhering to the
  # rules of the ordering of elements in a binary search tree.
  # Need to traverse to find spot to insert
  def insert(self, value):
    node = self
   
    traversing_nodes = True
    while traversing_nodes:
      if value >= node.value and node.right:
        node = node.right

      elif value < node.value and node.left:
        node = node.left

      elif value >= node.value and not node.right:
        node.right = BinarySearchTree(value)
        traversing_nodes = False


      elif value < node.value and not node.left:
        node.left = BinarySearchTree(value)
        traversing_nodes = False

    

  # * `contains` searches the binary search tree for the input value, 
  # returning a boolean indicating whether the value exists in the tree or not.
  # Start from root and traverse the tree
  # We can stop at the first instance of a value
  # We know it's not found if we get to a node that doesn't have children
  def contains(self, target):
    if self.value == None:
      return False
    elif target == self.value:
      return True
    elif target < self.value and self.left:
      return self.left.contains(target)
    elif target > self.value and self.right:
      return self.right.contains(target)
    else:
      return False



  # * `get_max` returns the maximum value in the binary search tree.
  def get_max(self):
    traversing_nodes = True
    node = self
    max = node.value
    while traversing_nodes:
      #still traversing the binary search tree for target while nodes still exist
      if node.right:
        node = node.right

      elif node.left:
        node = node.left

      elif node.value >= max:
        max = node.value
        traversing_nodes = False
      


    return max
 
  # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
  def in_order_dft():
      return 1

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
  def bft_print(node):
    print(node)

  # Print the value of every node, starting with the given node,
  # in an iterative depth first traversal
  def dft_print(node):
    return "ooga booga"

  # STRETCH Goals -------------------------
  # Note: Research may be required

  # Print In-order recursive DFT
  def pre_order_dft(self, node):
    return 1

  # Print Post-order recursive DFT
  def post_order_dft(self, node):
      pass


  # * `for_each` performs a traversal of _every_ node in the tree, executing
  # the passed-in callback function on each tree node value. There is a myriad of ways to
  # perform tree traversal; in this case any of them should work. 

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
#add first value to top of tree
node_tree = BinarySearchTree(names_1[0])
#add all the names to the tree
for i in range(len(names_1)):
    node_tree.insert(names_1[i])
for name in names_2:
    if node_tree.contains(name):
        duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
