import json
import pathlib
import pytest

from rinkrat import standings

TESTS_DIR = pathlib.Path(__file__).resolve().parent

@pytest.fixture
def standings_object() -> standings.Standings:
    return standings.Standings()

@pytest.fixture
def input_json():
    with open(TESTS_DIR / "data" / "standings_2023_12_31.json") as file:
        return json.loads(file.read())

@pytest.fixture
def expected_json(request):
    marker = request.node.get_closest_marker("expected_data")

    with open(TESTS_DIR / "data" / "expected_2023_12_31.json") as file:
        data = json.loads(file.read())

    match len(marker.args):
        case 1:
            return data.get(marker.args[0], {})
        case 2:
            return data.get(marker.args[0], {}).get(marker.args[1], {})
        case _:
            return data

def test_standings_has_ranking_attrs(standings_object):
    attrs = ["overall", "conference", "division", "wild"]

    for attr in attrs:
        assert hasattr(standings_object, attr)

def test_standings_exit_on_bad_ranking(standings_object):
    args = ["invalid"]

    with pytest.raises(SystemExit):
        standings_object.parse(args)

def test_standings_ranking_exit_on_bad_args(standings_object):
    args = {
        "overall": ["space"],
        "conference": ["northern", "western"],
        "division": ["atlantic", "mythic"],
        "wild": ["scandinavia"],
    }

    for k, v in args.items():
        with pytest.raises(SystemExit):
            argv = [k]
            [argv.append(a) for a in v]

            standings_object.parse(argv)
            standings_object.execute()

def test_standings_ranking_default_selection(standings_object):
    """
    Does opts contain the expected selections when defaults are used.
    """
    defaults = {
        "overall": ["overall"],
        "conference": ["eastern", "western"],
        "division": ["atlantic", "metropolitan", "central", "pacific"],
        "wild": ["eastern", "western"],
    }

    for ranking in defaults.keys():
        standings_object.parse([ranking])
        standings_object.execute()
        assert defaults[ranking] == standings_object.opts["selection"]

def test_standings_is_valid_query_date():
    assert standings._is_valid_query_date("2010-12-31") == True
    assert standings._is_valid_query_date("12.345/6789") == False

def test_standings_exit_on_bad_date(standings_object):
    args = ["overall", "-d", "785-8993.abcd,*&^%"]

    with pytest.raises(SystemExit):
        standings_object.parse(args)
        standings_object.execute()

@pytest.mark.expected_data("overall", "overall")
def test_standings_ranking_overall(input_json, expected_json):
    result = standings._ranked_overall(input_json["standings"])

    for i, input_team in enumerate(result["Overall"]):
        expected_team_name = expected_json[str(i)]
        input_team_name = input_team.get('teamName').get('default')

        assert expected_team_name == input_team_name
        
@pytest.mark.expected_data("conference", "eastern")
def test_standings_ranking_eastern_conference(input_json, expected_json):
    result = standings._ranked_conference(["eastern"], input_json["standings"])

    for i, input_team in enumerate(result["Eastern"]):
        expected_team_name = expected_json[str(i)]
        input_team_name = input_team.get('teamName').get('default')

        assert expected_team_name == input_team_name

@pytest.mark.expected_data("conference", "western")
def test_standings_ranking_western_conference(input_json, expected_json):
    result = standings._ranked_conference(["western"], input_json["standings"])

    for i, input_team in enumerate(result["Western"]):
        expected_team_name = expected_json[str(i)]
        input_team_name = input_team.get('teamName').get('default')

        assert expected_team_name == input_team_name

@pytest.mark.expected_data("division", "atlantic")
def test_standings_ranking_atlantic_division(input_json, expected_json):
    result = standings._ranked_division(["atlantic"], input_json["standings"])

    for i, input_team in enumerate(result["Atlantic"]):
        expected_team_name = expected_json[str(i)]
        input_team_name = input_team.get('teamName').get('default')

        assert expected_team_name == input_team_name
    
@pytest.mark.expected_data("division", "metropolitan")
def test_standings_ranking_metropolitan_division(input_json, expected_json):
    result = standings._ranked_division(["metropolitan"], input_json["standings"])

    for i, input_team in enumerate(result["Metropolitan"]):
        expected_team_name = expected_json[str(i)]
        input_team_name = input_team.get('teamName').get('default')

        assert expected_team_name == input_team_name

@pytest.mark.expected_data("division", "central")
def test_standings_ranking_central_division(input_json, expected_json):
    result = standings._ranked_division(["central"], input_json["standings"])

    for i, input_team in enumerate(result["Central"]):
        expected_team_name = expected_json[str(i)]
        input_team_name = input_team.get('teamName').get('default')

        assert expected_team_name == input_team_name

@pytest.mark.expected_data("division", "pacific")
def test_standings_ranking_pacific_division(input_json, expected_json):
    result = standings._ranked_division(["pacific"], input_json["standings"])

    for i, input_team in enumerate(result["Pacific"]):
        expected_team_name = expected_json[str(i)]
        input_team_name = input_team.get('teamName').get('default')

        assert expected_team_name == input_team_name

@pytest.mark.expected_data("wild", "eastern")
def test_standings_ranking_eastern_wildcard(input_json, expected_json):
    result = standings._ranked_wild(["eastern"], input_json["standings"])

    for i, input_team in enumerate(result["Eastern"]):
        expected_team_name = expected_json[str(i)]
        input_team_name = input_team.get('teamName').get('default')

        assert expected_team_name == input_team_name

@pytest.mark.expected_data("wild", "western")
def test_standings_ranking_western_wildcard(input_json, expected_json):
    result = standings._ranked_wild(["western"], input_json["standings"])

    for i, input_team in enumerate(result["Western"]):
        expected_team_name = expected_json[str(i)]
        input_team_name = input_team.get('teamName').get('default')

        assert expected_team_name == input_team_name

def test_standings_call_execute_without_parsing(standings_object):
    with pytest.raises(SystemExit):
        standings_object.execute()
