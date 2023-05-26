import pandas as pd


def test_create_df() -> None:
    df = pd.DataFrame({'column_name': [1, 2, 3]})


def test_fixed_test() -> None:
    df = pd.DataFrame({'afafafafaf': ["works"]})


def test_new() -> None:
    assert 2 != 0


def test_newer() -> None:
    assert 2 != 1

def test_newest() -> None:
    assert 2 != 1