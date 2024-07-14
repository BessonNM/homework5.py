immutable_var = 58, 12, 'EKB', True
print(immutable_var)

# immutable_var[0] = 200   - 'нельзя заменять элементы кортежа'
# print(immutable_var)

mutable_list = ['hello', 5, False, 22]
print(mutable_list)
mutable_list[3] = 44
mutable_list.append('MCK')
print(mutable_list)
