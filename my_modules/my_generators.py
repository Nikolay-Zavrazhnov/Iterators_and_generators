
def ListGENERATOR(any_list):
	for item in any_list:
		if isinstance(item, list):
			for inside_item in item:
				yield inside_item
		else:
			yield item


