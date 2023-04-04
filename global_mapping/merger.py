import constants_origin
import constants_stats
from pathlib import Path
import json
total = set([name for name in dir(constants_origin) if "__" not in name] + [name for name in dir(constants_stats) if "__" not in name])
f = {}
for name in total:
    ci = getattr(constants_origin, name, None)
    ti = getattr(constants_stats, name, None)
    if ci and ti:
        if isinstance(ci, dict) and isinstance(ti, dict):
            f[name] = ci | ti
        elif isinstance(ci, list) and isinstance(ti, list):
            f[name] = list(set(ci + ti))
    else:
        f[name] = ci or ti

f = dict(sorted(f.items()))
with open(Path(__file__).resolve().parent / "constants.py", "w") as file:
    for key, value in f.items():
        file.write(f"{key} = {value}\n")
