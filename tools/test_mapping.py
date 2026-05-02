import itertools
import json

from global_mapping import bf6

with open("test.json") as f:
    d: dict = json.load(f)
    segments = d.get("data", {}).get("segments", [])
    attr = {
        segment.get("attributes", {}).get("key", ""): segment.get("metadata", {}).get(
            "name", ""
        )
        for segment in segments
    }

gametools_keys = []
gametools_keys.extend(itertools.chain(bf6.WEAPONS, bf6.WEAPON_GROUPS))
gametools_keys.extend(itertools.chain(bf6.MELEE, bf6.MELEE_GROUPS))
gametools_keys.extend(
    itertools.chain(bf6.STAT_GAMEMODE_SMALL, bf6.STAT_GAMEMODE_SMALL_CATEGORY)
)
gametools_keys.extend(bf6.STAT_MAPS)
gametools_keys.extend(bf6.CLASSES)
gametools_keys.extend(itertools.chain(bf6.VEHICLES, bf6.VEHICLE_GROUPS))
gametools_keys.extend(itertools.chain(bf6.GADGETS, bf6.GADGET_GROUPS))

for key, val in attr.items():
    if key not in gametools_keys:
        print(key, val)

# res = {}
# for key, val in bf6.STAT_GAMEMODE_SMALL.items():
#     res[f"gm_{key}"] = val
# print(res)
