from itertools import chain
from typing import Optional

from dotenv import dotenv_values


def load_dotenv_files(files: list[str]) -> dict[str, Optional[str]]:
    """
    Loads environment variables from a list of dotenv files and merges
    them into a single dictionary. If a variable is defined in multiple files,
    the value from the last file in the list will overwrite earlier values.
    """

    return dict(chain.from_iterable(dotenv_values(file).items() for file in files))
