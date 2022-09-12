grade=[('a','apple',70),
('b','basketball',93),
('c','cat',79)
]

def aaa(d):
     return (d[2])
output=[]
for a,b,c in reversed(sorted(grade,key=aaa)):
      output.append(f'{a}{b}{c}')
for i in output:
      print(i)






 
