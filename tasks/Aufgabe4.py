from utils import utils


def task():

	param_count = utils.enterIntParams('Bitte gib eine Zahl an: ')
	param_parts = utils.enterIntParams('Bitte gib eine Zahl an: ')

	def fak(count):
		i = 1
		s = 1
		while i <= count:
			s = s * i
			i += 1
		return s

	solution = fak(param_count) / (fak(param_parts) *
	                               fak(param_count - param_parts))
	print(solution)

	#	print('4')
	return False
