
from itererators_and_generator.my_modules.my_iterators import LISTITERATOR
from itererators_and_generator.my_modules.my_generators import ListGENERATOR

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]
]
multi_nested_list = [[1, 2, 4, [23, 'yyyy'], [234, [555]]]]
if __name__ == "__main__":
	for element in LISTITERATOR(nested_list):
		print(element)

	flat_list_iter = [element for element in LISTITERATOR(nested_list)]
	print(flat_list_iter)

	print()

	for element_gen in ListGENERATOR(nested_list):
		print(element_gen)

	#проверка для многоуровневой вложенности

	for element in LISTITERATOR(multi_nested_list):
		print(element)

	flat_list_iter = [element for element in LISTITERATOR(multi_nested_list)]
	print(flat_list_iter)

	print(ListGENERATOR(LISTITERATOR(multi_nested_list)))

	for element_gen in ListGENERATOR(LISTITERATOR(multi_nested_list)):
		print(element_gen)
