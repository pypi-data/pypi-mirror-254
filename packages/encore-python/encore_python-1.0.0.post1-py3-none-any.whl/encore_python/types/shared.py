import re

md5_regex = re.compile(r"[a-f0-9]{32}$")

__all__ = []

def valid_per_page(i: int) -> int:
    if 0 < i <= 250:
        return i
    raise RuntimeError("Getting more than 250 results at a time is not supported")


def positive_num(i: int) -> int:
    if i > 0:
        return i
    raise RuntimeError("Invalid page specified")


def valid_hash(s: str) -> str:
    if md5_regex.match(s):
        return s
    raise RuntimeError("Invalid hash")


instruments = {
    "guitar",
    "guitarcoop",
    "rhythm",
    "bass",
    "drums",
    "keys",
    "guitarghl",
    "guitarcoopghl",
    "rhythmghl",
    "bassghl",
    None,
}

difficulties = {"expert", "hard", "medium", "easy", None}
