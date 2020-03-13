import argparse

from xuzu import box_text
from rubu import print_and_copy


def main():
    # CLI arg parser
    parser = argparse.ArgumentParser()
    arg = parser.add_argument
    arg('text', nargs='*', type=str, help='text to box')
    arg('-c', '--cap', default='#', type=str,
        help='char to cap lines (typically comment char)')
    arg('-l', '--line', default='-', type=str,
        help='char to make lines of box')

    # Parse args
    cli_args = parser.parse_args()
    text = ' '.join(cli_args.text)
    cap  = cli_args.cap
    line = cli_args.line

    # Make box and print/copy
    text_box = box_text(text, cap=cap, line_char=line)
    print_and_copy(text_box)

    return 0 # debugging purposes


if __name__ == '__main__':
    ret = main()
