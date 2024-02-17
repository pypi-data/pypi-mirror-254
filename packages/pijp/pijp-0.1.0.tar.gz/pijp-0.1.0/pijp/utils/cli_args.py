from typing import Union
import string
import re
import shlex


def build_cli_options(
    params: dict[str, Union[str, bool, list[str]]],
    variables: dict[str, str],
) -> list[str]:
    key_pattern = re.compile(r"^[a-zA-Z0-9_-]+$")

    result = []
    for name, value in params.items():
        key = name.strip()
        if not bool(key_pattern.match(key)):
            continue

        prefix = "-" if len(key) == 1 else "--"

        if isinstance(value, bool):
            if value:
                result.append(f"{prefix}{key}")
        elif isinstance(value, str):
            if value:
                param = string.Template(value).substitute(variables)
                result.extend([f"{prefix}{key}", shlex.quote(param)])
        elif isinstance(value, list):
            if not value:
                continue

            for item in value:
                if item:
                    param = string.Template(str(item)).substitute(variables)
                    result.extend([f"{prefix}{key}", shlex.quote(param)])
        else:
            continue

    return result
