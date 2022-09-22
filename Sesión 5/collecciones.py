import collections

nums = [1, 2, 3]

collec = collections.deque(nums)

print(collec)

collec.append(4)

print(collec)

collec.pop()

collec.pop()

collec.popleft()

print(collec)
