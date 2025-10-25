import array as ar
# a = ar.array('i', [1, 2, 3, 4, 5])
# print(a)
# print(ar.typecodes)
# print(a.itemsize)
# a.append(6)
# print(a)
# print(a.buffer_info())
# print(a.count(3))
# a.extend([7, 8, 9])
# print(a)
# a = ar.array('h', [10, 25, 9600, 32767])
# print(a)
# print(a.tobytes()) #b'\n\x00\x19\x00\x80%\xff\x7f'
# a.byteswap()
# print(a)
# print(a.tobytes()) #b'\x00\n\x00\x19%\x80\x7f\xff'
# a.byteswap()
# print(a)
# print(a.tobytes()) #b'\n\x00\x19\x00\x80%\xff\x7f'
# a = ar.array('h', [10, 12, 44, 5])
# print(len(a)) #4

# a = ar.array('h', [])
# n = int(input('n='))
# for i in range(1,n+1,1):
#     x = int(input('a('+str(i)+')='))
#     a.append(x)
# print(a)
# x = int(input('izlanayotgan son x='))
# if x in a:
#     z = a.index(x)
# else:
#     z = None
# while z!=None and z!=-1:
#     print(z, end='; ')
#     if x in a[z+1:]:
#         z = a.index(x,z+1)
#     else:
#         z = -1
# if z==None:
#     print('Topilmadi')
# else:
#     print(' indexlarda mavjud')