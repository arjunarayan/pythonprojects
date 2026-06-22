from contextlib import nullcontext
from operator import truediv

from ListNode import *
from LRUCache import *

# Example of creating nodes and linking them
if __name__ == "__main__":
    # 1. Using the default constructor (creates an empty node)



    lrucache1 = LRUCache(2)
    lrucache1.put("a", 1) # s
    lrucache1.put("b", 2) # s

    lrucache1.put("c", 3) # evict a
    print(lrucache1.get("a")) # return -1
    print(lrucache1.get("b")) # return 2

    lrucache1.put("d",4) # evict c
    print(lrucache1.get("c")) # return -1











