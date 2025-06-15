import sys
import os
import re


def get_all_dirs_by_suffix(dir: str, suffixes: list) -> list:
    array: list = list()

    try:
        current_dir: list = os.listdir(dir)
    except FileNotFoundError:
        print('Can\'t find directory: ' + dir + '!')
        sys.exit(-1)

    for d in current_dir:
        curr = dir + '/' + d

        if os.path.isdir(curr):
            array += get_all_dirs_by_suffix(curr, suffixes)

        elif any(re.match(r'^.*\.(R)$'.replace('R', suffix), curr) for suffix in suffixes):
            array.append(curr)
    
    return array


def get_lines_count(dir: str, conside_empty: bool = True) -> int:
    lines_count: int = 0

    try:

        with open(dir, 'r') as f:
            lines: list = f.readlines()

            if (not conside_empty):
                lines = [line.strip() for line in lines if line.strip() != ""]

            lines_count = len(lines)
    
    except UnicodeDecodeError:
        print('UnicodeDecodeError!')
        #sys.exit(-1)

    return lines_count


def main():
    if len(sys.argv) != 4:
        print('Incorrect arguments!\n1. The directory in which the lines will be counted.\n2. Supported file extensions (via \'+\' symbol).\n3. Will empty strings be counted? (1 if yes).')
        return
    elif not sys.argv[3] in ['0', '1']:
        print('Argument 3 can only be 1 or 0!')
        return

    DIR: str = sys.argv[1]
    TARGET_SUFFIXES: list = sys.argv[2].split('+')
    CONSIDE_EMPTY: bool = True if sys.argv[3] == '1' else False

    dirs: list = get_all_dirs_by_suffix(DIR, TARGET_SUFFIXES)
    print( "Lines count: " + str( sum( ( get_lines_count(dir, conside_empty = CONSIDE_EMPTY) for dir in dirs ) ) ) )


if __name__ == '__main__':
    main()
