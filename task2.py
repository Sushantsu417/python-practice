import csv

def generator(file_path):
   
    with open(file_path, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:          
            yield row  

if __name__ == "__main__":
    for row in generator('data.csv'):
        print(row)
