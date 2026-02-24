import asyncio
import datetime
from global_mapping.readability.shared import format_percentage_value
from global_mapping import bf1 as BF1


async def get_weapons(stats_dict: dict, format_values: bool = True):
    weapons = []
    for _id, extra in BF1.WEAPONS_STATS.items():
        weapon: dict[str, str | int | float] = {**extra}

        kills = stats_dict.get(f"{_id}__kw_g", 0)
        shots_hit = stats_dict.get(f"{_id}__shw_g", 0)
        shots_fired = stats_dict.get(f"{_id}__sfw_g", 0)
        headshots = stats_dict.get(f"{_id.replace('_', '__')}_hsh_g", 0)
        seconds = stats_dict.get(f"{_id}__sw_g", 0)

        try:
            accuracy = round((shots_hit / shots_fired) * 100, 2)
        except ZeroDivisionError:
            accuracy = 0.0

        try:
            kills_per_minute = round(kills / (seconds / 60), 2)
        except (ZeroDivisionError, KeyError):
            kills_per_minute = 0.0

        try:
            hits_per_kill = round(shots_hit / kills, 2)
        except ZeroDivisionError:
            hits_per_kill = 0.0

        try:
            headshot_rate = round((headshots / kills) * 100, 2)
        except ZeroDivisionError:
            headshot_rate = 0.0

        weapon["id"] = _id
        weapon["kills"] = kills
        weapon["accuracy"] = format_percentage_value(accuracy, format_values)
        weapon["headshots"] = headshots
        weapon["headshot_rate"] = format_percentage_value(headshot_rate, format_values)
        weapon["killsPerMinute"] = kills_per_minute
        weapon["hitVKills"] = hits_per_kill
        weapon["shotsHit"] = shots_hit
        weapon["shotsFired"] = shots_fired
        weapon["timeEquipped"] = seconds
        weapons.append(weapon)
    return weapons


async def get_gamemodes(stats_dict: dict, format_values: bool = False):
    gamemodes = []
    for _id, extra in BF1.STATS_GAMEMODE.items():
        wins = stats_dict.get(f"c_mwin_{_id}", 0)
        losses = stats_dict.get(f"c_mlos_{_id}", 0)
        # try:
        #     win_percent = round(wins / (wins + losses) * 100, 2)
        # except ZeroDivisionError:
        #     win_percent = 0.0

        gamemode: dict[str, str | int | float] = {**extra}
        gamemode["id"] = _id
        # gamemode["wins"] = wins
        # gamemode["losses"] = losses
        gamemode["score"] = stats_dict.get(BF1.GAMEMODE_SCORE.get(_id, ""), 0)
        # gamemode["winPercent"] = format_percentage_value(win_percent, format_values)
        gamemodes.append(gamemode)
    return gamemodes


async def get_classes(stats_dict: dict):
    kits = []
    for kit_id, extra in BF1.STATS_CLASSES.items():
        kills = stats_dict.get(f"{kit_id}_ks_g", 0)
        # deaths = stats_dict.get(f"deaths_char_{kit_id}", 0)
        seconds = stats_dict.get(f"{kit_id}_sa_g", 0)
        # try:
        #     kill_death = round(kills / deaths, 2)
        # except ZeroDivisionError:
        #     kill_death = 0.0
        try:
            kills_per_minute = round(kills / (seconds / 60), 2)
        except (ZeroDivisionError, KeyError):
            kills_per_minute = 0.0
        kit: dict[str, str | int | float] = {**extra}
        kit["id"] = kit_id
        kit["kills"] = kills
        kit["kpm"] = kills_per_minute
        kit["secondsPlayed"] = seconds
        kit["score"] = stats_dict.get(BF1.CLASSES_SCORE.get(kit_id, ""), 0)
        kit["image"] = (
            f"https://cdn.gametools.network/classes/bf1/white/{kit['className']}.png"
        )
        kit["altImage"] = (
            f"https://cdn.gametools.network/classes/bf1/black/{kit['className']}.png"
        )
        kit["timePlayed"] = str(datetime.timedelta(seconds=kit["secondsPlayed"]))
        kits.append(kit)
    return kits


async def get_main_stats(stats_dict: dict, format_values: bool = True):
    result: dict[str, str | int | float] = {}
    wins = stats_dict.get("c_mwin__roo_g", 0)
    losses = stats_dict.get("c_mlos__roo_g", 0)
    kills = stats_dict.get("c___k_g", 0)
    deaths = stats_dict.get("c___d_g", 0)
    shots_fired = stats_dict.get("c___sfw_g", 0)
    shots_hit = stats_dict.get("c___shw_g", 0)
    headshot_amount = stats_dict.get("c___hsh_g", 0)
    matches_played = stats_dict.get("c___roo_g", 0)
    try:
        accuracy = round((shots_hit / shots_fired) * 100, 2)
    except ZeroDivisionError:
        accuracy = 0.0
    try:
        win_percent = round(wins / (wins + losses) * 100, 2)
    except ZeroDivisionError:
        win_percent = 0.0
    try:
        headshots = round((headshot_amount / kills) * 100, 2)
    except ZeroDivisionError:
        headshots = 0.0
    try:
        kill_death = round(kills / deaths, 2)
    except ZeroDivisionError:
        kill_death = 0.0

    try:
        kills_per_match = round(kills / matches_played, 2)
    except (ZeroDivisionError, KeyError):
        kills_per_match = 0.0

    result["kills"] = kills
    result["deaths"] = deaths
    result["wins"] = wins
    result["loses"] = losses
    result["killsPerMatch"] = kills_per_match
    result["headShots"] = headshot_amount
    result["roundsPlayed"] = matches_played
    result["winPercent"] = format_percentage_value(win_percent, format_values)
    result["headshots"] = format_percentage_value(headshots, format_values)
    result["accuracy"] = format_percentage_value(accuracy, format_values)
    result["killDeath"] = kill_death
    result["score"] = stats_dict.get("score", 0)
    result["revives"] = stats_dict.get("c___re_g", 0)
    result["heals"] = stats_dict.get("c___h_g", 0)
    result["repairs"] = stats_dict.get("c___r_g", 0)
    result["killAssists"] = stats_dict.get("c___kak_g", 0)
    result["shotsHit"] = shots_hit
    result["shotsFired"] = shots_fired
    result["awardScore"] = stats_dict.get("sc_award", 0)
    result["bonusScore"] = stats_dict.get("sc_bonus", 0)
    result["squadScore"] = stats_dict.get("sc_squad", 0)
    result["currentRankProgress"] = stats_dict.get("sc_rank", 0)
    result["highestKillStreak"] = stats_dict.get("c___k_ghvs", 0)
    result["dogtagsTaken"] = stats_dict.get("c___dt_g", 0)
    result["longestHeadShot"] = stats_dict.get("c___hsd_ghva", 0)
    return result


async def get_stats_bf1_blaze(
    data: dict, format_values: bool = True, with_extras: bool = True
):
    result = {}
    for player_name, stats in data.items():
        int_stats = {}
        current_result = {}
        for key, value in stats.items():
            int_stats[key] = float(value)

        if with_extras:
            tasks = []
            tasks.append(get_weapons(int_stats, format_values))
            tasks.append(get_gamemodes(int_stats, format_values))
            tasks.append(get_classes(int_stats))
            (
                current_result["weapons"],
                current_result["gamemodes"],
                current_result["classes"],
            ) = await asyncio.gather(*tasks)

        current_result.update(await get_main_stats(int_stats, format_values))

        result[player_name] = current_result
    return result
