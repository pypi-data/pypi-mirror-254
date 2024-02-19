import sys as _sys
from typing import List, Optional

from rinkrat import cli

def main(argv: List[str]) -> None:
    interface = cli.Cli()

    interface.parse(argv)
    interface.execute()

# script entry point
def run(args: Optional[List[str]] = None) -> None:
    main(args or _sys.argv[1:])

if __name__ == "__main__":
    main(_sys.argv[1:])
    # ^ don't include the name of the program
