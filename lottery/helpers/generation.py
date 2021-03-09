import random

def casino_numbers(numbers_count, min_number, max_number):
	random_list = []

	while len(random_list) < numbers_count:
		rand_number = random.randint(min_number, max_number)

		if list_contains(random_list, rand_number):
			continue
		else:
			random_list.append(rand_number)

	return random_list


def list_contains(sourse_list, target_number):
	for i in range(len(sourse_list)):
		if sourse_list[i] == target_number:
			return True

	return False


