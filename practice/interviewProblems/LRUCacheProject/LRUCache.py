from ListNode import *

class LRUCache:
    head = ListNode("dummyHead", -1)
    tail = ListNode("dummyTail", -1)
    head.nextNode = tail
    tail.prevNode = head
    map = {}
    capacity = 2

    def __init__(self, capacity:int):
        self.capacity = capacity

    def put(self, key: str, val: int):

        if key in self.map:
            node = self.map[key]
            node.val = val
            self.removeNode(node)
            self.addNodeToHead(node)
            # update the value to the new value
            # remove the node from its current position
            # add the node to the self.head
        else:
            if len(self.map) > self.capacity:
                # remove the last node before tail
                # self.head <-> a <-> b <-> c <-> d <-> e <-> tail
                self.removeNode(self.tail.prevNode)
                
                del map[self.tail.prevNode]


                # remove key from map
            node = ListNode(key, val)
            self.addNodeToHead(node)
            self.map[key] = node

    def get(self, key):
        # if key does not exist, return -1
        # if key exists,
        # fetch the node
        # remove the node and add the node to self.head
        # return the node.val
        if key not in self.map:
            return -1
        else:
            node = self.map[key]
            self.removeNode(node)
            self.addNodeToHead(node)
            return node.val

    def removeNode(self, node):
        # self.head -> a -> b -> c -> d -> e ->
        # remove c
        prevNode = node.prevNode  # b
        nextNode = node.nextNode  # d

        if prevNode is not None:
            prevNode.nextNode = nextNode
        if nextNode is not None:
            nextNode.prevNode = prevNode

    def addNodeToHead(self, node):
        headNext = self.head.nextNode
        self.head.nextNode = node
        node.prevNode = self.head

        node.nextNode = headNext
        if headNext is not None:
            headNext.prevNode = node

    def display(self, node, direction):
        if direction == "forward":
            node1 = node
            while node1 is not None:
                print(node1.key)
                print("->")
                node1 = node1.nextNode
        else:
            node1 = node
            while node1 is not None:
                print(node1.key)
                print("->")
                node1 = node1.prevNode