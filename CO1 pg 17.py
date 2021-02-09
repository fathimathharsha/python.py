import operator
a={1: 2, 3: 4, 4: 3, 2: 1, 0: 0, 5: 6, 6: 5}
l=sorted(a.items(),key=operator.itemgetter(1))
print('ascending order:',l)
l1=dict(sorted(a.items(), key=operator.itemgetter(1),reverse=True))
print('descending order:',l1)