from typing import List


def extract_time_range(range_str: str) -> List[str]:
    res = range_str.split("~")
    if len(res) != 2:
        return ["", ""]
    return res
