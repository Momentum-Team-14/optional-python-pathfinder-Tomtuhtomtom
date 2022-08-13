# first step, create a 2d array from txt file - completed
# step 2, find min, max elevations, etc.

# imports (pillow imagecolor, Image, ImageDraw)
# from PIL import ImageColor
from PIL import Image, ImageDraw


# function that is called first after checking file
def create_array_from_file(file):
    with open(file, 'r') as data_file:
        data_for_array = data_file.readlines()
        array_data = convert_to_array(data_for_array)
        rows_and_columns_data = number_of_rows_and_columns(array_data)
        min_and_max_data = find_min_and_max(array_data)
        draw_map(rows_and_columns_data, min_and_max_data, array_data)


# creates a 2D array out of the txt file data
def convert_to_array(data):
    converted_line = [line.replace('\n', '').split() for line in data]
    converted_data = [list(map(int, i)) for i in converted_line]
    return converted_data


# counts number of rows and column for any 2D array
def number_of_rows_and_columns(array):
    number_of_rows = len(array)
    number_of_columns = len(array[0])
    return [number_of_columns, number_of_rows]


# find min and max
def find_min_and_max(array):
    min_of_array = min([min(x) for x in array])
    max_of_array = max([max(y) for y in array])
    return [min_of_array, max_of_array]


# draw map
def draw_map(rows_and_columns, min_and_max, array):
    map_image = Image.new('RGBA', (rows_and_columns[0], rows_and_columns[1]))
    for x in range(rows_and_columns[0]):
        for y in range(rows_and_columns[1]):
            numerator = ((min_and_max[1] - array[x][y]) * 255)
            denominator = (min_and_max[1] - min_and_max[0])
            map_image.putpixel((x, y), (0, int(numerator / denominator), 0))
    map_image.save('map.png')


# draw routes


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