# LRU置换算法

import random

physical_memory_size = 100
virtual_memory_size = 200

stack = []

access = 0
hit = 0

for i in range(1000):
    access += 1
    addr = int(random.random() * virtual_memory_size)
    # print(addr, stack)
    if addr in stack:
        hit += 1
        stack.remove(addr)
        stack.append(addr)
    elif len(stack) == physical_memory_size:
        stack.remove(stack[0])
        stack.append(addr)
    else:
        stack.append(addr)
print('缺页率：', (access - hit) / access)
