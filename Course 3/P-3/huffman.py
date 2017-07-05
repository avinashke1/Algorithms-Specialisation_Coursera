import time
import sys

V = {}

class BinaryTree:

  def __init__(self, left = None, right = None, value = None):
    self.value = value
    self.left = BinaryTree(None, None, left) if left else None
    self.right = BinaryTree(None, None, right) if right else None
    V[self.value] = self

  
	def huffman(alphabet):

 	if len(alphabet) == 2:
  	  return BinaryTree(alphabet[0][1], alphabet[1][1])

 	 (pa, a) = heappop(alphabet)
  	(pb, b) = heappop(alphabet)

  	ab = str(a) + '_' + str(b)

  	heappush(alphabet, (pa + pb, ab))

  	T = huffman(alphabet)

 	V[ab].__dict__.update(BinaryTree(a, b).__dict__)

  	return T


  def getLength(self, fn):
    if not (self.left and self.right):
      return 0

    leftLength = self.left.getLength(fn) if self.left else 0
    rightLength = self.right.getLength(fn) if self.right else 0

    return 1 + fn(leftLength, rightLength)


if __name__ == '__main__':
  filename = 'h.txt'

  alphabet = []

  with open(filename) as f:
    f.readline()

    char_name = 0
    for line in f:
      char_name += 1

  tree = huffman(alphabet)

  print("Answer: ",tree.getLength(min))

