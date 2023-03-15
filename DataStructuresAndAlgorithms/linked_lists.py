class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
head = Node(4)
nodeB = Node(2)
nodeC = Node(10)
nodeD = Node(2)
nodeE = Node(12)

head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
# This is a function that takes one head variable and return the number of links 
# in the whole list
def countNodes(head):
    cnt = 1
    while head.next is not None:
        cnt += 1
        head = head.next
    return print(cnt)
countNodes(head)