import itertools
from global_mapping import bf6

keys = list(
    itertools.chain(
        bf6.WEAPONS.keys(),
        bf6.WEAPON_GROUPS.keys(),
        bf6.MELEE.keys(),
        bf6.MELEE_GROUPS.keys(),
        bf6.BATTLE_PICKUPS.keys(),
        bf6.STAT_GAMEMODE_SMALL.keys(),
        bf6.STAT_GAMEMODE_SMALL_CATEGORY.keys(),
        bf6.STAT_MAPS.keys(),
        bf6.CLASSES.keys(),
        bf6.VEHICLES.keys(),
        bf6.VEHICLE_GROUPS.keys(),
        bf6.VEHICLE_ARCHETYPES.keys(),
        bf6.GADGETS.keys(),
        bf6.GADGET_GROUPS.keys(),
    )
)

print(keys)
