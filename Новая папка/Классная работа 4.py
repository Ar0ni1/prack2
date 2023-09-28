#Удаление элемента из кортежа
def udalenieelementa(cortage, element):
    return tuple(x for x in cortage if x != element)

my_cartage = (1, 2, 3, 4, 5, 6, 7, 8, 9)
result = udalenieelementa(my_cartage, 3)
print(result)