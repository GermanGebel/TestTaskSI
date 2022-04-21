from test_data import *
import logging

logging.basicConfig(filename="work.log", level=logging.DEBUG, filemode='w', \
                    format='%(asctime)s - %(levelname)s: %(message)s', encoding='utf-8')


class StoreLine:
    def __init__(self) -> None:
        self.__store_line = []
        self.__spent_energy = 0
    
    def logging(self):
        logging.info(f'Updated store line: {self.__store_line}')

    def spend_energy(self, value):
        self.__spent_energy += value
    
    def get_spent_energy(self):
        return self.__spent_energy
    
    def add_to_left(self, box_number):
        self.__store_line.insert(0, box_number)
        self.spend_energy(1)
        
        logging.info(f'Added box({box_number}) to left, spent 1 energy. Total spent energy: {self.get_spent_energy()}')

    def add_to_right(self, box_number):
        self.__store_line.append(box_number)
        self.spend_energy(1)

        logging.info(f'Added box({box_number}) to right, spent 1 energy. Total spent energy: {self.get_spent_energy()}')

    def take_out(self, box_number):
        id = self.__store_line.index(box_number)
        energy = len(self.__store_line[id + 1:]) * 2 + 1 # 2k + 1 where k is amount of boxes after needed

        self.__store_line.pop(id)
        self.spend_energy(energy)

        logging.info(f'Took out box({box_number}), spent {energy} energy. Total spent energy: {self.get_spent_energy()}')

def analyse(programm: list[tuple[str, int]]) -> int:
    logging.info(f'🚂🚃🚃🚃🚃🚃🚃🚃🚃🚃\n\n{programm}\n')

    store_line = StoreLine()
    out_boxes = [box for action, box in programm if action == OUT]
    logging.info(f'Boxes which will be taken out: {out_boxes}')

    count_added_boxes = 0
    count_taken_out_boxes = 0
    
    for index, (action, box) in enumerate(programm): 
        if action == OUT:
            store_line.take_out(box)
            out_boxes.remove(box)
            count_taken_out_boxes += 1
            logging.info(f'Boxes which will be taken out: {out_boxes}')
        
        if action == ADD:
            logging.info(f'Adding box({box})')
            if box in out_boxes:
                id = out_boxes.index(box)
                boxes_before_in_out_boxes = out_boxes[:id]
                
                amount_boxes_before_in_out_boxes = id
                amount_added_boxes_before_in_program = count_added_boxes - count_taken_out_boxes \
                        - len([b for a, b in programm[:index] if a == ADD and b in boxes_before_in_out_boxes]) 
                # where len([...]) is an amount of boxes which was added and will be taken out

                logging.info(f'Amount boxes before in out_boxes: {amount_boxes_before_in_out_boxes}')
                logging.info(f'Amount boxes before in programm: {amount_added_boxes_before_in_program}')

                if amount_boxes_before_in_out_boxes > amount_added_boxes_before_in_program:
                    # to don't affect for out boxes
                    store_line.add_to_left(box)
                else:
                    # to don't spend a lot of energy for out
                    store_line.add_to_right(box)
            else:
                store_line.add_to_left(box)
            
            count_added_boxes += 1
            logging.info(f'Amount added boxes: {count_added_boxes}')
        
        store_line.logging()
                
    return store_line.get_spent_energy()

def update_logs():
    for data in test_data:
        analyse(data[0])

if __name__ == '__main__':
    update_logs()