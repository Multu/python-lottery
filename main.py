import logging
import lottery.core as lottery

logging.basicConfig(filename='play_log.log', level=logging.DEBUG)

logging.info('Start new game')

lottery.print_input_rules()

player_numbers = []
for i in range(lottery.player_numbers_count):
	number = int(input('Number' + str(i + 1) + ': '))
	player_numbers.append(number)

assert len(player_numbers) == lottery.player_numbers_count

logging.info('Player numbers: %s', player_numbers)

if lottery.is_valid_player_input(player_numbers):
	logging.info('Player numbers valid. Start play')
	lottery.play(player_numbers)
else:
	logging.warning('Player numbers invalid')
	print('Incorrect input data')

logging.info('')