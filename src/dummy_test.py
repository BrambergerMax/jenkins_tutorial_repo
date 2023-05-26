import pandas as pd


def test_create_df() -> None:
    df = pd.DataFrame({'column_name': [1, 2, 3]})


def test_failing_test() -> None:
    df = pd.DataFrame( {'afafafafaf'}, 'faf')