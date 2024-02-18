import argparse
import sys
from typing import Any, Callable, Dict, List, Pattern, Union
from triple.server import Triple_Agent
def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage='',
        epilog=
            "",
        description="""""")

    
    parser.add_argument('-s', '--start', action='store_true', dest='start',
                        default=None,
                        help="I am here")
    
    return parser

def main(argv: List[str] = sys.argv[1:]) -> int:
    # parse options
    parser = get_parser()
    try:
        args = parser.parse_args(argv)

    except SystemExit as err:
        return err.code
    d = vars(args)
    
    if d.get("start", "None") == True:
        Triple_Agent()._start()
    else:
        print("**Good Bye**")


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))