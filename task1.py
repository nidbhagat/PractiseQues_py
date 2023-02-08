"""
Task-
1. Take input(to ask how many items)
2. Ask which type of comprehension
3. Create comprehension
4. Print
"""
n = int(input('Enter the num of items:'))
list1=[]
for i in range(n):
  a = input(f'Enter the {i+1}item')
  list1.append(a)
print('Enter the comprehension to be converted:')
print('1->List\n2->Dict\n3->Set')
ch=int(input('Enter the choice:'))
if ch==1:
  print(list1)
elif ch==2:
  dict1={i:j for i,j in enumerate(list1)}
  print(dict1)
  print(type(dict1))
elif t==3:
  s={i for i in list1}
  print(s)
  print(type(s))
