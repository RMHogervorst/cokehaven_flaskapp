import pandas as pd
from typing import Tuple
import logging


def process_file(filename: str) -> Tuple[int,int]:
    logger = logging.getLogger(__name__)
    logger.debug(f"processing file {filename}")
    data = process_submission(filename)
    data = merge_submission(data)
    kilos = score_file(data)
    streetworth = turn_to_streetworth(kilos)
    return kilos, streetworth


def process_submission(filename) -> pd.DataFrame:
    submission = pd.read_csv(filename)
    submission = submission.drop_duplicates(subset="containerid").dropna()
    n_submission = len(submission)
    if n_submission != 400:
        ValueError("Je moet specifiek 400 unieke containers uploaden")
    return submission


def merge_submission(submission: pd.DataFrame) -> pd.DataFrame:
    comparison = pd.read_csv("testscoring.csv")
    return comparison.merge(submission, on="containerid", how="inner")


def score_file(merged_df: pd.DataFrame) -> int:
    result = merged_df["coke_kilo"][merged_df["coke_ind"] == 1].sum()
    return result


def turn_to_streetworth(kilos: int) -> str:
    """A gram is 50 euros, so 1000g is 50000 euros"""
    currency_string = "€{:,}".format(kilos * 50000).replace(',', '.')
    return currency_string
