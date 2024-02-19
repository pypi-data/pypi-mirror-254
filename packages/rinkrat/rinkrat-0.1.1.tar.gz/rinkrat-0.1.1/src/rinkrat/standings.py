import argparse
from datetime import datetime
import sys as _sys
from typing import List

from rinkrat import api
from rinkrat import STANDINGS_BASE_URL

usage_str = """standings <ranking> [<args>]

rankings:
  overall     results ranked by league standing
  conference  results ranked by conference standing
  division    results ranked by division standing
  wild        results ranked by wild card standing
"""

class Standings:
    def __init__(self) -> None:
        # being verbose on set ranking attrs
        setattr(self, "overall", self._overall)
        setattr(self, "conference", self._conference)
        setattr(self, "division", self._division)
        setattr(self, "wild", self._wild)

        # use today's date as the default
        today = datetime.now()
        self.date = "{:04d}-{:02d}-{:02d}".format(
            today.year, 
            today.month, 
            today.day)

        self.parser = argparse.ArgumentParser(usage=usage_str)
        self.parser.add_argument("ranking")
        self.parser.add_argument(
            "-d",
            "--date",
            nargs="?",
            default=self.date,
            metavar="YYYY-MM-DD",
            help="query rankings for this date, YYYY-MM-DD")

    def parse(self, argv: List[str]) -> None:
        """
        Takes a list of arguments and passes them to argparse for parsing.

        The results are stored internally for later processing.
        """
        args = self.parser.parse_known_args(argv)

        if not hasattr(self, args[0].ranking):
            invalid = f"\"{args[0].ranking}\" is not a valid ranking, see --help"

            argparse.ArgumentParser.error(
                self=self.parser,
                message=invalid)

        # create a dictionary of options that contain values
        self.opts = {k: v for k, v in vars(args[0]).items() if v not in (None, "")}
        self.opts.setdefault("args", args[1])

    def execute(self) -> None:
        """
        Perform the action associated with the stored argument.
        """
        try:
            getattr(self, self.opts["ranking"])(self.opts["args"])
        except AttributeError:
            invalid = f"{self.parser.prog}: error: execute cannot be called without first calling parse\n"
            _sys.stderr.write(invalid)
            _sys.exit(2)

        self._get_data()
        self._rank_results()
        self._display()

    def _overall(self, argv):
        if argv:
            argparse.ArgumentParser.error(
                self=self.parser,
                message="overall does have a selection, see standings --help")
        else:
            self.opts.setdefault("selection", ["overall"])
        
    def _conference(self, argv: List[str]):
        conferences = ["eastern", "western"]
        if any(i not in conferences for i in argv):
            argparse.ArgumentParser.error(
                self=self.parser,
                message="you can only use 'eastern' or 'western', see standings --help")
        else:
            selection = []
            if not argv:
                selection = ["eastern", "western"]
            else:
                [selection.append(x) for x in argv if x not in selection]

            self.opts.setdefault("selection", selection)
        
    def _division(self, argv):
        divisions = ["atlantic", "metropolitan", "central", "pacific"]
        if any(i not in divisions for i in argv):
            argparse.ArgumentParser.error(
                self=self.parser,
                message="you can only use 'atlantic', 'metropolitan', 'central', 'pacific', see standings --help")
        else:
            selection = []
            if not argv:
                selection = ["atlantic", "metropolitan", "central", "pacific"]
            else:
                [selection.append(x) for x in argv if x not in selection]

            self.opts.setdefault("selection", selection)
        
    def _wild(self, argv):
        conferences = ["eastern", "western"]
        if any(i not in conferences for i in argv):
            argparse.ArgumentParser.error(
                self=self.parser,
                message="you can only use 'eastern' or 'western', see standings --help")
        else:
            selection = []
            if not argv:
                selection = ["eastern", "western"]
            else:
                [selection.append(x) for x in argv if x not in selection]

            self.opts.setdefault("selection", selection)

    def _get_data(self):
        if not _is_valid_query_date(self.opts["date"]):
            argparse.ArgumentParser.error(
                self=self.parser, 
                message="invalid date format - use YYYY-MM-DD. see standings --help")

        url = '{}{}'.format(STANDINGS_BASE_URL, self.opts["date"])

        self.opts.setdefault("data", api.get(url))

    def _rank_results(self):
        if self.opts["ranking"] == "overall":
            self.opts.setdefault(
                "ranked",
                _ranked_overall(self.opts["data"]["standings"]))

        if self.opts["ranking"] == "conference":
            self.opts.setdefault(
                "ranked",
                _ranked_conference(self.opts["selection"], 
                                  self.opts["data"]["standings"]))

        if self.opts["ranking"] == "division":
            self.opts.setdefault(
                "ranked",
                _ranked_division(self.opts["selection"],
                                self.opts["data"]["standings"]))

        if self.opts["ranking"] == "wild":
            self.opts.setdefault(
                "ranked",
                _ranked_wild(self.opts["selection"],
                            self.opts["data"]["standings"]))

    def _display(self):
        """Show the ranked results on the console"""

        """
        [date]

        [group-header]
        [team-stat-header]
        [ranked-team-stats]
        """

        for group, teams in self.opts["ranked"].items():
            # group header
            print(f"{group}")

            # team stat header
            print(f'{"": <3}{"": <26}{"GP": <4}{"W": <4}{"L": <4}{"OTL": <4}{"PTS": <4}')

            # ranked team stats
            for i, team in enumerate(teams):
                print(f"{i+1: <3}", end="")

                for key, value in team.items():

                    if key == "teamName":
                        print(f"{value['default']: <26}", end="")

                    elif key == "gamesPlayed":
                        print(f"{value: <4}", end="")

                    elif key == "wins":
                        print(f"{value: <4}", end="")

                    elif key == "losses":
                        print(f"{value: <4}", end="")

                    elif key == "otLosses":
                        print(f"{value: <4}", end="")

                    elif key == "points":
                        print(f"{value: <4}", end="")

                print()

            print()

        # show the date
        print(f'As of {self.opts["date"]}')

def _ranked_overall(teams: List[dict]) -> dict:
    result = dict()

    name = "Overall"

    result.setdefault(name, [])

    for team in teams:
        result[name].append(filter_team_stats(team))

    return result

def _ranked_conference(conferences: List[str], teams: List[dict]) -> dict:
    result = dict()

    for conf in conferences:
        result.setdefault(conf.capitalize(), [])

    for team in teams:
        if team["conferenceName"] in result:
            result[team["conferenceName"]].append(filter_team_stats(team))

    return result

def _ranked_division(divisions: List[str], teams: List[dict]) -> dict:
    result = dict()

    for div in divisions:
        result.setdefault(div.capitalize(), [])

    for team in teams:
        if team["divisionName"] in result:
            result[team["divisionName"]].append(filter_team_stats(team))

    return result

def _ranked_wild(conferences: List[str], teams: List[dict]) -> dict:
    result = dict()

    for conf in conferences:
        result.setdefault(conf.capitalize(), [])

    for team in teams:
        if team["conferenceName"] in result:
            if team["wildcardSequence"] > 0:
                result[team["conferenceName"]].append(filter_team_stats(team))

    return result

def _is_valid_query_date(text: str) -> bool:
    try:
        datetime.strptime(text, "%Y-%m-%d")
        return True
    except ValueError:
        pass
        
    return False

def filter_team_stats(team: dict) -> dict:
    """specify the team stats we want to show"""

    filtered = dict()

    filtered.setdefault("teamName", team.get("teamName"))
    filtered.setdefault("gamesPlayed", team.get("gamesPlayed"))
    filtered.setdefault("wins", team.get("wins"))
    filtered.setdefault("losses", team.get("losses"))
    filtered.setdefault("otLosses", team.get("otLosses"))
    filtered.setdefault("points", team.get("points"))

    filtered.setdefault("l10Wins", team.get("l10Wins"))
    filtered.setdefault("l10Losses", team.get("l10Losses"))
    filtered.setdefault("l10OtLosses", team.get("l10OtLosses"))

    filtered.setdefault("streakCode", team.get("streakCode"))
    filtered.setdefault("streakCount", team.get("streakCount"))

    filtered.setdefault("goalFor", team.get("goalFor"))
    filtered.setdefault("goalAgainst", team.get("goalAgainst"))
    filtered.setdefault("goalDifferential", team.get("goalDifferential"))

    return filtered
