# Поиск элемента в кортеже
def poiskelementa(cartege, elem):
    if elem in cartege:
        return cartege.index(elem)
    else:
        return "Элемент не найден"

mycortagw = (1, 2, 3, 4, 5, 6, 7, 8, 9)
result = poiskelementa(mycortagw, 3)
print(result)

