import argparse
import sys as _sys
from typing import List, Dict, Any

from rinkrat import standings, __version__

usage_str = """rinkrat <command> [<args>]

commands:
  standings  show the team rankings in a specified format
"""

class Cli:
    def __init__(self) -> None:
        # create an attribute that points to the command's constructor
        setattr(self, "standings", standings.Standings)

        self.parser = argparse.ArgumentParser(prog="rinkrat", usage=usage_str)
        self.parser.add_argument("command")
        self.parser.add_argument(
            "-v",
            "--version",
            action="version",
            version=f"%(prog)s {__version__}")

    def parse(self, argv: List[str]) -> None:
        """
        Parses the argument vector looking for a command name that matches
        a registered attr. The results are stored internally for further
        processing.
        """
        args = self.parser.parse_args(argv[:1])

        if not hasattr(self, args.command):
            invalid = f"\"{args.command}\" is not a valid command, see --help"

            argparse.ArgumentParser.error(
                self=self.parser,
                message=invalid)

        self.opts = {k: v for k, v in vars(args).items() if v not in (None, "")}
        self.opts.setdefault("args", argv[1:])
        # ^ forward the remaining args for parsing by the assigned class

    def execute(self):
        """
        Perform the actions associated with the stored command.
        """
        try:
            obj = getattr(self, self.opts["command"])()
            obj.parse(self.opts["args"])
            obj.execute()
        except AttributeError:
            invalid = f"{self.parser.prog}: error: calling execute without a stored attribute\n"
            _sys.stderr.write(invalid)
            _sys.exit(2)
