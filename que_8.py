# Q8. Some neat tricks up her sleeve:
# Looking at the below code, write down the final values of A0, A1, ...An

from functools import reduce

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
print(A0)
A1 = range(10)
print(A1)
A2 = sorted([i for i in A1 if i in A0])
print(A2)
A3 = sorted([A0[s] for s in A0])
print(A3)
A4 = [i for i in A1 if i in A3]
print(A4)
A5 = {i:i*i for i in A1}
print(A5)
A6 = [[i,i*i] for i in A1]
print(A6)
A7 = reduce(lambda x,y: x+y, [10,23, -45, 33])
print(A7)
A8 = list(map(lambda x: x*2, [1,2,3,4]))
print(A8)
A9 = list(filter(lambda x: len(x) >3, ["I" , "want", "to", "learn", "python"]))
print(A9)


# ------   OutPut   ------  #
A0 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
A1 = range(0, 10)
A2 = []
A3 = [1, 2, 3, 4, 5]
A4 = [1, 2, 3, 4, 5]
A5 = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
A6 = [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]
A7 = 21
A8 = [2, 4, 6, 8]
A9 = ['want', 'learn', 'python']

