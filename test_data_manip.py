import pandas as pd
import pytest
import data_manip


@pytest.fixture()
def example_submission():
    return pd.DataFrame(
        {
            "containerid": [
                "gcn79399957",
                "gcn79399960",
                "gcn79399966",
                "gcn79399970",
                "gcn79399977",
                "gcn79399982",
                "gcn79007358",
                "gcn79012772",
            ]
        }
    )


def test_submission():
    data_manip.process_submission("testscoring.csv")


def test_merge_submission(example_submission):
    result = data_manip.merge_submission(example_submission)
    assert result.shape == (8, 3)


def test_score(example_submission):
    result = data_manip.score_file(data_manip.merge_submission(example_submission))
    assert result == 7


def test_turn_to_streetworth():
    result = data_manip.turn_to_streetworth(1)
    assert result == "€50.000"
