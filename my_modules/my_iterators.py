from itertools import chain


class LISTITERATOR(list):

	def __iter__(self):
		self.item_ = list.__iter__(self)
		return self
	def __next__(self):
		el = next(self.item_)
		if isinstance(el, list):
			self.item_ = chain(el, self.item_)
			return next(self.item_)
		return el


