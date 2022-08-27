
from array import array
from dotenv import load_dotenv
from os.path import join, dirname
import csv, os



class PairNumbers:

    def __init__(self, path, expected_sum, name_file):
        self.path = path
        self.expected_sum = int(expected_sum)
        self.name_file = name_file

    
    def get_pairs(self):
        with open(f"./{self.name_file}.csv", 'r', encoding="utf-8-sig") as file:
            list_to_check = [[int(x) for x in rec] for rec in csv.reader(file, delimiter=',')][0]           
            return self.get_pairs_numbers_into_csv(list_to_check)
            
    
    def get_pairs_numbers_into_csv(self, list_to_check):
        arr_length = len(list_to_check)
        save_pairs = {}
        unordered_map = {}
        count = 0
        for i in range(arr_length):
            if self.expected_sum - list_to_check[i] in unordered_map:
                count += unordered_map[self.expected_sum - list_to_check[i]]
            if list_to_check[i] in unordered_map:
                unordered_map[list_to_check[i]] += 1
            else:
                unordered_map[list_to_check[i]] = 1
        return unordered_map



if __name__ == "__main__":
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    get_pairs_numbers = PairNumbers(dotenv_path,os.getenv("EXPECTED_SUM"), os.getenv("CSV_FILE_NAME"))
    print(f" Casos encontrados: {get_pairs_numbers.get_pairs()}")