import logging

def matching_count(casino_list, player_list):
	matching_list = []

	for i in range(len(player_list)):
		for j in range(len(casino_list)):
			if player_list[i] == casino_list[j]:
				matching_list.append(player_list[i])
				break

	logging.info('Matching numbers list: %s', matching_list)

	return len(matching_list)



def win_size(intersection_count):
	if intersection_count == 2:
		return 500
	elif intersection_count == 3:
		return 1000
	elif intersection_count == 4:
		return 5000
	elif intersection_count == 5:
		return 100000
	else:
		return 0