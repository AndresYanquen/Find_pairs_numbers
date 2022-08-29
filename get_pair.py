
from array import array
from cmath import exp
from dotenv import load_dotenv
from os.path import join, dirname
import csv, os

EXPECTED_SUM = "EXPECTED_SUM"
CSV_FILE_NAME = "CSV_FILE_NAME"

class PairNumbers:

    
    def get_pairs(self, expected_sum, name_file):
        self.expected_sum = int(expected_sum)
        self.name_file = name_file
        with open(f"./{self.name_file}.csv", 'r', encoding="utf-8-sig") as file:
            list_to_check = [[int(x) for x in rec] for rec in csv.reader(file, delimiter=',')][0]          
        arr_length = len(list_to_check)
        save_pairs = {}
        unordered_map = {}
        for i in range(arr_length):
            if self.expected_sum - list_to_check[i] in unordered_map:
                save_pairs[list_to_check[i]]= self.expected_sum - list_to_check[i]
            if list_to_check[i] in unordered_map:
                unordered_map[list_to_check[i]] += 1
            else:
                unordered_map[list_to_check[i]] = 1
        return save_pairs
            
def get_user_value():
    while True:
        try:
            num = int(input("Please, write the desired sum result to find pairs numbers: \n your input:  "))
            break
        except ValueError:
            print("Please input integer only...")  
            continue
    return num

        
    
if __name__ == "__main__":
    expected_sum = get_user_value()
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    get_pairs_numbers = PairNumbers()
    print(f" Pairs of intergers found: {get_pairs_numbers.get_pairs(expected_sum, os.getenv(CSV_FILE_NAME))}")
