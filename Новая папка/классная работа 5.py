#Подсчет элементов в кортеже
def count_element(tup, element):
    return tup.count(element)

my_tuple = (1, 2, 2, 3, 3, 3, 4, 5)
result = count_element(my_tuple, 3)
print(result)