# number = 3

# if type(number) == int:
#     print("this is true")
# else:
#     print("this is false")
   

# difference between == and is        

list_1 = ['a', 'b', 'c']
list_2 = list_1
list_3 = list(list_1)

print(list_1)
print(list_2)
print(list_3)
print('------------------')

if list_1 == list_2:
    print('list_2 == list_2')
    print('list_2 == list_3')
print('------------------')
    
    