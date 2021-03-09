import logging
from lottery.helpers import generation, result

player_numbers_count = 5
casino_numbers_count = 10
min_number = 1
max_number = 35


def play(player_numbers):
    casino_numbers = generation.casino_numbers(casino_numbers_count, min_number, max_number)
    assert len(casino_numbers) == casino_numbers_count
    logging.info('Casino numbers: %s', casino_numbers)

    matching_count = result.matching_count(casino_numbers, player_numbers)
    assert matching_count <= player_numbers_count

    win_size = result.win_size(matching_count)
    logging.info('Matching count: %d, Win size: %d', matching_count, win_size)

    print_result(casino_numbers, matching_count, win_size)

def print_result(casino_numbers, matching_count, win_size):
    print('Casino numbers', casino_numbers)
    print('You guess', matching_count, 'numbers and win', win_size, 'dollars')

def print_input_rules():
    print('You must input', player_numbers_count,
          'unique numbers with value from',
          min_number, 'to', max_number)


def is_valid_player_input(player_numbers):
    logging.info('Start players input validation')
    if len(player_numbers) == player_numbers_count:
        for i in range(len(player_numbers)):

            # Check if inside min-max range
            if player_numbers[i] < min_number or player_numbers[i] > max_number:
                logging.warning('Number %d is out of range from %d to %d',
                             player_numbers[i], min_number, max_number)
                return False

            # Check if unique numbers
            for j in range(i + 1, len(player_numbers)):
                if player_numbers[i] == player_numbers[j]:
                    logging.warning('Number %d is not unique',
                                 player_numbers[i])
                    return False
        else:
            return True

    logging.warning('Incorrect count of numbers')
    return False
