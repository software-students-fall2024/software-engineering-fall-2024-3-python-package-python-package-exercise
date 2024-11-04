import argparse
import sys

CHOICES = {"km", "kilometers", "mi", "miles", "lb", "pounds", "kg", "kilograms"}
bubble = '''
 _______________            ________________
|   324         |           |    response    |
 ---------------            ----------------
'''
animal = '''
        \ \                 / /
         \ \               / /
          \ \ _         _ / /
  __   ___.--'_`.     .'_`--.___   __
 ( _`.'. -   'o` )   ( 'o`   - .`.'_ )
 _\.'_'      _.-'     `-._      `_`./_
( \`. )    //\`         '/\\    ( .'/ )
 \_`-'`---'\\__,       ,__//`---'`-'_/
  \`        `-\         /-'        '/
   `                               '   
'''


def parse_args(args):
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-fm', '--from-unit', choices=CHOICES, help="Unit to convert from")
    parser.add_argument('-to', '--to-unit', choices=CHOICES, help="Unit to convert to")
    parser.add_argument('--value', type=float, required=True, help="Value of unit")
    args = parser.parse_args(args)
    return args

def main():
    print(bubble, animal)
    args = parse_args(sys.argv[1:])
    print(args.value, args.from_unit, 'to', args.to_unit)
if __name__ == "__main__":
    main()