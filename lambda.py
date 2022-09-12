import operator 
d=[1,2,3,4,5]
select=operator.itemgetter(1)

print(select(d))