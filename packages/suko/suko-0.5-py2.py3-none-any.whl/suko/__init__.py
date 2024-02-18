# !/usr/bin/env python3

__version__="0.5"

def __init__():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    
    subparsers = parser.add_subparsers(title="subcommand(s)", dest="subcommand", help="choose a subcommand:")
    subparsers.add_parser('g', help='[g] generate a suko pattern')

    args = parser.parse_args()
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

        def generate_colors():
            num1 = random.randint(2, 5)
            num2 = random.randint(2, 5)
            num3 = 9 - num1 - num2
            if 2 <= num3 <= 5:
                return num1, num2, num3
            else:
                return generate_colors()
            
        pattern1 = generate_random_pattern()
        print("Random Pattern (Answer):", pattern1)

        sums = calculate_sums(pattern1)
        print("Sums:", sums)

        # Generate and print the result as color range
        result = generate_colors()
        print("Color Range (Green, Orange, Yellow):", result)

        pattern2 = generate_random_pattern()
        print("Color Pattern:", pattern2)
        sorting_number = ''.join(map(str, pattern2))

        #Sum of Green Pattern
        print(f"Green :",sum(pattern1[int(digit)-1] for digit in sorting_number[:result[0]]))
        # Sum of Orange Pattern
        print(f"Orange:",sum(pattern1[int(digit)-1] for digit in sorting_number[result[0]:result[0]+result[1]]))
        # Sum of Yellow Pattern
        print(f"Yellow:",sum(pattern1[int(digit)-1] for digit in sorting_number[result[0]+result[1]:9]))

    # print("in __init__ function")