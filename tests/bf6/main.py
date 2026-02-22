import itertools
from typing import Any

import requests
import asyncio
import json

from global_mapping import bf6
from global_mapping.readability.bf6.main import get_stats
from tests.bf6 import used_methods


def find_player(player_name: str):
    return requests.get(
        url="https://api.gametools.network/bf6/stats/",
        params={"name": player_name, "platform": "pc", "raw": "true"},
    ).json()


def check_unmapped(globalstats: dict[str, str]):
    results = {
        "weapons": {},
        "maps": {},
        "gameModes": {},
        "classes": {},
        "vehicles": {},
        "gadgets": {},
        "unused": {},
    }

    for key in globalstats.keys():
        if "tp_wp_" in key and key.replace("tp_wp_", "") not in list(
            itertools.chain(bf6.WEAPONS, bf6.WEAPON_GROUPS)
        ):
            results["weapons"][key] = globalstats[key]
        if "tp_gm_" in key and key.replace("tp_gm_", "") not in list(
            itertools.chain(bf6.STAT_GAMEMODE_SMALL, bf6.STAT_GAMEMODE_SMALL_CATEGORY)
        ):
            results["gameModes"][key] = globalstats[key]
        if "tp_lvl" in key and key.replace("tp_lvl", "") not in bf6.STAT_MAPS:
            results["maps"][key] = globalstats[key]
        if "tp_kit_" in key and key.replace("tp_kit_", "") not in bf6.CLASSES:
            results["classes"][key] = globalstats[key]
        if "tp_veh_" in key and key.replace("tp_veh_", "") not in list(
            itertools.chain(bf6.VEHICLES, bf6.VEHICLE_GROUPS)
        ):
            results["vehicles"][key] = globalstats[key]
        if "tp_gad_" in key and key.replace("tp_gad_", "") not in list(
            itertools.chain(bf6.GADGETS, bf6.GADGET_GROUPS)
        ):
            results["gadgets"][key] = globalstats[key]

    keys = list(globalstats.keys())
    for key in keys:
        if not any(key.startswith(item) for item in used_methods.starts_with):
            if key not in used_methods.normal:
                results["unused"][key] = globalstats[key]

    with open("temp/unused_keys.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)


async def test_stats(data: dict, category_name: str):
    for player in data.get("playerStats", []):
        global_stats: dict[str, Any] = {}
        for category in player.get("categories", []):
            cat_fields = category.get("catFields") or []
            if category.get("catName", "") != category_name:
                continue

            for item in cat_fields:
                fields = item.get("fields", [])
                if not fields:
                    continue

                is_global = any([f.get("name") == "global" for f in fields])

                item_name = item.get("name")
                item_value = item.get("value")

                if is_global:
                    global_stats[item_name] = item_value

        with open("temp/global_stats.json", "w", encoding="utf-8") as f:
            json.dump(global_stats, f, ensure_ascii=False, indent=4)

        check_unmapped(global_stats)


async def main():
    raw_stats = find_player("LackSpuds")
    with open("temp/raw_stats.json", "w", encoding="utf-8") as f:
        json.dump(raw_stats, f, ensure_ascii=False, indent=4)
    data = await get_stats(raw_stats, "glacier_mp", False, True)
    await test_stats(raw_stats, "glacier_mp")
    with open("temp/result.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    asyncio.run(main())
