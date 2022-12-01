import pathlib

PROJECT_ROOT =pathlib.Path(__file__).parents[1]
INPUT_DIR = PROJECT_ROOT / "input"
SHIMS_DIR = PROJECT_ROOT / "shims"
AOC_DIR = PROJECT_ROOT / "aoc"

COOKIE_FILE = PROJECT_ROOT / "cookie"
SHIM_FILE = SHIMS_DIR / "day_shim.py"
