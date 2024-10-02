#immutable_var = 1, 2 , 3, 'a'
#print(type(immutable_var))
#immutable_var[0] = 200
#print(immutable_var) #не разрешает изменять элементы внутри кортежа ;( в данном случае у нас первый элемент это символ 1
                      #и тем более проверив класс методом type мы точно понимаем что tuple нам не даст поменять элемент
mutable_list = 1, 2, 3 , 'my', 'arm'
print(type(mutable_list))
mutable_list = ([1, 2, 3], 'my', 'arm' )
print(mutable_list)
mutable_list[0][0] = 5
print(mutable_list)

#mutable_list_ = [1, 2, 3]
#tuple_ = 1, 2, 3
#print(type(tuple_))
#print(type(mutable_list_))
#print(tuple_.__sizeof__())
#print(mutable_list_.__sizeof__())
