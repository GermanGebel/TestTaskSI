from test_data import *
import logging

logging.basicConfig(filename="hack.log", level=logging.DEBUG, filemode='w', \
                    format='%(asctime)s - %(levelname)s: %(message)s', encoding='utf-8')


def calculate(m: int, n: int, p: list):
    logging.info(f'🚂🚃🚃🚃🚃🚃🚃🚃🚃🚃')
    logging.info(f'm = {m}, n = {n}, p = {p}')

    if n > m:
        n = m
        p = p[:n]

    first_strategy = m // n * p + p[:m % n] # if m > n: m = 5, n = 3, p = [1, 2, 3] result: [1, 2, 3, 1, 2]
    total_max_sum = sum(first_strategy)

    logging.info(f'First strategy: {first_strategy}. Total sum: {total_max_sum}')

    DAY_OFF = 0
    final_strategy = first_strategy
    
    i = 1
    while i < m:
        slice = first_strategy[:i]
        slice.append(DAY_OFF) 

        len_arr = i + 1

        temp_strategy = m // len_arr * slice + slice[:m % len_arr]

        if m % len_arr == 0: # if end on day_off 
            if i >= m:
                temp_strategy[-1] = first_strategy[0]
            else:
                temp_strategy[-1] = first_strategy[i]
        
        sum_of_temp_strategy = sum(temp_strategy)
        

        logging.info(f'Temporary strategy: {temp_strategy}. Its sum: {sum_of_temp_strategy}')

        if sum_of_temp_strategy > total_max_sum:
            total_max_sum = sum_of_temp_strategy
            final_strategy = temp_strategy
            logging.info(f'NEW STRATEGY: {temp_strategy}. TOTAL SUM: {sum_of_temp_strategy}')
        
        i += 1


    logging.info(f'FINAL STRATEGY: {final_strategy}. TOTAL SUM: {total_max_sum}')
    return total_max_sum

def update_logs():
    for m, n, p, _ in test_data:
        calculate(m, n, p)

if __name__ == '__main__':
    update_logs()