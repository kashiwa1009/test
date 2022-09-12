def aaa(data,*,start=0,end=0):
    for value in (data[start:end]):
        print(value)
data=["a","c","d","e"]
print(aaa(data))
