# !/usr/bin/env python3

__version__="0.3"

def __init__():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    # parser.add_argument('g', help='[g] generate a suko pattern')
    
    subparsers = parser.add_subparsers(title="subcommand(s)", dest="subcommand", help="Choose a subcommand")
    subparsers.add_parser('g', help='[g] generate a suko pattern')

    args = parser.parse_args()
    # if args.g=="g":
    if args.subcommand=="g":
        import random

        def generate_random_pattern():
            pattern = list(range(1, 10))
            random.shuffle(pattern)
            return pattern

        def calculate_sums(pattern):
            sums = []
            #Sums for four corners
            for indices in [(0, 1, 3, 4), (1, 2, 4, 5), (3, 4, 6, 7), (4, 5, 7, 8)]:
                sums.append(sum(int(pattern[i]) for i in indices))
            return sums

        pattern1 = generate_random_pattern()
        print("Random Pattern (answer):", pattern1)

        sums = calculate_sums(pattern1)
        print("Sums:", sums)

        pattern2 = generate_random_pattern()
        print("Color Pattern (sorting):", pattern2)
        sorting_number = ''.join(map(str, pattern2))

        #Sum of the first three digits of the Sorting Number using 1st Pattern
        print(f"Green :",sum(pattern1[int(digit)-1] for digit in sorting_number[:3]))
        # Sum of the second three digits of the Sorting Number using 1st Pattern
        print(f"Orange:",sum(pattern1[int(digit)-1] for digit in sorting_number[3:6]))
        # Sum of the third three digits of the Sorting Number using 1st Pattern
        print(f"Yellow:",sum(pattern1[int(digit)-1] for digit in sorting_number[6:9]))

    # print("in __init__ function")
