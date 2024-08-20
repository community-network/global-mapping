import requests
from global_mapping import bf2042 as statics
import checks
from filters import filters
from used import has_used

# load player
data = requests.get(
    f"https://api.gametools.network/bf2042/stats/",
    params={"name": "POPE_YNS14_AI", "raw": "true", "platform": "pc"},
).json()
# print(data)
# map to a big dictrionary
player = data.get("playerStats", [])[0]  # out of range == player not found
current_player = player.get("player", {"personaId": 0})
current_player_id = current_player.get("personaId", 0)
current_result = {
    "id": current_player_id,
    "platform": statics.PLATFORM.get(current_player.get("platformId"), "pc"),
    "platformId": current_player.get("platformId", 1),
}
for category in player.get("categories", []):
    for item in category.get("catFields", {"fields": []}).get("fields", []):
        current_result[item["name"]] = item["value"]
# # save example of current output
# with open("stats_list_player.json", "w") as outfile:
#     json.dump(dict(sorted(current_result.items())), outfile, indent=4)

# Check if everything in category is mapped
print("\nWeapons:")
checks.main(
    "tp_wp_",
    "kw_wp_",
    statics.WEAPONS,
    statics.WEAPON_GROUPS,
    current_result,
)
print("\nVehicles:")
checks.main(
    "tp_vh_",
    "dmg_vh_",
    statics.VEHICLES,
    statics.VEHICLE_GROUPS,
    current_result,
)
print("\nGamemodes:")
checks.main("tp_gm_", "wins_gm_", statics.STAT_GAMEMODE, {}, current_result)
print("\nCharacter:")
checks.main("tp_char_", "kw_char_", statics.CLASSES, {}, current_result)
print("\nGadgets:")
checks.main("tp_gad_", "tp_gad_", statics.GADGETS, {}, current_result)
print("\nMaps:")
checks.main("tp_lvl_", "wins_lvl_", statics.STAT_MAPS, {}, current_result)

# check item mapping outside of the categories
to_print = {}
for name, item in current_result.items():
    second_split = "_".join(name.split("_", 2)[:2])
    third_split = "_".join(name.split("_", 3)[:3])  #
    if (
        second_split not in filters.keys()
        and third_split not in filters.keys()
        and name not in has_used
    ):
        to_print[name] = item
print("\nOther items:")
result = dict(sorted(to_print.items()))
for key, val in result.items():
    print(f"{key} - {val}")
