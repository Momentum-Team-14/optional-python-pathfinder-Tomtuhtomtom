# first step, create a 2d array from txt file - completed
# step 2, find min, max elevations, etc.

# imports (pillow imagecolor)
from PIL import ImageColor


# function that is called first after checking file
def create_array_from_file(file):
    with open(file, 'r') as data_file:
        data_for_array = data_file.readlines()
        array_data = convert_to_array(data_for_array)
        rows_and_columns = number_of_rows_and_columns(array_data)
        print(rows_and_columns)


# creates a 2D array out of the txt file data
def convert_to_array(data):
    converted_line = [line.replace('\n', '').split() for line in data]
    converted_data = [list(map(int,i)) for i in converted_line]
    return converted_data


# counts number of rows and column for any 2D array
def number_of_rows_and_columns(array):
    number_of_rows = len(array)
    number_of_columns = len(array[0])
    return [number_of_columns, number_of_rows]


# opens file path, checks if it's a file and calls function if so
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Draw an elevation map from numbers in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        create_array_from_file(file)
    else:
        print(f"{file} does not exist!")
        exit(1)