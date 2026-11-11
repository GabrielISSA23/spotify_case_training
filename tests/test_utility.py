from notebooks.spotify_eda import get_extremes


def test_get_extremes_returns_minimum_and_maximum():
    selection = [{"x": 1, "y": 10}, {"x": 3, "y": 5}, {"x": 2, "y": 20}]

    assert get_extremes(selection, "y", (0, 0)) == (5, 20)


def test_get_extremes_uses_defaults_when_selection_is_empty(capsys):
    defaults = (120, 360)

    assert get_extremes([], "x", defaults) == defaults
    assert "Using default values (120, 360)" in capsys.readouterr().out
